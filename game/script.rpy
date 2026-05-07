# --- 1. DEFINITIONS (Characters, Images, and Variables) ---

define e = Character("Eileen")
define p1 = Character("Person 1", color="#c8ffc8", image="person1_image")
define p2 = Character("Person 2", color="#c8c8ff")


# Backgrounds
image bg cafe = Transform("images/maqha_chaabi.png", size=(config.screen_width, config.screen_height))
image bg map = Transform("images/bg_map.png", size=(config.screen_width, config.screen_height))

# Side Image for Person 1
image side person1_image = Transform("images/person1_image.png", xalign=0.05, yalign=0.85)

# Game State Variable
default oran_unlocked = False

# --- 2. THE INTERACTIVE MAP SCREEN ---

screen algeria_map():
    add "bg map"

    text "SELECT A CITY TO WITNESS THE TRAGEDY" xalign 0.5 yalign 0.05 size 30 color "#fff" outlines [(2, "#000")]

    # Sétif Button
    imagebutton:
        xpos 850 ypos 320
        idle "images/marker.png"
        hover "images/marker_hover.png"
        hovered Notify("Sétif: May 8, 1945")
        unhovered Hide("notify")
        action Jump("setif_mission")

    # Oran Button (Locked)
    if oran_unlocked:
        imagebutton:
            xpos 400 ypos 400
            idle "images/marker_oran.png"
            hover "images/marker_oran_hover.png"
            action Jump("oran_mission")
    else:
        imagebutton:
            xpos 400 ypos 400
            idle "images/marker_locked.png" # Create a grayed-out marker image
            action Notify("Oran is currently locked.")

# --- 3. THE GAME START ---

label start:
    scene bg cafe with fade

    p1 "I remember it like yesterday."
    p2 "What?"
    p1 "The massacres of the French army."
    p2 "Which year was it?"

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

# --- 4. OUTCOMES & TRANSITION TO MAP ---

label correct_answer:
    p1 "Exactly. May 8th, 1945. While the world celebrated the end of WWII, our people were massacred."
    p1 "Let us look at the regions affected."
    jump open_map # Send them to the map

label wrong_answer:
    p1 "No, it was May 8th, 1945. A day the world celebrated peace, but we faced bloodshed."
    p1 "Look closely at the map; this is where the history was written."
    jump open_map # Send them to the map

label open_map:
    window hide # Hide the textbox so the map is clear
    call screen algeria_map
    return

# --- 5. MISSION LABELS ---

label setif_mission:
    window show
    "The mission in Sétif begins..."
    # Add your mission 1 code here
    return

label oran_mission:
    window show
    "The mission in Oran begins..."
    # Add your mission 2 code here






screen inventory_screen():
    tag menu
    add Transform("images/inventory_bg_map.png", size=(config.screen_width, config.screen_height))

    vbox:
        align (0.5, 0.4)
        spacing 20
        text "INVENTORY" size 60 color "#fff" xalign 0.5
        
        # This is just a placeholder text
        text "Items collected from Sétif will appear here." size 22 xalign 0.5

    textbutton _("Return"):
        align (0.1, 0.9) # Bottom left
        action Return()





