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
from quest.examples.grandmas_soup import *
from quest.helpers import resolve_resource_path
from quest.strategy import RandomWalk
from quest.contrib.sprite_directionality import DirectionalMixin
from quest.sprite import QuestSprite
from puzzle import *

class IslandAdventure(InventoryMixin,GrandmasSoupGame):
    """
    Main game class that runs the game
    """
    player_sprite_image_lr="island/boy.png"
    player_sprite_image_down="island/boy_simple.png"
    player_sprite_image_up="island/boy_copy.png"
    player_scaling=0.7
    screen_width = 500
    screen_height = 500
    left_viewport_margin = 96
    right_viewport_margin = 96
    bottom_viewport_margin = 96
    top_viewport_margin = 96
    player_initial_x = 5*32
    player_initial_y = (100-50)*32
    player_speed = 6

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

    instruction_shortcut = arcade.key.P

    def on_key_press(self, key, modifier):
        """
        Opens the instructions when you press "P" key
        """
        if key == self.instruction_shortcut:
            self.open_modal(self.modal1)
        else:
            super().on_key_press(key, modifier)

    def talk_with_pirate(self):
        """
        Opens the talk with pirate dialogue(dialogue.ink)
        """
        self.open_modal(self.modal)

    def pirateambush(self):
        """
        Opens the pirate ambush dialogue(dialogue2.ink)
        """
        self.open_modal(self.modal2)

    def setup_npcs(self):
        """Creates and places the keys and artifacts.
        """
        npc_data = [
            [Puzzle, "island/key.png", 1, 9*32, (99-31)*32],
            [Puzzle, "island/key1.png", 1, 34*32, (100-34)*32],
            [Puzzle, "island/key2.png", 1, 12*32, (100-60)*32],
            [Puzzle, "island/key3.png", 1, 35*32, (100-61)*32],
            [Puzzle2, "island/amulet.png", 1, 65*32, (99-15)*32],
            [Puzzle2, "island/godstatue.png", 1, 136*32, (100-10)*32],
            [Puzzle2, "island/statue.png", 1, 128*32, (100-72)*32],
            [Puzzle2, "island/cat.png", 0.7, 45*32, (100-92)*32],
            [Puzzle2, "island/goblet.png", 0.6, 135*32, (100-92)*32],
        ]
        self.npc_list = arcade.SpriteList()
        for sprite_class, image, scale, x, y in npc_data:
            sprite = sprite_class(self,image,scale)
            sprite.center_x = x
            sprite.center_y = y
            self.npc_list.append(sprite)

    def SpriteList(self):
        """
        Returns NPC list
        """
        self.npc_list = arcade.SpriteList()
        return npc_list

    def setup_player(self):
        """
        Sets up the player
        """
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
        """
        Starts the instruction dialogue
        """
        self.open_modal(self.modal1)

    def on_draw(self):
        super().on_draw()
        if self.game_over:
            self.draw_game_over()

    def draw_game_over(self):
        """
        Draw "The End" across the screen and reports the notification statistics
        to the player at the end of the game. Also draws "Game by Jared & Maddalena"

        Code from Python Arcade library documentation:
        https://arcade.academy/examples/instruction_and_game_over_screens.html
        """
        output = "The End"
        arcade.draw_text(output, self.view_left + self.screen_width/2, self.view_bottom + self.screen_height/1.5,
            arcade.color.WHITE, 54, align="center", anchor_x="center", anchor_y="center")

        output = "Game by Jared & Maddalena"
        arcade.draw_text(output, self.view_left + self.screen_width/2, self.view_bottom + self.screen_height/2.5,
            arcade.color.WHITE, 24, align="center", anchor_x="center", anchor_y="center")

class PlayerDirectional(DirectionalMixin,QuestSprite):
    pass

if __name__ == '__main__':
    game = IslandAdventure()
    game.run()
