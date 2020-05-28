# A Pirate Game
#
# Authors: Jared, Maddalena
from quest.dialogue import *
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
    screen_width = 500
    screen_height = 400
    left_viewport_margin = 96
    right_viewport_margin = 96
    bottom_viewport_margin = 96
    top_viewport_margin = 96
    player_initial_x = 300
    player_initial_y = 300
    player_speed = 6

    def setup_npcs(self):
        """Creates and places Grandma and the vegetables.
        """
        npc_data = [
            [Puzzle, "carrots.png", 1, 220, 640],
            [Puzzle, "mushroom.png", 1, 220, 645],
            [Puzzle, "potatoes.png", 1, 220, 600],
            [Puzzle, "tomatos.png", 1, 220, 580],
        ]
        self.npc_list = arcade.SpriteList()
        for sprite_class, image, scale, x, y in npc_data:
            sprite = sprite_class(self,image,scale)
            sprite.center_x = x
            sprite.center_y = y
            self.npc_list.append(sprite)

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
        super().setup_maps()
        sprite_classes = {
            "Obstacles": Wall,
            "Background": QuestSprite,
        }
        self.add_map(TiledMap("island/basemap.tmx",sprite_classes))

class PirateDialogue(Dialogue):
    def __init__():
        self.dialogue = Dialogue.from_ink("dialogue.ink")
        self.modal1 = DialogueModal(self, self.dialogue)

    def talk_to_pirate():
        self.open_modal(self.modal1)


class PlayerDirectional(DirectionalMixin,QuestSprite):
    pass

class Grandma(NPC):
    description= "Grandma"


if __name__ == '__main__':
    game = IslandAdventure()
    game.run()
