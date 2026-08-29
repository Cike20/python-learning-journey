from pathlib import Path
from datetime import datetime

folder = Path("documents")

def is_standardized(filename):
    if len(filename) < 11:
        return False

    date_part = filename[:10]

    try:
        datetime.strptime(date_part, "%Y-%m-%d")
    except ValueError:
        return False

    if "_" not in filename:
        return False

    return True

def clean_filename(filename):
    cleaned = filename.lower()
    cleaned = cleaned.replace(" ", "_")
    cleaned = cleaned.replace("-", "_")
    while "__" in cleaned:
        cleaned = cleaned.replace("__", "_")
    cleaned = cleaned.strip("_")
    return cleaned

def get_unique_path(folder, desired_name, current_file):
    new_path = folder / desired_name

    if new_path == current_file:
        return new_path

    if not new_path.exists():
        return new_path

    stem = new_path.stem
    suffix = new_path.suffix
    counter = 2

    while True:
        candidate = folder / f"{stem}_{counter}{suffix}"

        if not candidate.exists():
            return candidate

        counter += 1

def build_invoice_filename(filename):
    parts = filename.split()
    if len(parts) < 5:
        return None

    year = parts[0]
    month = parts[1]
    day = parts[2]

    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return None

    if len(year) != 4:
        return None
    
    try:
        datetime(int(year), int(month), int(day))
    except ValueError:
        return None
    
    invoice_number = parts[-1]
    supplier = " ".join(parts[3:-1])
    clean_supplier = clean_filename(supplier)
    new_name = f"{year}-{month}-{day}_{clean_supplier}_{invoice_number}.pdf"
    return new_name

renamed_files = 0
skipped_files = 0
already_standardized = 0

for file in folder.iterdir():
    if not file.is_file():
        continue

    if is_standardized(file.stem):
        print(f"Already standardized: {file.name}")
        already_standardized += 1
        continue

    new_name = build_invoice_filename(file.stem)
    if new_name is None:
        print(f"Skipped invalid filename: {file.name}")
        skipped_files += 1
        continue

    new_path = get_unique_path(folder, new_name, file)

    old_name = file.name
    file.rename(new_path)
    renamed_files += 1

    print(f"{old_name} -> {new_path.name}")

print("\n--- Summary ---")
print(f"Files renamed: {renamed_files}")
print(f"Invalid files skipped: {skipped_files}")
print(f"Already standardized: {already_standardized}")