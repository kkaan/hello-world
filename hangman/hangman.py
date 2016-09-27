# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 19:41:31 2016

@author: Kankean
"""
from random import *

player_score = 0
computer_score = 0

def hangedman():
    graphic = [
    
    """
      
      /n
      /n
      /n
      /n
      /n
    =============
    """,
    
    """
      +
      |
      |
      |
      |
      |
    =============
    """,
    
    """
      +-------+
      |
      |
      |
      |
      |
    =============
    """,
    
    """
      +-------+
      |      |
      |     ( )
      |
      |
      |
    =============
    """,
    
    """
      +-------+
      |      |
      |      0 
      |     -|-
      |     / \
      |
    =============
    """
        
    ]
    
    print graphic[hangman]

def start():
    print "let's play a windows game of hangman."
    while game():
        pass
    scores()


