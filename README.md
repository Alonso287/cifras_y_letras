# CIFRAS Y LETRAS
#### Video Demo:  https://youtu.be/Xo49F0smHqQ
#### Description:

Cifras y Letras is an Spanish TV show, based on the french show "Des chiffres et des lettres", created by Armand Jammot. 
In each episode, two contestants play a series of games related to numbers and letters, where they earn points. Whoever gets the most points at the end of the episode gets a chance to win a monetary price.

This is a CLI adaptation of the game, where you can play in two modes: Numbers and Letters.

## Numbers mode

In Numbers mode, you will be asked to choose the difficulty, which will determine how many steps, at maximum, will be necessary to use to reach the solution.
Then, you'll be asked to choose how many small numbers (From 1 to 10) you want.

You'll also be asked to choose between the new algorythm and the old one, which only generates a random number, which will make the game much more difficult

After that, the game will start:

You will be given a target number between 100 and 999, and a set of 6 numbers, which can go from 1 to 10, or bigger numbers like 25, 50, 75 or 100.

**The goal of the game is to reach the target number by combining the given numbers through basic arithmetic operations (addition, substracion, multiplication and division).** You must only use positive, integer numbers for your combinations

If you don't reach the target number, you will be shown how close you were to that target number.

## Letters mode

In letters mode, you will be asked to choose how many vocals you want, between 3 and 6.

Then, you'll have the option to play in anagram mode, which means there will always be at least one combination to create a word.

If you don't choose anagram mode, the letter set will be random, which will make the game much more difficult

After that, the game will start:
You will be given a set of 10 letters, and **the goal of the game is to form the longest word possible with those letters**. Obviously, the word must be valid and registered in the spanish dictionary (DLRAE). It should also be 5 letters long or more


## UI

The program has a simple interface, where you can choose between 4 options:
- Play in Numbers mode
- Play in Letters mode
- Consult the rules and how to play
- Exit the program


## Dependencies

The Letters mode module depends on [RAE API](https://rae-api.com/), a free, public, community API to consult the validity of words and its definitions. Half of this project wouldn't have been possible without it, and I must thank them for creating such an amazing tool and making it available to everyone, for free. Half of this wouldn't have been possible without it
___

![[This was developed by a human, not by AI](https://notbyai.fyi/)](Developed-By-a-Human-Not-By-AI-Badge-black.svg)