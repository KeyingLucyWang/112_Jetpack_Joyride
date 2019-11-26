import pygame
import math
from gameObject import GameObject

class Monsters(GameObject):
    @staticmethod
    def init():
        Monsters.sprite = []
