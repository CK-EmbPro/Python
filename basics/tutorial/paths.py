from pathlib import Path
import shutil
files= Path("path_file")
myFolder= Path("myFolder")
files = Path(myFolder/"new_fil")

files.touch()
files.write_text("Hello world of pathlib")

with open(files, "a") as f:
    f.write("\n this is an appended text file")

files.unlink()
shutil.rmtree(myFolder)
