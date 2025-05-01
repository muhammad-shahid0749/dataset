import os
import pandas as pd

# Specify the folder path
folder_path = r'before_merge'  # Replace with your folder path

# Get list of .jpg files in the folder
jpg_files = []
for file in os.listdir(folder_path):
    if file.lower().endswith('.jpg') and os.path.isfile(os.path.join(folder_path, file)):
        jpg_files.append(file)

# Create DataFrame
df = pd.DataFrame(jpg_files, columns=['File Name.jpg'])

# Save to Excel
df.to_excel('jpg_file_names.xlsx', index=False)

print(f"{len(jpg_files)} .jpg files successfully saved to jpg_file_names.xlsx")