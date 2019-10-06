import pygame, GameObject, Block, importlib
from pytmx.util_pygame import load_pygame


def load_map(path):
    tiled_map = load_pygame(path)
    gameobjects = []

    for layer in tiled_map.layers:
        for obj in layer:
            name = obj.properties['class']
            className = getattr(importlib.import_module(name),name)
            gameobjects.append(className(obj.x, obj.y, obj.image))

    return gameobjects
