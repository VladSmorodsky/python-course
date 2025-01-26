from directory_image_iterator import DirectoryImageIterator
from csv_writer import write_csv

image_directory = DirectoryImageIterator('image_dir')  # Create directory iterator
images_data = [['File Name', 'Format', 'Size (KB)']]  # list with content
while True:
    try:
        images_data.append(next(image_directory))
    except StopIteration:
        break

write_csv('image_data.csv', iter(images_data))  # create new file and write content into it
