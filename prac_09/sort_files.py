import os
import shutil

os.chdir("FilesToSort")
EXTENSIONS =[]
for directory_name, subdirectoris, filenames in os.walk("."):
    for filename in filenames:
        file = os.path.splitext(filename)
        if file[1] not in EXTENSIONS:
            EXTENSIONS.append(file[1])
            print(EXTENSIONS)

for extension in EXTENSIONS:
    os.mkdir(extension)
