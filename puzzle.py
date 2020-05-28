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
from game import PirateDialogue

class Puzzle(InventoryItemMixin,NPC):
    description = "coin"
    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)


    def check(self,inventory):
        if len(inventory) == 4:
            npc_data = [
                [Portal, "portal.png", 0.1, 400, 400]
            ]
            for sprite_class, image, scale, x, y in npc_data:
                sprite = sprite_class(self.gamestate,image,scale)
                sprite.center_x = x
                sprite.center_y = y
                self.gamestate.npc_list.append(sprite)

    def on_collision(self, sprite, game):
        super().on_collision(sprite,game)
        self.check(self.gamestate.inventory())


class Portal(InventoryItemMixin,NPC):

    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)

    def on_collision(self,sprite,game):
        talk_to_pirate()
        #sprite.center_x = 100
        #sprite.center_y = 100
