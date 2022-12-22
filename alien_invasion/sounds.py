import copy

import pygame.mixer
from pygame import mixer

class Sounds:

    def __init__(self):

        mixer.init()

        self.bg_music = pygame.mixer.music.load('game_music.mp3')
        self.gunfire_sounds = pygame.mixer.Sound("sounds/gunfire.ogg")
        self.alien_hit_sound = pygame.mixer.Sound("sounds/alien_impact.ogg")
        self.alien_offscreen_sound = pygame.mixer.Sound("sounds/break_barrier.ogg")

        pygame.mixer.music.play(-1)

