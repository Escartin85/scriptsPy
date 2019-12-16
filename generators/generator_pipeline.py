# using generators to find the longest name

full_names = (name.strip() for name in open('generators/names.txt'))
lenghts = ((name, len(name)) for name in full_names)
longest = max(lenghts, key=lambda x:x[1])

print(longest)

# adding separate_names generator as another stage in pipeline
def separate_names(names):
    for full_names in names:
        for name in full_names.split(' '):
            yield name

full_names = (name.strip() for name in open('generators/names.txt'))
names = separate_names(full_names)
lenghts = ((name, len(name)) for name in names)
longest = max(lenghts, key=lambda x:x[1])

print(longest)
