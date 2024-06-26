import os
import sys
import pygame
import random
from sprite import Sprite
from pygame_combat import run_pygame_combat
from pygame_human_player import PyGameHumanPlayer
from pygame_ai_player import PyGameAIPlayer
import numpy as np

from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / "..").resolve().absolute()))

script_directory = os.path.dirname(__file__)

from lab2.cities_n_routes import get_routes
from lab7.ga_cities import game_fitness, setup_GA, solution_to_cities
from lab5.landscape import get_landscape, elevation_to_rgba, get_elevation

get_combat_bg = lambda pixel_map: elevation_to_rgba(
    get_elevation(pixel_map), "RdPu"
)

pygame.font.init()
game_font = pygame.font.SysFont("Comic Sans MS", 15)

def get_landscape_surface(size):
    landscape = get_landscape(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def get_combat_surface(size):
    landscape = get_combat_bg(size)
    print("Created a landscape of size", landscape.shape)
    pygame_surface = pygame.surfarray.make_surface(landscape[:, :, :3])
    return pygame_surface


def setup_window(width, height, caption):
    pygame.init()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(caption)
    return window


def displayCityNames(city_locations, city_names):
    for i, name in enumerate(city_names):
        text_surface = game_font.render(str(i) + " " + name, True, (0, 0, 150))
        screen.blit(text_surface, city_locations[i])


class State:
    def __init__(
        self,
        current_city,
        destination_city,
        travelling,
        encounter_event,
        cities,
        routes,
    ):
        self.current_city = current_city
        self.destination_city = destination_city
        self.travelling = travelling
        self.encounter_event = encounter_event
        self.cities = cities
        self.routes = routes


if __name__ == "__main__":
    size = width, height = 640, 480
    black = 1, 1, 1
    start_city = 0
    end_city = 9
    sprite_path = "../../assets/lego.png"
    sprite_speed = 1

    screen = setup_window(width, height, "Game World Gen Practice")

    landscape_surface = get_landscape_surface(size)
    combat_surface = get_combat_surface(size)
    city_names = [
        "Morkomasto",
        "Morathrad",
        "Eregailin",
        "Corathrad",
        "Eregarta",
        "Numensari",
        "Rhunkadi",
        "Londathrad",
        "Baernlad",
        "Forthyr",
    ]

    elevation = get_elevation(size)
    elevation = np.array(elevation)
    elevation = (elevation - elevation.min()) / (elevation.max() - elevation.min())
    fitness = lambda solution, idx: game_fitness(
        solution, idx, elevation=elevation, size=size
    )

    # Incorporation of GA 
    fitness_function, ga_instance = setup_GA(fitness, len(city_names), size)

    # Show one of the initial solutions.
    random_solution = ga_instance.initial_population[0]
    cities = solution_to_cities(random_solution, size)

    # Run the GA to optimize the parameters of the function.
    ga_instance.run()
    best_solution = ga_instance.best_solution()[0]

    #city_locations = get_randomly_spread_cities(size, len(city_names))
    city_locations = solution_to_cities(best_solution, size)
    routes = get_routes(city_locations)

    random.shuffle(routes)
    routes = routes[:10]

    player_sprite = Sprite(sprite_path, city_locations[start_city])

    player = PyGameHumanPlayer()

    """ Add a line below that will reset the player variable to 
    a new object of PyGameAIPlayer class."""

    state = State(
        current_city=start_city,
        destination_city=start_city,
        travelling=False,
        encounter_event=False,
        cities=city_locations,
        routes=routes,
    )

    journalEntries = []
    destination = city_locations[state.destination_city]

    while True:
        action = player.selectAction(state)
        if 0 <= int(chr(action)) <= 9:
            if int(chr(action)) != state.current_city and not state.travelling:

                destination_city = int(chr(action))
                if routes[state.current_city][destination_city] is not None:
                    # Route exists
                    state.destination_city = destination_city
                    player_sprite.set_location(city_locations[state.current_city])
                    state.travelling = True
                    print("Travelling from", state.current_city, "to", state.destination_city)
                else:
                    # Route does not exist
                    print("No route exists between", state.current_city, "and", destination_city)

        screen.fill(black)
        screen.blit(landscape_surface, (0, 0))

        for city in city_locations:
            pygame.draw.circle(screen, (255, 0, 0), city, 5)

        for line in routes:
            pygame.draw.line(screen, (255, 0, 0), *line)

        displayCityNames(city_locations, city_names)
        if state.travelling:
            state.travelling = player_sprite.move_sprite(destination, sprite_speed)
            state.encounter_event = random.randint(0, 1000) < 2
            if not state.travelling:
                print('Arrived at', state.destination_city)

        if not state.travelling:
            encounter_event = False
            state.current_city = state.destination_city

        if state.encounter_event:
            journalEntry = run_pygame_combat(combat_surface, screen, player_sprite)
            state.encounter_event = False
            journalEntries.append(journalEntry)
        else:
            player_sprite.draw_sprite(screen)
        pygame.display.update()
        if state.current_city == end_city:
            print('You have reached the end of the game!')
            break
