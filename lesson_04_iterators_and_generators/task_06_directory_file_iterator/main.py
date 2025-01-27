from directory_file_iterator import DirectoryFileIterator

directory_iterator = DirectoryFileIterator('dir')

for item in iter(directory_iterator):
    print(item)