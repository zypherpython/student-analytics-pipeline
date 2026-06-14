import csv
import psycopg2

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
        student = (row['ID'], row['NAME'], row['AGE'], row['COURSE'], row['GRADE'])
        
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
        
        # Check for missing course values
        if row['COURSE'] == "":
            removed += 1
            continue
        
        # Normalize name to title case
        row['NAME'] = row['NAME'].title()
        
        seen.add(student)
        clean_data.append(row)
        
    print(f'{removed} records removed during transformation')
    return clean_data

def load(data):
    """Load cleaned data into PostgreSQL database using psycopg.
    
    Args:
        data: List of cleaned student records to insert into database
        
    Requires:
        - PostgreSQL database named 'STUDENT_ANALYSIS'
        - 'students' table with columns: ID, NAME, AGE, COURSE, GRADE
    """
    try:
        conn = psycopg2.connect(
            dbname='STUDENT_ANALYSIS',
            user='youruser',
            password='yourpassword',
            host='localhost',
            port='5432'
        )
        cur = conn.cursor()
        
        # Insert records into database
        for row in data:
            cur.execute(
                '''
                INSERT INTO students
                (ID, NAME, AGE, COURSE, GRADE)
                VALUES (%s, %s, %s, %s, %s)
                ''',
                (row['ID'], row['NAME'], row['AGE'], row['COURSE'], row['GRADE'])
            )
        
        conn.commit()
        cur.close()
        conn.close()
        print(f'Successfully loaded {len(data)} records into database')
        
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        return False
    
    return True

def main():
    """Execute complete ETL pipeline: Extract → Transform → Load"""
    data = extract('data/messy_students_100.csv')
    clean_data = transform(data)
    load(clean_data)

if __name__ == '__main__':
    main()
