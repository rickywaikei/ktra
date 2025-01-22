import pandas as pd
from sqlalchemy import create_engine, text
import os
import json  # Import json module for handling JSON files
import django
from datetime import date, datetime  # Import date and datetime for type checking
from django.db import connection  # Import connection to execute raw SQL

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kproject.settings')
django.setup()

from django.contrib import admin
from django.contrib.auth.models import User
from events.models import Event
from services.models import Service

def serialize_data(queryset):
    """Convert queryset to a list of dictionaries, exclude 'id', and serialize date fields."""
    data = []
    for item in queryset:
        item_dict = item.copy()  # Create a copy of the dictionary
        item_dict.pop('id', None)  # Exclude the 'id' field
        for key, value in item_dict.items():
            if isinstance(value, (date, datetime)):
                item_dict[key] = value.isoformat()  # Convert to ISO format string
        data.append(item_dict)
    return data

def reset_sequence(model):
    """Reset the primary key sequence for the specified model."""
    with connection.cursor() as cursor:
        table_name = model._meta.db_table  # Get the table name
        cursor.execute(f"ALTER SEQUENCE {table_name}_id_seq RESTART WITH 1;")  # Reset sequence

def truncate_table(model):
    """Truncate the table for the specified model with CASCADE."""
    with connection.cursor() as cursor:
        table_name = model._meta.db_table  # Get the table name
        cursor.execute(f"TRUNCATE TABLE {table_name} CASCADE;")  # Truncate table with cascade

def main():
    myinput = input("What do you want to do? 1 = Data Import, 2 = Data Export: ")

    if myinput == '1':
        print("You selected Data Import.")
        filePath = input("Please paste your .json path here: ")
        try:
            # Read the JSON file into a DataFrame
            df = pd.read_json(filePath)

            # Data Cleansing
            df.drop_duplicates(inplace=True)
            print("Data cleansing complete. Here is the cleansed data:")
            print(df.head())

            if input("Do you want to save your cleansed data file? 1 = Yes, 2 = No: ") == "1":
                output_path = 'cleansed_data.json'
                df.to_json(output_path, orient='records', lines=True)  # Save as JSON
                print(f"Cleansed data saved to {output_path}")

            if input("Do you want to import your data to the database? 1 = Yes, 2 = No: ") == "1":
                while True:
                    importTable = input("Which model/table do you want to import to (1: Service, 2: Event, 3: User): ")
                    if importTable in ['1', '2', '3']:
                        if importTable == '1':
                            model = Service
                        elif importTable == '2':
                            model = Event
                        else:
                            model = User

                        if input(f"Do you want to format table - {model.__name__}? 1 = Yes, 2 = No : ") == "1":
                            truncate_table(model)  # Truncate the table instead of deleting entries
                            print(f"{model.__name__} truncated.")
                            reset_sequence(model)  # Reset the sequence after truncation

                        # Import data into the model
                        for index, row in df.iterrows():
                            instance = model(**row.to_dict())
                            instance.save()
                        print(f"Successfully imported data to {model.__name__} from {filePath}")

                        if input("Do you need to register the model in admin cms? 1=Yes, 2=No: ") == "1":
                            if admin.site.is_registered(model):
                                print(f"{model.__name__}Admin is already registered.")
                            else:
                                class ModelAdmin(admin.ModelAdmin):
                                    list_display = ('id', 'username') if model == User else ('title',)  # Customize based on model
                                    list_display_link = "id",  # Customize based on model
                                admin.site.register(model, ModelAdmin)
                                print(f"{model.__name__}Admin is registered.")
                        break
                    else:
                        print("Input Error, Please select 1-3.")
        except Exception as e:
            print(f"An error occurred: {e}")  # Handle exceptions appropriately

    elif myinput == '2':
        print("You selected Data Export.")
        while True:
            exportTable = input("Which model/table do you want to export from (1: Service, 2: Event, 3: User): ")
            if exportTable in ['1', '2', '3']:
                if exportTable == '1':
                    model = Service
                elif exportTable == '2':
                    model = Event
                else:
                    model = User

                # Query all objects from the selected model
                queryset = model.objects.all().values()  # Use .values() to get a queryset of dictionaries
                data = serialize_data(queryset)  # Serialize data to handle date fields and exclude 'id'

                # Export to JSON
                output_path = f'{model.__name__.lower()}_data.json'
                with open(output_path, 'w', encoding='utf-8') as json_file:
                    json.dump(data, json_file, ensure_ascii=False, indent=4)  # Save data to JSON
                print(f"Data exported to {output_path}")
                break
            else:
                print("Input Error, Please select 1-3.")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()