
import numpy , http , pandas
import datetime as dt

import sys # used for the sys.exit function 
import random 
import time 
from random import * 



print("Welcome to Power Magnet Program")
# start with a welcome to Power Magnet Program page 
# next with a log in page 
# require name and password location and time of login 
print("Log In to the Power Magnet Program")
print("Enter Name, Password, Location & Time: ")
# time for each display 5 seconds 


def name(name):
  pass 

def programming_language(programming_language):
  pass 

def user(user_name):
  pass 

def logged(logged):
  pass 

def password(password):
  pass 

def int_condition(int_condition):
  pass 



PMP = "Help members first"
name = str(input("Whats your name: "))
print('')
print(name +" You are welcome to "+ PMP  )
print('')
welcome_name = print("You are on the Power Magnet Program " + name)
print('')
print("Programming language")
print('')
prog = input("Input Programming language< ")
if prog == "Python":
  print("Python Pogrammer")
else:
  print(prog + "Programmer")



print("User_Name and Password.")
user = input('')
logged_in = True 
if user == name and logged_in:
  print('Admin Page')
else:
  print("Bad creds")  




int_condition = int(input("Enter Interger"))
if int_condition < 6:
  sys.exit("int_condition must be >= 6")
else:
  print("int_condition was >= 6 - continuning")


rock = 1
paper = 2 
scissors = 3

names = { rock: 'Rock', paper:'Paper', scissors:'Scissors' }
rules = { rock: scissors, paper: rock, scissors:paper }

user_score = 0
powermagnetprogram_score = 0 

def start():
  print("The Power Magnet Program Game of Rock, Paper, Scissors.")
  time.sleep(0.5)
  print("Logging in the Power Magnet Program Rock Paper Scissors")
  print('.....................................................')
  time.sleep(0.5)
  print('........................................')
  time.sleep(0.5)
  print('........................')
  time.sleep(0.5)
  print('..................')
  time.sleep(0.5)
  print('............')
  time.sleep(0.5)
  print('...........')
  time.sleep(0.5)
  print('........')
  time.sleep(1)
  while game():
    pass 
  scores()

def game():
  player = move()
  PMP = random.randint(1, 3)
  result(player, PMP )
  return play_again()

def move():
  while True:
    print('')
    print('Input .........................\n1. for Rock \n2. for Paper \n3. for Scissors')
    time.sleep(0.5)
    print("<<<<<PMP TALKS>>> <<<<<<Log in to Power Magnet Program>>>>>>> <<<<<Power Magnet Program>>>>>>>> ")
    print('.............................................')
    time.sleep(0.5)
    print("............................")
    time.sleep(0.4)
    print("..................")
    time.sleep(0.3)
    print("...........")
    time.sleep(0.2)
    print("......")
    time.sleep(0.1)
    print('.....')
    time.sleep(1)
    print('...')
    time.sleep(1)
    player = input("Rock = 1 \nPaper = 2\n Scissors = 3\nMake a move: ")
    time.sleep(0.5)
    print('.........................')
    time.sleep(1)
    print('................')
    time.sleep(0.5)
    print('...........')
    time.sleep(1)
    print('..........')
    time.sleep(0.5)
    print('......')
    try:
      player = int(player)
      if player in (1,2,3):
        return player 
    except ValueError:
      pass 
    print( "Oops!\n I did't  understand that. Please enter 1, 2, 3." )

def result(player, PMP):
  print("1....")
  time.sleep(1)
  print("2....")
  time.sleep(1)
  print("3....")
  time.sleep(0.5)
  print("PMP threw {0}!".format(names[PMP]))
  global user_score, powermagnetprogram_score 
  if player == PMP:
    print("Tie Game")
  else:
    if rules[player] == PMP:
      print("Your victory Has Been assured.")
      user_score += 1
    else:
      print("The PMP laughs as you realise you have been defeated.")
      powermagnetprogram_score += 1

def play_again():
  print("Play Again Enter Yes")
  print(".....................")
  answer = input("Would you like to play again? y/n: ")
  if answer in ("y", "Y", "yes", "Yes", "of course!"):
    return answer 
  else:
    print("Thank you very much for running the Power Magnet Program. see you text time") 

def scores():
  global user_score , powermagnetprogram_score
  print("HIGH SCORES")
  print("Player: ", user_score)
  print("PMP: ", powermagnetprogram_score)

if __name__ == '__main__':
  start()



user_score = 0 
powermagnetprogram_score = 0 

def hangedman(hangman):
  graphic = [
    """
    ..........................
    .............
    ...............
    ..............
    .........
    ......
    .
    ...

    ""","""
    """
  ]

def start():
  print("Let's Play a game of Linux Hangman.")
  while game():
    pass 
  scores()

def game():
  dictionary = ["gnu","kernal","linux","mageia","penguin","ubuntu"]
  word = choice(dictionary)
  word_length = len(word)
  clue = word_length * ['_']
  tries = 6 
  letters_tried = ""
  guesses = 0 
  letters_right = 0 
  letters_wrong = 0 
  global user_score, powermagnetprogram_score
  
  while (letters_wrong != tries) and ("".join(clue) != word):
    letter = guess_letter()
    if len(letter)==1 and letter.isalpha():
      if letters_tried.find(letter) != 1:
        print("You've already Picked", letter)
      else:
        letters_tried = letters_tried + letter
        first_index=word.find(letter)
        if first_index == -1:
          letters_wrong += 1
          print("Congrautaltions,", letter,"is correct.")
          for i in range(word_length):
            if letter == word[i]:
              clue[i] = letter
    else:
      print("Chooice another.")
    
    hangedman(letters_wrong)
    print(" ".join(clue))
    print("Guesses:", letters_tried)

    if letters_wrong == tries:
      print("Game Over.")
      print("The word was", word)
      powermagnetprogram_score += 1
      break 
    if "".join(clue) == word:
      print("You win!")
      print("The word was", word)
      powermagnetprogram_score += 1
      break 
  return play_again()

def guess_letter():
  print("")
  letter = input("Take a guess at our mystry word:")
  letter.strip()
  letter.lower()
  print("")
  return letter

def play_again():
  answer = input("Would You like to play again? y/n: ")
  if answer in ("y", "Y", "yes", "Yes", "YES", "Of course"):
    return answer
  else:
    print("Thank you very much for playing our game. see you next time!")

def scores():
  global user_score, powermagnetprogram_score
  print("HIGH SCORE")
  print("Player: ", user_score)
  print("Computer: ", powermagnetprogram_score)
  

if __name__ == '__main__':
  start()





pick = int(input("Pick a Number> "))
print("add 5 to ", int(pick))
num = int(pick) + 5 
print(num)
nnn = int(num)  * 10
print("Numberer * 10 ")
minune = nnn - pick
print("Number us " + pick) 


try:

  password = input("Enter Password: ")
  if 3 < len(password):
    strong_password = input("Input Strong password 8 and Above ")
except:
  pass 

password_check = input("password input")

  

n = int(input("Input a Number"))

error = "Error Message PMP"

try:
  b = int(input("Enter a Number: "))
except ValueError:
  go = input("Enter go:>>>>>>>>>") 


d = str(input("what your code "))


age = int(input("whats your age: "))
if age < 18 :
  ages = input("Enter Real AGE? ")

section = input("Whats your session: ")




