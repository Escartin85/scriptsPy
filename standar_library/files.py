# Files adn File Writing
import tempfile
import os
from os import path
import shutil

# Open a file
myFile = open("scores.txt", "w")
# w --> write
# w --> write
# w --> write
# w --> write
# Show attributes and properties of that file
print("Name " + myFile.name)
print("Mode " + myFile.mode)

# Write to a file
myFile.write("GBJ : 100\nKHD : 99\nBBB : 89")
myFile.close()

# Read the file
myFile = open("scores.txt", "r")
# print("Reading...\n" + myFile.read())
print("Reading...\n" + myFile.read(10))
myFile.seek(0)
print("Reading...\n" + myFile.read(10))

# Read the file
myFile = open("scores.txt", "r")

# Read one line at a time
print("My one line: " + myFile.readline())
myFile.seek(0)
print("My one line: " + myFile.readline())

for line in myFile:
	newHighScorer = line.replace("BBB", "PDJ")
	print(newHighScorer)

myFile.close()

# Create a temporary file
tempFile = tempfile.TemporaryFile()

# Write to a temporary file
tempFile.write(b"Save this special number for me: DK34")
tempFile.seek(0)

# Read the temporary file
print(tempFile.read())

# Close the temporary file
tempFile.close()

print()
# Print the name of the OS
print("OS: ", os.name)
print("Item exists: " + str(path.exists("standar_library/archive.zip")))
print("Item is a file: " + str(path.isfile("standar_library/archive.zip")))
print("Item is a dir: " + str(path.isdir("standar_library/archive.zip")))
print("Item dir: " + str(path.realpath("standar_library/archive.zip")))

if(path.exists("standar_library/archive.zip")):
	# Get the path to the file in the current directory
	src = path.realpath("standar_library/archive.zip")

	# let's make a backup copy by appending "bak" to the name
	dst = src + ".bak"
	dst2 = src + "2.bak"
	print()
	print(dst)
	print(dst2)

	# Copy over the permissions, modification times, and other info
	shutil.copy(src, dst)
	shutil.copystat(src, dst2)
	os.rename("standar_library/archive.zip", "standar_library/archive2.zip")
	# Rename the original file
