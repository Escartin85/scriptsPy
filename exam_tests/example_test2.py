# Implement a group_by_owners function that:
# - Accepts a dictionary containing the file owner name for echa file name
# - Returns a dictionary containing a list of file names for each owner name, in any order.
#
# For example, for dictionary {'Input.txt':'Randy','Code.py':'Stan','Output.txt':'Randy'}
# the group_by_owners function should return {'Randy':['Input.txt','Output.txt'],'Stan':['Code.py']}

class FileOwners:
    @staticmethod
    def group_by_owners(files):
        values = []
        for key, val in files.items():
            valTmp = val
            found = False
            for value in values:
                if valTmp == value:
                    found = True
                    break
            if found == False:
                values.append(val)
        newDict = {}

        for values in values:
            keyFiles = []
            for key, val in files.items():
                if value == val:
                    keyFiles.append(key)
            newDict.setdefault(value, keyFiles)
        return newDict


files = {
    'Input.txt':'Randy',
    'Code.py':'Stan',
    'Output.txt':'Randy'
}

print(FileOwners.group_by_owners(files))
