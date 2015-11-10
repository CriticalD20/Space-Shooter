"""
spaceshooter.py
Author: James Napier
Credit: Space War Source Code

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""


#still need to flesh out what I need to write on my own
#some parts of the classes need to be redefined so that they are not including elements included in the SpaceWar Source Code


from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class GravitySprite(Sprite):
    def step(self
    #not sure how to translate this -->class GracitySprite(Sprite)<-- from the sourcecode 
class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512

    def __init__(self, position):
        super().__init__(Stars.asset, position)

class Ship(GravitySprite):
    
    def registerKeys(self, leys):
        commans = ["left", "right", "forward"]
        self.keymap = dict(zip(keys, commands))
        [self.app.listenKeyEvent("keydown", k, self.controldown) for k in keys]
        [self.app.listenKeyEvent("keyup", k, self.controlup) for k in keys]
class Ship1(Ship):
        asset = imageAsset("images/four_spaceship_by_albertiv_with_thrust.png",
            Frame(227,0,292-227,125), 4, 'vertical')
            
        def_init_(self, app, position, velocity):
            super()._init_(Ship1.asset, app, position, velocity)
            self.registerKeys(["a", "d", "w"])
            
        def step(self, t, dT):
            super().step(T, dT)
            if self.visible:
                collides = self.collidingWithSprites(Ship2)
                if len(collides):
                        if collides[0].visible:
                            collides[0].explode()
                            self.explode()
                            
class Ship2(Ship):
        asset=ImageAsset("images/four_spaceship_by_albertov_with_thrust.png",
            Frame(0,0,86,125), 4, 'vertical')
            
        def_init_(self, app, position, velocity):
            super()._init_(Ship2.asset, app, position, velocity)
            self.registerKeys(["left arrow", "right arrow", "up arrow"])
            
        def step(self, T, dT):
            super().step(T, dT)
            if self.visible:
                collides = self.collidingWithSprites(Ship1)
                if len(collides): 
                    if collides[0].visible:
                        collides[0].explode()
                        self.explode()
                



