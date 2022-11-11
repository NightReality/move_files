import glob
import sys
import shutil
import os

# 1st argument is always file_name

# Move desired file outside current folder
def move_file(path: str, extension: str):
    for file in glob.glob(os.path.join(path, "*.") + extension):
        shutil.move(file, os.path.dirname(path))
        print("Moved:", file[:15])

# Collect all directories, extension
extension = sys.argv[1]
all_dirs = []
for path in sys.argv[2:]:
    all_dirs = [os.path.join(path, a) for a in os.listdir(path) if os.path.isdir(os.path.join(path, a))]
    # all_dirs += dir_filter([path], obj_type="dir")

for dir_ in all_dirs:
    move_file(dir_, extension)
