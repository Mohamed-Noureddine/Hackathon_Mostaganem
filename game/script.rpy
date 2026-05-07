# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

define p1 = Character("Person 1", color="#c8ffc8", image="person1_image")
define p2 = Character("Person 2", color="#c8c8ff")

image bg cafe = Transform("images/maqha_chaabi.png", size=(config.screen_width, config.screen_height))
image side person1_image = Transform("images/person1_image.png", xalign=0.05, yalign=0.85)


# define p1 = Character("Person 1", color="#c8ffc8")
# define p2 = Character("Person 2", color="#c8c8ff")

# image bg cafe = Transform("images/maqha_chaabi.png", size=(config.screen_width, config.screen_height))

# image person1_sprite = "images/person1_image.png"

# transform custom_left:
#     xalign -0.005
#     yalign 1.0

# The game starts here.

label start:

    # Show the Algerian cafe background
    scene bg cafe with fade

    p1 "I remember it like yesterday."
    p2 "What?"
    p1 "The massacres of the French army."
    p2 "Which year was it?"

    # Step 3: The choice menu (2 wrong, 1 correct)
    menu:
        "1 November 1954":
            p2 "Wasn't that the start of the revolution? No, he's talking about a specific massacre before that."
            jump wrong_answer

        "8 May 1945":
            p2 "Ah, yes. The Sétif, Guelma and Kherrata massacres. A tragic day."
            jump correct_answer

        "5 July 1962":
            p2 "No, that's Independence Day. It happened much earlier."
            jump wrong_answer

# Step 4: Outcomes based on the player's choice
label correct_answer:
    p1 "Exactly. May 8th, 1945. While the world celebrated the end of WWII, our people were massacred."
    # Continue your story here...
    return

label wrong_answer:
    p1 "No, it was May 8th, 1945. A day the world celebrated peace, but we faced bloodshed."
    # Continue your story here...
    return
