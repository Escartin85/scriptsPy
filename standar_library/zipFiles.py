# Zipfile Module
import zipfile

# Open and List
zip = zipfile.ZipFile('Archive.zip', 'r')
print(zip.namelist())

# Metadata in the zip folder
for meta in zip.infolist():
	print(meta)

print()
info = zip.getinfo("list.txt")
print(info)

# Access to files in zip folder
print(zip.read("list.txt"))
with zip.open("list.txt") as f:
	print(f.read())

# Extracting files
#zip.extract("list.txt")
zip.extractall()

# Closing the zip
zip.close()