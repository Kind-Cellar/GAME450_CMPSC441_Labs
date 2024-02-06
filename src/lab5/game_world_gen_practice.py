'''
Lab 5: PCG and Project Lab

This a combined procedural content generation and project lab. 
You will be creating the static components of the game that will be used in the project.
Use the landscape.py file to generate a landscape for the game using perlin noise.
Use the lab 2 cities_n_routes.py file to generate cities and routes for the game.
Draw the landscape, cities and routes on the screen using pygame.draw functions.
Look for triple quotes for instructions on what to do where.
The intention of this lab is to get you familiar with the pygame.draw functions, 
use perlin noise to generate a landscape and more importantly,
build a mindset of writing modular code.
This is the first time you will be creating code that you may use later in the project.
So, please try to write good modular code that you can reuse later.
You can always write non-modular code for the first time and then refactor it later.
'''

import sys
import pygame
import random
import numpy as np
from landscape import get_landscape
from bresenham import bresenham

from pathlib import Path
sys.path.append(str((Path(__file__)/'..'/'..').resolve().absolute()))
from lab2.cities_n_routes import get_randomly_spread_cities, get_routes


# TODO: Demo blittable surface helper function

''' Create helper functions here '''
def drawCities(screen, city_locations_dict):
    ''' draw cities '''
    for city in city_locations_dict:
        val = city_locations_dict[city]
        pygame.draw.rect(screen, (0,0,0), [val[0], val[1], 10,10], 0)

def drawRoutes(screen, routes, city_locations_dict):
    ''' draw first 10 routes '''
    for route in routes:
        firstCity = route[0]
        secondCity = route[1]
        firstCityLocation = city_locations_dict[firstCity]
        secondCityLocation = city_locations_dict[secondCity]
        firstCityX, firstCityY = firstCityLocation[0], firstCityLocation[1]
        secondCityX, secondCityY = secondCityLocation[0], secondCityLocation[1]
        pygame.draw.line(screen, (0,0,0), [firstCityX, firstCityY], [secondCityX, secondCityY], 2)

def createGameSurface(size):
    screen = pygame.display.set_mode(size)
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return screen,pygame_surface

def setupCitiesAndRoutes(size, city_names):
    city_locations = [] 
    routes = []

    city_locations = get_randomly_spread_cities(size, len(city_names))
    routes = get_routes(city_names)
    return city_locations,routes

if __name__ == "__main__":
    pygame.init()
    size = width, height = 640, 480
    black = 1, 1, 1

    screen, pygame_surface = createGameSurface(size) 

    city_names = ['Morkomasto', 'Morathrad', 'Eregailin', 'Corathrad', 'Eregarta',
                  'Numensari', 'Rhunkadi', 'Londathrad', 'Baernlad', 'Forthyr']
    
    city_locations, routes = setupCitiesAndRoutes(size, city_names)

    city_locations_dict = {name: location for name, location in zip(city_names, city_locations)}
    random.shuffle(routes)
    routes = routes[:10] 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(black)
        screen.blit(pygame_surface, (0, 0))

        drawCities(screen, city_locations_dict)
        
        drawRoutes(screen, routes, city_locations_dict)

        pygame.display.flip()
