CSV Data Splitter

This Python script reads data from an input CSV file and writes it into two output CSV files - opportunity.csv and attribute.csv. The input CSV file must have column names starting with either "opportunity" or "attribute". The script extracts data from columns that start with "opportunity" and writes them into opportunity.csv and data from columns that start with "attribute" is written into attribute.csv.
Usage

    Install Python 3.x on your computer.
    Clone or download this repository to your local machine.
    Place your input CSV file in the same directory as the script.
    Edit the script file to specify the name of your input file.
    Run the script using the following command: python csv_data_splitter.py.

Dependencies

This script requires the following Python modules to be installed:

    csv
    os

Input

    A CSV file with header columns starting with "opportunity" or "attribute".

Output

    opportunity.csv - CSV file containing data from columns that start with "opportunity".
    attribute.csv - CSV file containing data from columns that start with "attribute".
