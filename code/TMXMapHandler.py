import pygame, GameObject, Block, importlib
from pytmx.util_pygame import load_pygame


def load_map(path): # loads  tmx tile map
    tiled_map = load_pygame(path)
    gameobjects = []

    for layer in tiled_map.layers: # iterates through all layers of the tile map
        for x, y, image in layer.tiles(): # iterates through ttiles in layer
            name = layer.name
            className = getattr(importlib.import_module(name),name) # assigns variable classname with the atributes of the layer
            gameobjects.append(className(x*tiled_map.tilewidth, y*tiled_map.tileheight, image)) #generates game objects 

    return gameobjects
