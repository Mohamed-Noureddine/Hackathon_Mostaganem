

# --- 1. DEFINITIONS (Characters, Images, and Variables) ---

define e = Character("Eileen")
define p1 = Character("Person 1", color="#c8ffc8", image="person1_image")
define p2 = Character("Person 2", color="#c8c8ff")


# Backgrounds
image bg cafe = Transform("images/maqha_chaabi.png", size=(config.screen_width, config.screen_height))
image bg map = Transform("images/bg_map.png", size=(config.screen_width, config.screen_height))
# Base Inventory Image
image inventory_base = Transform("images/inventory_bg_map.png", size=(config.screen_width, config.screen_height))

# Create a style for our number icons to make them clear
style inventory_number is text:
    size 30
    color "#fff"
    outlines [(2, "#000")]
    bold True
    kerning 2

# Text strings for your item descriptions (2-3 lines each)
# define item_2_desc = "Leatherwork: Hand-stitched saddlebags, typical of the Algerian desert tribes, crafted for durability."


define item_1_desc = "Traditional Chaoui Leather Satchel: A hand-stitched leather pouch crafted in the Aurès Mountains by skilled Amazigh artisans. Such satchels were commonly used by travelers, shepherds, and resistance fighters to carry letters, food, and ammunition during the Algerian Revolution."
define item_story_1 = "You receive this satchel from Ahmed, a young messenger of the FLN, after helping his village survive a French military raid in 1956 near the Aurès region. Inside the pouch, hidden beneath the leather lining, lies a folded revolutionary message meant for the mountain resistance."

define item_2_desc = "الحقيبة الجلدية الشاوية التقليدية: جراب جلدي مخيط يدويًا صُنع في جبال الأوراس على يد حرفيين أمازيغ مهرة. كانت هذه الحقائب تُستعمل بكثرة من طرف المسافرين والرعاة ومجاهدي المقاومة لحمل الرسائل والطعام والذخيرة خلال الثورة الجزائرية."
define item_story_2 = "تتحصل على هذه الحقيبة من أحمد، وهو رسول شاب تابع لجبهة التحرير الوطني، بعد مساعدتك لقريته على النجاة من مداهمة عسكرية فرنسية سنة 1956 بالقرب من منطقة الأوراس. داخل الجراب، وتحت البطانة الجلدية المخفية، توجد رسالة ثورية مطوية موجهة إلى مقاومي الجبال."


define item_3_desc = "حقيبة سرج الطوارق: حقيبة سفر متينة تُثبت على ظهور الجمال، استعملتها قوافل الطوارق أثناء عبور الصحراء الكبرى. كان جلدها السميك وتصميمها العملي يحميان المؤونة من حرارة الصحراء والعواصف الرملية."
define item_story_3 = "يهديك هذه الحقيبة دليل قوافل مسن يُدعى موسى سنة 1957 بعد مرافقتك للاجئين عبر الطرق التجارية الجنوبية قرب تمنراست. لا تزال الحقيبة تحمل آثار رمال الصحراء ورائحة الأعشاب الصحراوية التي يستعملها الرحّل."



define item_4_desc = "الزرابي القبائلية المنسوجة: زربية تقليدية منسوجة يدويًا ومزينة برموز أمازيغية هندسية ترمز للحماية والوحدة والإرث العائلي. كانت مثل هذه الزرابي تزين البيوت في مختلف مناطق القبائل وتنتقل بين الأجيال."
define item_story_4 = "تتحصل على هذه الزربية من أرملة مجاهد سقط في المعركة سنة 1958 داخل قرية جبلية قرب تيزي وزو. تطلب منك الاحتفاظ بها تخليدًا لذكرى عائلتها والتضحيات التي قُدمت في سبيل الاستقلال."

define item_5_desc = "سيف النمشة: سيف شمال إفريقي ذو مقبض مميز ونصل أحادي الحد، اشتهر باستعماله من طرف البحارة والمحاربين في مناطق المغرب العربي، خاصة خلال القرنين الثامن عشر والتاسع عشر."
define item_story_5 = "تتحصل على هذا السيف سنة 1957 من بحّار عجوز يُدعى الطاهر في ميناء وهران، بعد مساعدته على تهريب إمدادات سرية للمجاهدين عبر الساحل. يخبرك الرجل أن السيف ورثه عن جده الذي قاوم القراصنة وحمى السفن التجارية الجزائرية في البحر الأبيض المتوسط."

