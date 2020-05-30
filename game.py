# A Pirate Game
#
# Authors: Jared, Maddalena
from quest.dialogue import *
from quest.modal import *
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
from puzzle import *


class IslandAdventure(InventoryMixin,GrandmasSoupGame):
    """A very simple subclass of :py:class:`QuestGame`.

    To run this example::

        $ python -m quest.examples.island

    :py:class:`IslandAdventure` shows off the basic features of the Quest
    framework, loading a map and letting the player explore it.
    After you play it, check out the sorce code by clicking on "source" in the
    blue bar just above.
    """
    player_sprite_image_lr="boy.png"
    player_sprite_image_down="boy_simple.png"
    player_sprite_image_up="boy_copy.png"
    player_scaling=0.7
    screen_width = 1000
    screen_height = 750
    left_viewport_margin = 96
    right_viewport_margin = 96
    bottom_viewport_margin = 96
    top_viewport_margin = 96
    player_initial_x = 5*32
    player_initial_y = (100-50)*32
    player_speed = 10

    def __init__(self):
        super().__init__()
        self.dialogue = Dialogue.from_ink("dialogue.ink")
        self.modal = DialogueModal(self, self.dialogue)
        self.dialogue1 = Dialogue.from_ink("dialogue1.ink")
        self.modal1= DialogueModal(self, self.dialogue1)
        self.dialogue2 = Dialogue.from_ink("dialogue2.ink")
        self.modal2= DialogueModal(self, self.dialogue2)
        self.dialogue3 = Dialogue.from_ink("dialogue3.ink")
        self.modal3= DialogueModal(self, self.dialogue3)
        self.InitTalk()

    def talk_with_pirate(self):
        self.open_modal(self.modal)

    def Talk2(self):
        self.open_modal(self.modal2)

    def Escape(self):
        self.open_modal(self.modal3)

    def setup_npcs(self):
        """Creates and places Grandma and the vegetables.
        """
        npc_data = [
            [Puzzle, "key.png", 1, 9*32, (99-31)*32],
            [Puzzle, "key1.png", 1, 34*32, (100-34)*32],
            [Puzzle, "key2.png", 1, 12*32, (100-60)*32],
            [Puzzle, "key3.png", 1, 35*32, (100-61)*32],
            [Puzzle2, "carrots.png", 1, 65*32, (99-15)*32],
            [Puzzle2, "mushroom.png", 1, 136*32, (100-10)*32],
            [Puzzle2, "potatoes.png", 1, 128*32, (100-72)*32],
            [Puzzle2, "tomatos.png", 1, 45*32, (100-92)*32],
            [Puzzle2, "tomatos.png", 1, 135*32, (100-92)*32],
        ]
        self.npc_list = arcade.SpriteList()
        for sprite_class, image, scale, x, y in npc_data:
            sprite = sprite_class(self,image,scale)
            sprite.center_x = x
            sprite.center_y = y
            self.npc_list.append(sprite)

    def SpriteList(self):
        self.npc_list = arcade.SpriteList()
        return npc_list

    def setup_player(self):
        self.player = PlayerDirectional(self.player_sprite_image_lr,self.player_sprite_image_up,self.player_sprite_image_down,self.player_scaling)
        self.player.center_x = self.player_initial_x
        self.player.center_y = self.player_initial_y
        self.player.speed = self.player_speed
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

    def setup_maps(self):
        """Sets up the standard island map.
        """
        self.maps=[]
        sprite_classes = {
            "Background": QuestSprite,
            "Obstacles": Wall,
        }
        self.add_map(TiledMap("island/combinedmaps.tmx",sprite_classes))

    def InitTalk(self):
        self.open_modal(self.modal1)


class PlayerDirectional(DirectionalMixin,QuestSprite):
    pass

if __name__ == '__main__':
    game = IslandAdventure()
    game.run()
