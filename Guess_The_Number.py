# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 16:35:04 2021

@author: Karnas
"""
from random import randint as rd
def computer_num(mini,maxi):
    return rd(mini,maxi)
def player_number(mini,maxi):
    print(f"guess the number from {mini} to {maxi}")
    player_num=int(input())
    return player_num
def play():
    print(f"enter the minimum and maximum limit of numbers inorder to play")
    mini=int(input("minimum number"))
    maxi=int(input("maximum number"))
    chances=1
    computer_value=computer_num(mini,maxi)
    player_value=player_number(mini,maxi)
    while(computer_value!=player_value):
        if(player_value<mini and player_value>maxi):
            print(f"YOU GUESSED IT OUT OF LIMIT ,,,SO PLEASE MAKE SURE TO GUESS IN LIMIT")
        if(computer_value<player_value):
            print(f"YOU GUESSED LARGER VALUE SO GUESS SOME SMALL VALUE")
        else:
            print(f"YOU GUESSED SMALLER VALUE SO GUESS SOME LARGE VALUE")
        player_value=player_number(mini,maxi)
        chances=chances+1
    print(f"WOHOOOOO YOU GOT IT RIGHT\n  U GUESSED IT RIGHT \n YOU TOOK {chances} TO FIND THIS NUMBER !!! \n***********   THAT'S AMAZING   ***********")
play()