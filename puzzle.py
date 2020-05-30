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
from quest.helpers import scale
from game import *
from quest.examples.grandmas_soup import *



class Puzzle(InventoryItemMixin,NPC):
    description = "key"
    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)

    def check(self,inventory):
        if len(inventory) == 1:
            npc_data = [
                [Portal, "portal.png", 0.1, 14*32, (100-51)*32],
            ]
            for sprite_class, image, scale, x, y in npc_data:
                sprite = sprite_class(self.gamestate,image,scale)
                sprite.center_x = x
                sprite.center_y = y
                self.gamestate.npc_list.append(sprite)

    def on_collision(self, sprite, game):
        super().on_collision(sprite,game)
        self.check(self.gamestate.inventory())


class Puzzle2(InventoryItemMixin,NPC):
    description = "coin"
    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)



    def check(self,inventory):
        if len(inventory) == 2:
            npc_data = [
                [Treasure, "treasure.png", 1, 92*32, (100-95)*32]
            ]
            for sprite_class, image, scale, x, y in npc_data:
                sprite = sprite_class(self.gamestate,image,scale)
                sprite.center_x = x
                sprite.center_y = y
                self.gamestate.npc_list.append(sprite)

    def on_collision(self, sprite,game):
        super().on_collision(sprite,game)
        self.check(self.gamestate.inventory())
        print (len(self.gamestate.npc_list))

class Treasure(InventoryItemMixin,NPC):
    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)

    def piratespawn(self):
        for i in range(5):
            npc_data = [
                [TalktoPirate, "pirate.30.39_AM.png", 1, 95*32, (100-43)*32]
            ]
            for sprite_class, image, scale, x, y in npc_data:
                sprite = sprite_class(self.gamestate,image,scale)
                sprite.center_x = x
                sprite.center_y = y
                self.gamestate.npc_list.append(sprite)
                pirate = self.gamestate.npc_list[1+i]
                walk = RandomWalk(0.05)
                pirate.strategy = walk

    def on_collision(self, sprite,game):
        game.Escape()
        super().on_collision(sprite,game)
        self.piratespawn()

class Portal(InventoryItemMixin,NPC):

    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)

    def on_collision(self,sprite,game):
        sprite.center_x = 101*32
        sprite.center_y = (100-7)*32

class TalktoPirate(InventoryItemMixin, NPC):
    repel_distance = 20

    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)

    def on_collision(self,sprite,game):
        grandmas_soup.repel(sprite)
        game.talk_with_pirate()
