import os

__all__ = []


def list_folder_contents(directory, indent=0):
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    name, ext = os.path.splitext(entry.name)
                    print("  " * indent + f"File: {name} (Extension: {ext})")
                elif entry.is_dir():
                    print("  " * indent + f"Folder: {entry.name}")
                    list_folder_contents(entry.path, indent + 1)
                else:
                    print("  " * indent + f"Unknown: {entry.name}")
    except PermissionError:
        print("  " * indent + "[Permission Denied]")

# folder_path = input("Enter folder path: ")
# if os.path.isdir(folder_path):
#     list_folder_contents(folder_path)
# else:
#     print("Invalid folder path.")