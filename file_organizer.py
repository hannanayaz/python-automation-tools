import shutil
from pathlib import Path
name = input("enter the name of the folder you want to sort: ")
p = Path(name)

if p.exists() and p.is_dir():
    for f in p.iterdir():
        if f.is_file():
            print(f.suffix)
            
            
            if f.suffix == ".txt":
                folder = p /"text_files"
                folder.mkdir(exist_ok=True)
                shutil.move(f, folder / f.name)
                print("moved to text_files", f)

            elif f.suffix == ".jpg":
                folder = p / "photos"
                folder.mkdir(exist_ok=True)
                shutil.move(f, folder / f.name)
                print("moved to photos", f)

            elif f.suffix == ".mp3":
                folder = p / "songs"
                folder.mkdir(exist_ok=True)
                shutil.move(f, folder / f.name)
                print("moved to songs", f)

            elif f.suffix == ".mp4":
                folder = p / "videos"
                folder.mkdir(exist_ok=True)
                shutil.move(f, folder / f.name)
                print("moved to videos", f)

            elif f.suffix == ".pdf":
                folder = p / "pdfs"
                folder.mkdir(exist_ok=True)
                shutil.move(f, folder / f.name)
                print("moved to pdfs", f)

            elif f.suffix == ".py":
                folder = p / "python"
                folder.mkdir(exist_ok=True)
                shutil.move(f, folder / f.name)
                print("moved to python", f)

else:
    print("please check for correct file or correct name")
