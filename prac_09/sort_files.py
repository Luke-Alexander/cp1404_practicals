import os
import shutil

os.chdir("FilesToSort")
extensions = []
for directory_name, subdirectoris, filenames in os.walk("."):
    for filename in filenames:
        file = os.path.splitext(filename)
        if file[1] not in extensions:
            extensions.append(file[1])
            print(extensions)
try:
    for extension in extensions:
        os.mkdir(extension[1:])
except FileExistsError:
    pass

