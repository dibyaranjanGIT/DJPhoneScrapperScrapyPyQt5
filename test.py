import pandas as pd


df = pd.read_excel(r"phoneScrapper\Canada_Data.xlsx")
df = df[['Zip']]
df['Country'] = 'CA'

df1 = pd.read_excel(r"phoneScrapper\USA_Data.xlsx")
df1 = df1[['Zip']]
df1['Country'] = 'US'

final_df = pd.concat([df, df1])

print(final_df.columns)


final_df.to_csv(r"phoneScrapper\Country_zip.csv", index=False)

# # Function to read, rename columns, and write back to Excel

# def rename_excel_columns(input_file, output_file, new_column_names, columns_to_str):
#     try:
#         # Read the Excel file into a DataFrame
#         df = pd.read_excel(input_file)

#         # Convert specified columns to string to preserve leading zeros
#         # for column in columns_to_str:
#         #     df[column] = df[column].astype(str).str.zfill(5)  # Adjust zfill as needed for the length of leading zeros
        
#         # Rename the columns
#         df.columns = new_column_names
        
#         # Write the updated DataFrame to a new Excel file
#         df.to_excel(output_file, index=False)
        
#         print(f"Columns renamed and saved to {output_file}")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# input_file = r"phoneScrapper\Canada Data.xlsx"  # Update with the correct path
# output_file = r"phoneScrapper\Canada_Data.xlsx"  # Update with the correct path
# new_column_names = ['City', 'City Code', 'State', 'Zip']  # Adjust this list to match the number of columns in your DataFrame
# columns_to_str = ['Zip']  # List the columns that need to be converted to string

# # Call the function
# rename_excel_columns(input_file, output_file, new_column_names, columns_to_str)
