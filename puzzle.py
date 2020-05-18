from quest.game import QuestGame
from quest.map import TiledMap
from quest.sprite import Background, Wall, NPC
import arcade
import os
from quest.contrib.inventory import InventoryMixin, InventoryItemMixin
from quest.examples.grandmas_soup import GrandmasSoupGame
from quest.helpers import resolve_resource_path
from quest.strategy import RandomWalk
from quest.contrib.sprite_directionality import DirectionalMixin
from quest.sprite import QuestSprite



class PuzzleKey():
    puzzle_1=0

class PuzzleImage():
    puzzle_1=
    pass


class Puzzlepiece(InventoryItemMixin,NPC):
    description="item"

class Puzzle1(Puzzlepiece):
    description="puzzle piece 1"
