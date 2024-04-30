# Repository for Labs

## CMPSC 441 and GAME 450

This repository will contain code for all the lab sessions for the course. New folders will be added to 'src' folder with the name of the lab.

## Abstract

The report explores the integration of a pre-trained Transformer model, ChatGPT-2, as an AI component in a conversational game. ChatGPT-2 is employed to provide engaging and realistic interactions with players, enhancing the overall gaming experience.

### AI Components

1. **Genetic Algorithm**
   * Problems Solved
   * Inputs
   * Outputs
   * Description
2. **Pre-trained Transformer ChatGPT-2 (personally implemented)**
   * Problems Solved
     * Generating journal entries with context of recent battles performed by the player
   * Inputs
     * Contextual information such as game state, player actions, and narrative elements.
   * Outputs
     * AI-generated responses or dialogues tailored to the current game context.
   * Description
     * ChatGPT-2 is a pre-trained Transformer-based language model developed by OpenAI.
     * It leverages a large corpus of text data to understand natural language patterns and generate coherent responses.
     * The model operates in a sequence-to-sequence manner, where it takes input text and predicts the most likely continuation or response.
     * ChatGPT-2 can handle various conversational topics and adapt its responses based on context, providing personalized interactions with players.
     * The model utilizes self-attention mechanisms to capture long-range dependencies and generate contextually relevant responses.
     * It can be fine-tuned on specific datasets or domains to further enhance its performance and adaptability to the game environment.
   * Integration
     * Journal entries are created after every battle sequence and are accrued.
     * Each journal entry is created with knowing how many rounds happened and the players remaining health.
