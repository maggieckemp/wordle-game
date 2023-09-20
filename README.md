# wordle-game
A Python project I made for a computer science class in my undergrad.  It currently runs and is interactive in the console.  My next steps are to have it pop up in its own interactive window.
The output of the code will look like this in the console:
![Screen Shot 2023-09-13 at 3 55 44 PM](https://github.com/maggieckemp/wordle-game/assets/102002464/7b19bdbf-e49b-4c46-a642-fe9ec9daa0b3)

# Wordle Game Project

## Project Overview

For my final project, I undertook the task of recreating the popular word puzzle game known as 'Wordle,' as featured in The New York Times. Wordle is a daily online game where players attempt to guess a 5-letter target word in just 6 tries. After each guess, players receive feedback in the form of colored letters: green for correct letters in the correct position and yellow for correct letters in the incorrect position.

## Project Implementation

To create my version of Wordle, I utilized Python and two key packages: `Random` and `Termcolor`.

- **Random Package**: I employed the `Random` package to select a random word from a predefined list, setting it as the target word for each game. The `random_choice` function was instrumental in this process, as it returns a randomly selected element from a sequence.

- **Termcolor Package**: For enhancing the user experience, I used the `Termcolor` package to apply colors (green and yellow) to letters in the user's guess. This was accomplished by incorporating the `colored(text, color)` function within the `print()` function to display colored letters in the console.

## Addressing Challenges

During the development process, I encountered challenges related to ensuring the fairness and accuracy of the game. Specifically, I had to address the issue of words with double letters, as they were not handled correctly in the initial code I found.

I initially attempted to avoid words with double letters by checking and rerolling the target word at the start of each game and for each user guess. However, this approach severely limited the available word choices and deviated from the true Wordle experience. I decided to revise my approach.

I introduced a function called `split()`, which separated the Wordle word and the user's guessed word into two lists containing individual letters. I used the `double` list to represent the ordered letters in the Wordle word and `g_double` for the user's guessed word. This enabled a more precise comparison between the two words.

Within a loop iterating over each letter in the guessed word, I counted the occurrences of that letter in both the guessed word (`guess_count`) and the Wordle word (`word_count`). I then used these counts to accurately color letters yellow when they were in the Wordle word, while preserving the integrity of the game by accounting for double letters.

## Key Takeaways

This project provided valuable insights into problem-solving in programming, demonstrating the need to adapt and refine solutions as challenges arise. It deepened my understanding of nested loops, a concept briefly covered in class, and introduced me to new Python packages not previously explored.

Overall, this project expanded my programming skills, especially in developing larger, more complex programs. For future projects, I plan to incorporate flowchart diagrams as a visual aid to plan and understand the program's structure more effectively. 

## References

The initial inspiration for this project came from this YouTube tutorial, which served as a foundation for my work: https://youtu.be/NCgN4qtbh2Q 
I got the file with 5-letter words from here: https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt 
