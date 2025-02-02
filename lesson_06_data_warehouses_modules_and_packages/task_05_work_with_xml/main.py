from xml_manager import XMLManager

# Read XML file
for product in XMLManager.read_file('products.xml'):
    print(product)

# Decrease items
XMLManager.decrease_product_count('products.xml', 'Хліб', 2)
XMLManager.increase_product_count('products.xml', 'Хліб', 4)
