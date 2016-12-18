
from random import shuffle

tarot_majors=["0 the fool", "1 the magician", "2 the high priestess", "3 the empress", "4 the emporer", "5 the hierophant",
              "6 the lovers", "7 the chariot", "8 strength", "9 the hermit", "10 the wheel of fortune",
              "11 justice", "12 the hanged man", "13 death", "14 temprance", "15 the devil", "16 the tower",
              "17 the star", "18 the moon", "19 the sun", "20 judgement" , "21 the world"]

tarot_minors=["ace of wands", "two of wands", "three of wands", "four of wands", "five of wands", "six of wands", "seven of wands",
              "eight of wands", "nine of wands", "10 of wands", "page of wands", "jack of wands", "queen of wands", "king of wands",
              "ace of swords", "two of swords", "three of swords", "four of swords", "five of swords", "six of swords", "seven of swords",
              "eight of swords", "nine of swords", "ten of swords", "'page of swords", "jack of swords", "queen of swords", "king of swords",
              "ace of cups", 'two of cups', 'three of cups', 'four of cups', 'five of cups', 'six of cups', 'seven of cups',
              'eight of cups', 'nine of cups', 'ten of cups', 'page of cups', 'knight of cups', 'queen of cups', 'king of cups',
              'ace of pentacles', 'two of pentacles', 'three of pentacles', 'four of pentacles', 'five of pentacles', 'six of pentacles', 'seven of pentacles',
              'eight of pentacles', 'nine of pentacles', 'ten of pentacles', 'page of pentacles', 'jack of pentacles', 'queen of pentacles', 'king of pentacles']

full_deck= tarot_majors + tarot_minors

tarot={}

    
def deck_choice(deck):
    
    if deck=="1" or deck=="majors":
        return tarot_majors
    elif deck=="2" or deck=="minors":
        return tarot_minors
    elif deck =="3" or deck=="full reading":
        return full_deck
    else:
        return deck_choice(input("invalid option, try again:   "))



print("Welcome to your tarot reading")
deck=input("you can have a majors reading, a minors reading, or a full reading. \n Which would you like (1,2,3):    ").lower()
reading=deck_choice(deck)
shuffle(reading)
print(reading[:3])




