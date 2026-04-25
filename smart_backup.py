import shutil
from pathlib import Path
from datetime import datetime

folder = input("enter the folder/file name you want to backup: ")
source = Path(folder)

today = datetime.today()
date_str = today.strftime("%Y-%m-%d")

if source.exists() and source.is_dir():
    backup_folder = source.name + "_backup_" + date_str
    backup_path = Path(backup_folder)

    if backup_path.exists():
        print("backup folder already exists")
    else:
        shutil.copytree(source, backup_path)
        print("Backup created:", backup_folder)

elif source.exists() and source.is_file():
    choice = input("this is a file, do you want to backup it? (y/n): ").lower()

    if choice == "y":
        backup_file = source.stem + "_backup_" + date_str + source.suffix
        backup_path = Path(backup_file)

        if backup_path.exists():
            print("backup file already exists")
        else:
            shutil.copy2(source, backup_path)
            print("backup file created:", backup_file)

    else:
        print("backup cancelled")

else:
    print("please check for correct file or correct name")