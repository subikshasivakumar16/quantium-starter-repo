import pandas as pd
import os

# Path to data folder
data_folder = "data"

# Get all CSV files
csv_files = [file for file in os.listdir(data_folder) if file.endswith(".csv")]

# Empty list to store dataframes
all_data = []

for file in csv_files:
    file_path = os.path.join(data_folder, file)
    df = pd.read_csv(file_path)
    
    # Keep only Pink Morsels
    df = df[df["product"] == "pink morsel"]
    
    # Create sales column
    df["sales"] = df["quantity"] * df["price"]
    
    # Keep required columns
    df = df[["sales", "date", "region"]]
    
    all_data.append(df)

# Combine all files
final_df = pd.concat(all_data)

# Save output
final_df.to_csv("processed_data.csv", index=False)

print("Data processing complete. File saved as processed_data.csv")
