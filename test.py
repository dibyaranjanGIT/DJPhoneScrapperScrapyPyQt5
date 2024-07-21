import pandas as pd


# df = pd.read_excel(r"phoneScrapper\USA Data.xlsx")
# Function to read, rename columns, and write back to Excel
def rename_excel_columns(input_file, output_file, new_column_names):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(input_file)
    
    # Rename the columns
    df.columns = new_column_names
    
    # Write the updated DataFrame to a new Excel file
    df.to_excel(output_file, index=False)

# Example usage

new_column_names = ['City', 'CityCode', 'State', 'Zip']  # Adjust this list to match the number of columns in your DataFrame

# Call the function
rename_excel_columns(r"phoneScrapper\Canada Data.xlsx", r"phoneScrapper\Canada_Data.xlsx", new_column_names)
