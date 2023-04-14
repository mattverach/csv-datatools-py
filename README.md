CSV Data Tools

This repository contains two Python scripts for working with CSV data - splitter.py and verify.py.
splitter.py

This script reads data from an input CSV file and writes it into two output CSV files - opportunity.csv and attribute.csv. The input CSV file must have header column names starting with either "opportunity" or "attribute". The script extracts data from columns and writes them to their respective output files.
Usage

    Install Python 3.x on your computer.
    Clone or download this repository to your local machine.
    Place your input CSV file in the root directory of the repository.
    Run the script using the following command: python csv_data_splitter.py.
    The output CSV files will be generated in the output directory.

Dependencies

This script requires the following Python modules to be installed:

    os
    csv

Input

    One CSV file located in the root directory of the repository.

Output

    Two CSV files located in the output directory, named opportunity.csv and attribute.csv.

verify.py

This script is designed to display the contents of CSV files in a readable format. It reads all CSV files located in the output folder created by the previous script and prints their contents to the console.
Usage

    Install Python 3.x on your computer.
    Clone or download this repository to your local machine.
    Place your output CSV files in the output directory.
    Run the script using the following command: python csv_data_viewer.py.

Dependencies

This script requires the following Python modules to be installed:

    os
    csv

Input

    CSV files located in the output directory.

Output

    Console output showing the contents of each CSV file. The output is formatted to be readable, with headers aligned and separated from the data by a separator line.
