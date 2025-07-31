import csv
from pathlib import Path

csv_file="peoples_TDSheet.csv"

folder_path=Path("low_resolution_images")
images_paths=folder_path.glob('*')

new_header=["Name","Case"]
new_file='no_images.csv'
with open(csv_file,mode='r',newline='') as file1, open(new_file,mode='w',newline='') as file2:
    reader1=csv.reader(file1)
    header=next(reader1)
    next(reader1)
    writer=csv.writer(file2)
    writer.writerow(new_header)
    
    for row in reader1:
        if row[3]=="" and row[1]!='':
            writer.writerow([row[1],"No images"])

