import os
import csv

# Get the path to the output folder
folder_path = os.path.join(os.getcwd(), 'output')

# Loop through all CSV files in the output folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        print(f"File: {filename}\n")
        
        # Open the CSV file and create a reader object
        with open(os.path.join(folder_path, filename), 'r') as csvfile:
            csvreader = csv.reader(csvfile)

            # Get the headers from the first row
            headers = next(csvreader)

            # Calculate the maximum width of each column
            column_widths = [len(header) for header in headers]
            for row in csvreader:
                for i, value in enumerate(row):
                    column_widths[i] = max(column_widths[i], len(value))

            # Print the headers
            for i, header in enumerate(headers):
                print(header.ljust(column_widths[i]), end='  ')
            print()

            # Print the separator line
            separator = '-' * (sum(column_widths) + len(column_widths) - 1)
            print(separator)

            # Print each row
            csvfile.seek(0)  # Rewind to the beginning of the file
            next(csvreader)  # Skip the header row
            for row in csvreader:
                for i, value in enumerate(row):
                    print(value.ljust(column_widths[i]), end='  ')
                print()

            # Add a blank line after each file
            print()