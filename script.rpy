﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define alex = Character("Alex")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show alex happy

    # These display lines of dialogue.

    alex "Hello! Are you a new student?"
    alex "Welcome to the International School Lucille Teasdale, the school of many dreams!"
    show alex skibidi
    alex "I promise on skibidi I'll be the best tour guide ever!!! >:3"

    # This ends the game.

    return
