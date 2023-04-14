import csv
import os

# Get the absolute path of the current module's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define input and output file paths relative to the script directory
input_file = os.path.join(script_dir, "input.csv")
opportunity_file = "opportunity.csv"
attribute_file = "attribute.csv"

# Create output directories if they don't exist
output_dir = os.path.join(script_dir, "output")
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Open input and output files
with open(input_file, 'r') as csv_file, \
     open(os.path.join(output_dir, opportunity_file), 'w', newline='') as opportunity_csv, \
     open(os.path.join(output_dir, attribute_file), 'w', newline='') as attribute_csv:

    # Create CSV readers and writers
    reader = csv.reader(csv_file)
    opportunity_writer = csv.writer(opportunity_csv)
    attribute_writer = csv.writer(attribute_csv)

    # Read header row
    header = next(reader)

    # Write headers to output files
    opportunity_header = [col.split(".", 1)[-1] for col in header if col.startswith("opportunity")]
    attribute_header = [col.split(".", 1)[-1] for col in header if col.startswith("attribute")]

    opportunity_writer.writerow(opportunity_header)
    attribute_writer.writerow(attribute_header)

    # Count total rows in input file
    total_rows = len(list(reader))

    # Reset file pointer to beginning of input file
    csv_file.seek(0)

    # Skip header row
    next(reader)

    # Write data rows to output files with progress bar
    for i, row in enumerate(reader):
        opportunity_data = [row[i] for i in range(len(header)) if header[i].startswith("opportunity")]
        attribute_data = [row[i] for i in range(len(header)) if header[i].startswith("attribute")]

        opportunity_writer.writerow(opportunity_data)
        attribute_writer.writerow(attribute_data)

        # Print progress bar
        progress = i / (total_rows - 1) * 100
        print(f"Progreso: [{int(progress):<20}] {i + 1}/{total_rows} filas", end="\r")

    # Print completion message
    print("Completado!")