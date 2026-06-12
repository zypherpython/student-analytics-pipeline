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