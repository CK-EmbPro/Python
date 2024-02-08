from pathlib import Path
import shutil
path= Path()

glob_path=path.glob("*")

for file in glob_path:
    print(file)