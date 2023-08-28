# pathlib  
from pathlib import Path

# absolute path
# c:/Program file/..
# relative path
# ../

path = Path("public")
print(path.exists())
if path.exists():
    print("exists")
else:
    path.mkdir()


# path.rmdir()

paths = Path()
print(paths.glob('*.py'))

for file in paths.glob('*'):
    print(file)

