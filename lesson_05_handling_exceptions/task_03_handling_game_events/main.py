from game_event_exception import GameEventException
from monster import Monster
from player import Player

try:
    player1 = Player('Knight', 200, 20)
    monster = Monster('Monster', 100, 30, 20)

    while player1.health > 0 or monster.health > 0:
        player1.hit(monster)
        monster.hit(player1)
        print(f"{player1} vs {monster}")

except GameEventException as exception:
    print(exception)
