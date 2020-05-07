# A Pirate Game
#
# Authors: Jared, Maddalena

from quest.game import QuestGame
from quest.map import TiledMap
from quest.sprite import Background, Wall, NPC
import arcade
import os
from quest.contrib.inventory import InventoryMixin, InventoryItemMixin
from pathlib import Path


def resolve_path(relative_path):
    """A helper function to find images and other resources.
    """
    here = Path(os.path.abspath(__file__)).parent
    return str(here / relative_path)

class IslandAdventure(InventoryMixin,QuestGame):
    """A very simple subclass of :py:class:`QuestGame`.

    To run this example::

        $ python -m quest.examples.island

    :py:class:`IslandAdventure` shows off the basic features of the Quest
    framework, loading a map and letting the player explore it.
    After you play it, check out the sorce code by clicking on "source" in the
    blue bar just above.
    """

    player_sprite_image = resolve_path("images/boy_simple.png")
    screen_width = 1000
    screen_height = 750
    left_viewport_margin = 96
    right_viewport_margin = 96
    bottom_viewport_margin = 96
    top_viewport_margin = 96
    player_initial_x = 0
    player_initial_y = 0
    player_speed = 6

    def setup_maps(self):
        """Sets up the map.

        Uses a :py:class:`TiledMap` to load the map from a ``.tmx`` file,
        created using :doc:`Tiled <tiled:manual/introduction>`.
        """
        super().setup_maps()
        sprite_classes = {
            "Obstacles": Wall,
            "Background": Background,
        }
        island_map = TiledMap(resolve_path("images/island/island.tmx"), sprite_classes)
        self.add_map(island_map)

    def setup_walls(self):
        """Assigns sprites to `self.wall_list`. These sprites will function as walls, blocking
        the player from passing through them.
        """
        self.wall_list = self.get_current_map().get_layer_by_name("Obstacles").sprite_list

    def setup_npcs(self):
        """Creates and places Grandma and the vegetables.
        """
        npc_data = [
            [Grandma, "images/people/grandma.png", 3, 400, 400],
            [Carrots, "images/items/carrots.png", 1, 220, 640],
            [Mushroom, "images/items/mushroom.png", 1, 1028, 264],
            [Potatoes, "images/items/potatoes.png", 1, 959, 991],
            [Tomatos, "images/items/tomatos.png", 1, 323, 1055],
        ]
        self.npc_list = arcade.SpriteList()
        for sprite_class, image, scale, x, y in npc_data:
            sprite = sprite_class(resolve_path(image), scale)
            sprite.center_x = x
            sprite.center_y = y
            self.npc_list.append(sprite)

        grandma = self.npc_list[0]
        walk = RandomWalk(0.05)
        grandma.strategy = walk


class Vegetable(NPC):
    """A vegetable is an NPC that can be picked up.
    """
    description = "item"
    def on_collision(self, sprite, game):
        """When the player collides with a vegetable, it tells the game and then
        kills itself.
        """
        game.got_item(self.description)
        self.kill()

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
