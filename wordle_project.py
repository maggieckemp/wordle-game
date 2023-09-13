#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 08:43:56 2022
Wordle Final Project
@author: maggiekemp
"""

import random
from termcolor import colored


def introduction():
    print('Welcome to Wordle!')
    print('This program will give you six attempts to guess a preset 5-letter-word.')
    print('You will be prompted to guess a word in the console.')
    print('Upon guessing a word, the program will return each letter of your guess, colored either green, red, or white.')
    print('If a letter is returned green, the letter is in the word and in the right spot.')
    print('If a letter is returned red, the letter is in the word, but not in the right spot.')
    print('If a letter is returned white, the letter is not in the word.')
    print('When you\'re ready, enter your first guess!')





def random_word(): #choose the wordle word
    words = open('five_letter_words.txt', 'r').read().splitlines() #splits string into a list at the line breaks
    return(str(random.choice(words))).upper() #selects a random word from the list



    

def split(my_word): #used for words with double letters
    return [char for char in my_word]
        
    
    


def game(word):

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for attempt in range(1,7):
        
        guess = str(input('Enter your five-letter guess: ').upper())
        doubles = split(word) #for a word or guess with double letters
        g_doubles = split(guess)
        
       
        if guess != word:   
           
            for i in range(min(len(guess), 5)):
                
                guess_count = g_doubles.count(guess[i])
                word_count = doubles.count(guess[i])
               
                if guess[i] == word[i]:
                    print(colored(guess[i], 'green'), end = ' ')
                    
                      
                    
                elif guess[i] in word and guess[i] != word[i]: 
                    
                    
                    if guess_count <= word_count:
                        print(colored(guess[i], 'yellow'), end = ' ') 
                       
                    
                    if guess_count > word_count:
                        print(guess[i], end = ' ')
                        index_double = g_doubles.index(guess[i])
                        del g_doubles[index_double]
                        g_doubles.insert(index_double, '_')
                        
                    
                else:
                    print(guess[i], end = ' ')
                    
                  
                if guess[i] not in word and guess[i] in alphabet:
                    index = alphabet.index(guess[i])
                    del alphabet[index]
        
            print('\n\nThe letter choices you have remaining are: ', '\n',alphabet)
                            
                
        if guess==word:
            
            print(colored(guess, 'green'))
            print('\nCongrats! You got the wordle in ', attempt, 'tries!')
            break
        
        
        if attempt == 6 and guess != word:
            print('\nBetter luck next time :(')
            print('The word was: ', word)
            
            
            
            
            
def play_again():
    while True:
        
        decision = str(input('Would you like to play again? Type yes or no: ')).lower()
        
        if decision == 'yes':
            word = random_word()
            game(word)
       
        if decision == 'no':
            break
       
        else:
            print('')
       
        
       
        
       
def main():
    introduction()
    word = random_word()
    game(word)
    play_again()
          
main()
