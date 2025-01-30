from sword import Sword
from player import Player
from shop import Shop

try:
    # Initialize shop and add items
    shop = Shop()
    sword = Sword('Sword', 30, 20)
    shop.add_to_shop(sword)
    shop.add_to_shop(sword)
    print(shop.attack_items.items)  # 2 swords

    # Player try to purchase sword
    player = Player('Test', 20)
    player.buy(shop, sword)

except Exception as exception:
    print(exception)
