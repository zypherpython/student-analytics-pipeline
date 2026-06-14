import csv

def extract(filename):
    """Extract data from a CSV file."""

    data = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:

            reader = csv.DictReader(file)

            for row in reader:
                data.append(row)

            print(f"Extracted {len(data)} records")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return []

    return data

def transform(data):
    """Transform and clean student data.
    
    Args:
        data: List of dictionaries containing student records
        
    Returns:
        clean_data: List of cleaned and normalized student records
    """
    clean_data = []
    removed = 0
    seen = set()
    
    for row in data:
        student = (row['ID'], row['NAME'], row['AGE'], row['GRADE'])
        
        # Check for duplicates
        if student in seen:
            removed += 1
            continue
            
        # Validate grade range (0-100)
        if int(row['GRADE']) < 0 or int(row['GRADE']) > 100:
            removed += 1
            continue
            
        # Check for missing age values
        if row['AGE'] == "":
            removed += 1
            continue
        
        # Normalize name to title case
        row['NAME'] = row['NAME'].title()
        
        seen.add(student)
        clean_data.append(row)
        
    print(f'{removed} records removed during transformation')
    return clean_data
