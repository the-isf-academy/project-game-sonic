# A Pirate Game
#
# Authors: Jared, Maddalena

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
    player_scaling=1
    screen_width = 1000
    screen_height = 750
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
            [Grandma, "pirate.30.39_AM.png", 0.3, 400, 400],
            [Carrots, "carrots.png", 1, 220, 640],
            [Mushroom, "mushroom.png", 1, 1028, 264],
            [Potatoes, "potatoes.png", 1, 959, 991],
            [Tomatos, "tomatos.png", 1, 323, 1055],
        ]
        self.npc_list = arcade.SpriteList()
        for sprite_class, image, scale, x, y in npc_data:
            sprite = sprite_class(image, scale)
            sprite.center_x = x
            sprite.center_y = y
            self.npc_list.append(sprite)

        grandma = self.npc_list[0]
        walk = RandomWalk(0.05)
        grandma.strategy = walk

    def setup_player(self):
        self.player = PlayerDirectional(self.player_sprite_image_lr,self.player_sprite_image_up,self.player_sprite_image_down,self.player_scaling)
        self.player.center_x = self.player_initial_x
        self.player.center_y = self.player_initial_y
        self.player.speed = self.player_speed
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)


class PlayerDirectional(DirectionalMixin,QuestSprite):
    pass

class Grandma(NPC):
    description= "Grandma"

class Vegetable(InventoryItemMixin,NPC):
    """A vegetable is an NPC that can be picked up.
    """
    description = "item"

class Carrots(Vegetable):
    description = "carrots"

class Mushroom(Vegetable):
    description = "mushroom"

class Potatoes(Vegetable):
    description = "potatoes"

class Tomatos(Vegetable):
    description = "tomatos"


if __name__ == '__main__':
    game = IslandAdventure()
    game.run()
