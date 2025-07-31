from pathlib import Path
import csv
path=Path("Total")

all_images=path.glob("*/*.*")

csv_file = "workers_names.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name'])  
    for path in all_images:
        name = Path(path).stem
        writer.writerow([name])


