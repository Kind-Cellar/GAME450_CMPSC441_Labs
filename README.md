# Repository for Labs

## CMPSC 441 and GAME 450

This repository will contain code for all the lab sessions for the course. New folders will be added to 'src' folder with the name of the lab.

## Abstract

This abstract serves as an introduction to a comprehensive report detailing the AI components employed within this game system. The report aims to provide a clear demonstration of all AI components utilized, describing the problems each method solves, detailing their inputs and outputs, and providing a thorough description of each algorithm. The AI components covered include a Genetic Algorithm for city generation, a pre-trained Transformer ChatGPT-2 model for narrative journal generation, and Perlin Noise for dynamic terrain generation. Each component is analyzed in depth to showcase its functionality, integration within the game system. By understanding the role and capabilities of these AI components, developers could effectively leverage them to solve complex problems when developing games or other projects.

### AI/Algorithms Components

1. **Genetic Algorithm**
   * **Problems Solved:**
     * Used to generate a list of city locations based on elevation and the location of cities relative to each other.
   * **Inputs:**
     * Fitness function, number of cities, and size of the map.
   * **Outputs:**
     * List of city locations.
   * **Description:**
     * This Genetic Algorithm incorporates the elevation of randomly generated city locations. It ensures that cities are not placed too low (e.g., in water) or too high (e.g., on a mountain).
   * **Integration:**
     * City locations determined by the genetic algorithm are used to populate the game map, influencing factors such as resource distribution, terrain type, and strategic positioning for gameplay.
   * **Potential Enhancements:**
     * Implementing constraints for diverse city placement, such as proximity to resources or strategic chokepoints.

2. **Pre-trained Transformer ChatGPT-2 (personally implemented)**
   * **Problems Solved:**
     * Generating journal entries with context from recent battles performed by the player.
   * **Inputs:**
     * Contextual information such as game state, player actions, and narrative elements.
   * **Outputs:**
     * AI-generated responses or dialogues tailored to the current game context.
   * **Description:**
     * ChatGPT-2, a pre-trained Transformer-based language model, leverages a large corpus of text data to understand natural language patterns and generate coherent responses.
     * It adapts responses based on context, providing personalized interactions with players.
   * **Integration:**
     * Journal entries are automatically generated after every battle sequence, providing players with a narrative recap of their actions and outcomes.
   * **Potential Enhancements:**
     * Fine-tuning the model on specific gaming datasets to enhance coherence and relevance of generated journal entries.

3. **Perlin Noise**
   * **Problems Solved:**
     * Generating elevations and terrain for the game map.
   * **Inputs:**
     * Size of the game map.
   * **Outputs:**
     * Array of floating-point values representing various elevations.
   * **Description:**
     * Perlin Noise is used to create natural-looking terrains with smooth transitions and realistic features.
   * **Integration:**
     * The generated elevations and terrain influence gameplay mechanics such as movement speed, line of sight, and resource distribution.
   * **Potential Enhancements:**
     * Incorporating additional parameters to generate more diverse terrain features, such as rivers, cliffs, and valleys.


### Appendix
1. Chat GPT 3.5 Prompt - "Can you give me a template for a Problem Solving Rubric in markdown?"
2. Chat GPT 3.5 Prompt - "What AI free package can I use to generate text prompts in Python?"
