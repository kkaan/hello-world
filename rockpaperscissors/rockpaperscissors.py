# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:45:14 2016

@author: Kankean
"""

import random
import time

rock = 1
paper = 2
scissors = 3

names = { rock: "rock", paper: "paper", scissors: "scissors"}
rules = { rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

def start():
    print "let's play rock paper scissors"
    while game():
        pass
    scores()
    
def game():
    player = move()
    computer = randint(1,3)
    result(player, computer)
    return play_again()

def move():
    while true:
        print
        player = raw_input("Rock = 1\nPaper = 2\nScissors = 3. Make your move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print "I didn't understand that try again nincompoop"
            
def result():
    print "1..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "3..."
    time.sleep(0.5)
    print "computer threw {0}".format(names[computer])
    global player_score, computer_score
    if player == computer:
        print "tie game"
        
    
    
    
    
    

