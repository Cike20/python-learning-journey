from pathlib import Path

def create_folder(parent_folder, folder_name):
    new_folder = parent_folder / folder_name
    new_folder.mkdir(exist_ok=True)
    return new_folder

def move_file(file, destination_folder):
    destination = destination_folder / file.name

    if destination.exists():
        print(f"Skipped duplicate: {file.name}")
        return "skipped"

    file.rename(destination)
    print(f"{file.name} -> {destination_folder.name}")
    return "moved" 

folder = Path("documents")
office_folder = create_folder(folder, "Office")
travel_folder = create_folder(folder, "Travel")
meals_folder = create_folder(folder, "Meals")
uncategorized_folder = create_folder(folder, "Uncategorized")

rules = {
    "office": office_folder,
    "train": travel_folder,
    "lunch": meals_folder
}

moved_files = 0
skipped_files = 0

category_counts = {
    "Office": 0,
    "Travel": 0,
    "Meals": 0,
    "Uncategorized": 0
}

for file in folder.iterdir():
    if not file.is_file():
        continue

    matched = False

    for keyword, destination_folder in rules.items():
        if keyword in file.name.lower():
            matched = True
            result = move_file(file, destination_folder)
            if result == "moved":
                moved_files += 1
                category_counts[destination_folder.name] += 1
            else:
                skipped_files += 1
            break

    if not matched:
        result = move_file(file, uncategorized_folder)
        if result == "moved":
            moved_files += 1
            category_counts["Uncategorized"] += 1
        else:
            skipped_files += 1
print("\n--- Summary ---")
print(f"Files moved: {moved_files}")
print(f"Duplicates skipped: {skipped_files}")

for category, count in category_counts.items():
    print(f"{category}: {count}")