from json_manager import JsonManager

# # Read JSON file
# for row in JsonManager.read_file('books.json'):
#     print(row)
#
# # Get available books
# print('Available books:')
# for available_book in JsonManager.get_available_book_list('books.json'):
#     print(available_book)

# Add book
try:
    JsonManager.add_book('books.json',
                         {"name": "Burning Daylight", "author": "Jack London", "year": "1910", "isAvailable": True})
except Exception as exception:
    print(exception)