define item_7_desc = "The Nimcha Sword: A distinctively shaped hilt single-edged sword from North Africa, often used by sailors."




# 1. Define variables at the very top of your file (outside any labels or screens)
default item_hover_1 = False
default item_hover_2 = False
default item_hover_4 = False
default item_hover_5 = False
default item_hover_6 = False
default item_hover_7 = False




# 2. The Screen Definition
screen inventory_screen():
    add "inventory_base"

    # --- ITEM 1: 
    imagebutton:
        xpos 185 ypos 455 
        idle Solid("#00000000", xsize=105, ysize=85)
        hover Solid("#ffffff20", xsize=105, ysize=85)
        hovered SetVariable("item_hover_1", True)
        unhovered SetVariable("item_hover_1", False)
        action [SetVariable("current_item_desc", item_1_desc), Show("item_desc_window")]

    # --- ITEM 2: B
    imagebutton:
        xpos 358 ypos 410 
        idle Solid("#00000000", xsize=85, ysize=255)
        hover Solid("#ffffff20", xsize=85, ysize=255)
        hovered SetVariable("item_hover_2", True)
        unhovered SetVariable("item_hover_2", False)
        action [
            SetVariable("current_item_desc", item_2_desc),
            SetVariable("current_item_story", item_story_2),
            Show("item_desc_window")
        ]

    # --- ITEM 4: OUD ---
    imagebutton:
        xpos 570 ypos 525 
        idle Solid("#00000000", xsize=95, ysize=180)
        hover Solid("#ffffff20", xsize=95, ysize=180)
        hovered SetVariable("item_hover_4", True)
        unhovered SetVariable("item_hover_4", False)
        action [
            SetVariable("current_item_desc", item_3_desc),
            SetVariable("current_item_story", item_story_3),
            Show("item_desc_window")
        ]

    # --- ITEM 5: CERAMICS ---
    imagebutton:
        xpos 705 ypos 400 
        idle Solid("#00000000", xsize=120, ysize=180)
        hover Solid("#ffffff20", xsize=120, ysize=180)
        hovered SetVariable("item_hover_5", True)
        unhovered SetVariable("item_hover_5", False)
        action [
            SetVariable("current_item_desc", item_4_desc),
            SetVariable("current_item_story", item_story_4),
            Show("item_desc_window")
        ]

    # --- ITEM 6: ARTIFACT ---
    imagebutton:
        xpos 950 ypos 450 
        idle Solid("#00000000", xsize=140, ysize=220)
        hover Solid("#ffffff20", xsize=140, ysize=220)
        hovered SetVariable("item_hover_6", True)
        unhovered SetVariable("item_hover_6", False)
        action [
            SetVariable("current_item_desc", item_5_desc),
            SetVariable("current_item_story", item_story_5),
            Show("item_desc_window")
        ]

    # --- ITEM 7: JEWELRY ---
    imagebutton:
        xpos 185 ypos 560 
        idle Solid("#00000000", xsize=100, ysize=140)
        hover Solid("#ffffff20", xsize=100, ysize=140)
        hovered SetVariable("item_hover_7", True)
        unhovered SetVariable("item_hover_7", False)
        action [SetVariable("current_item_desc", item_7_desc), Show("item_desc_window")]

    # --- HOVER NUMBERS (Logic inside the screen) ---
    if item_hover_1:
        text "1" xpos 237 ypos 497 style "inventory_number"
    if item_hover_2:
        text "2" xpos 400 ypos 530 style "inventory_number"

    if item_hover_4:
        text "4" xpos 617 ypos 550 style "inventory_number"
    if item_hover_5:
        text "5" xpos 747 ypos 600 style "inventory_number"
    if item_hover_6:
        text "6" xpos 950 ypos 450 style "inventory_number"
    if item_hover_7:
        text "7" xpos 235 ypos 630 style "inventory_number"


    # Return Button
    textbutton _("Return"):
        align (0.95, 0.05)
        action Return()


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





# The Main Inventory Screen
    # Variables to control hover visibility
    # default item_hover_1 = False
    # default item_hover_2 = False
    # # ... add 3, 4, 5, 6 as needed ...


label view_exhibit:
    # First ensure no other description window is open
    $ current_item_desc = ""
    # Call the new screen, hiding the normal dialogue window
    window hide
    call screen inventory_screen
    # When they return, show dialogue again
    window show
    "The artifacts tell a powerful story of Algeria's past..."
    jump continue_story
    
    







