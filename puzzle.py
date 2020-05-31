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
from quest.examples.grandmas_soup import Grandma



class Puzzle(InventoryItemMixin,NPC):
    description = "key"
    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)

    def check(self,inventory):
        if len(inventory) == 4:
            npc_data = [
                [Portal, "island/portal.png", 0.1, 14*32, (100-51)*32],
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
        if len(inventory) == 9:
            npc_data = [
                [Treasure, "island/loot.png", 0.6, 91.5*32, (100-96.5)*32]
            ]
            for sprite_class, image, scale, x, y in npc_data:
                sprite = sprite_class(self.gamestate,image,scale)
                sprite.center_x = x
                sprite.center_y = y
                self.gamestate.npc_list.append(sprite)

    def on_collision(self, sprite, game):
        super().on_collision(sprite,game)
        self.check(self.gamestate.inventory())

class Treasure(InventoryItemMixin,NPC):
    description="Treasure"
    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)

    def check(self,inventory):
        if len(inventory) == 10:
            npc_data = [
                [Puzzle, "island/piratesword.png", 0.45, 86*32, (100-90.5)*32],
                [Puzzle, "island/pirategun.png", 0.45, 83*32, (100-91)*32],
                [Puzzle, "island/piratesword.png", 0.45, 90.7*32, (100-89)*32],
                [Puzzle, "island/pirategun.png", 0.45, 90*32, (100-85)*32],
                #Pirate:
                [PirateLord, "island/piratesword.png", 0.45,91.5*32,(100-91)*32],
                [Puzzle, "island/piratesword.png", 0.45,89*32,(100-82)*32],
                [Puzzle, "island/pirategun.png", 0.45,86*32,(100-81)*32],
                [Puzzle, "island/piratesword.png", 0.45,85*32,(100-79)*32],
                [Puzzle, "island/pirategun.png", 0.45,88*32,(100-91)*32],
                [Puzzle, "island/piratesword.png", 0.45,80*32,(100-90)*32],
                [Puzzle, "island/pirategun.png", 0.45,78*32,(100-89)*32],
                #Down:
                [Puzzle, "island/shipd.png", 0.5,92*32,(100-79)*32],
                [Puzzle, "island/shipd.png", 0.5,89*32,(100-76)*32],
                [Puzzle, "island/shipd.png", 0.5,92*32,(100-74)*32],
                [Puzzle, "island/shipd.png", 0.5,88*32,(100-71)*32],
                [Puzzle, "island/shipd.png", 0.5,86*32,(100-74)*32],
                #Left:
                [Puzzle, "island/shipl.png", 0.5,96*32,(100-83)*32],
                [Puzzle, "island/shipl.png", 0.5,95*32,(100-86)*32],
                [Puzzle, "island/shipl.png", 0.5,97*32,(100-88)*32],
                [Puzzle, "island/shipl.png", 0.5,99*32,(100-85)*32],
                [Puzzle, "island/shipl.png", 0.5,100*32,(100-90)*32],
                [Puzzle, "island/shipl.png", 0.5,101*32,(100-93)*32],
                [Puzzle, "island/shipl.png", 0.5,98*32,(100-96)*32],
                [Puzzle, "island/shipl.png", 0.5,103*32,(100-97)*32],
                [Puzzle, "island/shipl.png", 0.5,101*32,(100-89)*32],
                #Right:
                [Puzzle, "island/shipr.png", 0.5,83*32,(100-94)*32],
                [Puzzle, "island/shipr.png", 0.5,80*32,(100-97)*32],
                [Puzzle, "island/shipr.png", 0.5,77*32,(100-94)*32],
                [Puzzle, "island/shipr.png", 0.5,85*32,(100-96)*32],
                [Puzzle, "island/shipr.png", 0.5,76*32,(100-96)*32],
            ]
            for sprite_class, image, scale, x, y in npc_data:
                sprite = sprite_class(self.gamestate,image,scale)
                sprite.center_x = x
                sprite.center_y = y
                self.gamestate.npc_list.append(sprite)

    def on_collision(self, sprite, game):
        super().on_collision(sprite,game)
        self.check(self.gamestate.inventory())
        game.pirateambush()

class PirateLord(NPC):
    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)

    def on_collision(self,sprite,game):
        sprite.center_x = 91.5*32
        sprite.center_y = (100-92.5)*32
        game.talk_with_pirate()
        sprite.stop()
        npc_data = [
            [End, "island/portal.png", 0.0001, 91.5*32, (100-93.5)*32],
        ]
        for sprite_class, image, scale, x, y in npc_data:
            sprite = sprite_class(self.gamestate,image,scale)
            sprite.center_x = x
            sprite.center_y = y
            self.gamestate.npc_list.append(sprite)

class End(NPC):
    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)

    def on_collision(self,sprite,game):
        game.game_over = True
        sprite.center_x = 179.5*32
        sprite.center_y = (100-47)*32

class Portal(InventoryItemMixin,NPC):

    def __init__(self,gamestate,image,scale):
        self.gamestate=gamestate
        super().__init__(image,scale)

    def on_collision(self,sprite,game):
        sprite.center_x = 101*32
        sprite.center_y = (100-7)*32
