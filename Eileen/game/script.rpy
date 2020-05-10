# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the

# name of the character.

define e = Character("Eileen")
define m = Character ('Mother', color = "#C5A3FF") 

# The game starts here.

label start:
    stop music 
    
    play music "sakura.mp3"
    
    scene black
    
    # This shows a character sprite. A placeholder is used, but you can
    
    # replace it by adding a file named "eileen happy.png" to the images
    
    # directory.
    
    e "hello?? Anyone there?" 
    
    image eileen neutral = "Eileen2.png"

    image mum angy = "mum2.png"
    
    image lights = "lights.png" 
    
    image cute dog = "cutedog.png"
    
    image faker = "faker.png" 
    
    image bread = "bread.png" 
    
    show lights at top
    
    show eileen neutral at left 

    e "oh hi there! I'm sorry I didn't see you earlier" 
    
    e "I know  I shouldn't break the third wall.  But here I am! Eileen. Please to meet you!"
    
    e "lemme show you my mum's weapons of choice." 
    
    e "First off, we have..." 
    
    hide lights 
    
    e "Slippers!!" 
    
    image slippers = "slippers.png" 
    
    show slippers 
    
    e "very efficient, can be found anywhere in this Asian household. Can do job of smacking me in a timely manner"
    
    hide slippers 
    
    e "then we have..." 
    
    e "spatula!" 
    
    image spatula = "spatula.png" 
    
    show spatula 
    
    e "hits the spot just right *cringes*" 
    
    hide spatula 
    
    e "I guess some things never change" 
    
    e "anywho, this is story time of my Asian mum" 
    
    e "so I grew up in a kind of sketchy neighbourhood" 
    
    e "one day she was like yo listen up here ya little piece of poop..."
    
    e "...there are people following us, so we have to be extra cautious" 
    
    e "at that time, I was like oh okay, but of course I also didn't know what anxiety was at that time"
 
    e "I'm sure many of you can relate to this next one" 
    
    e "once she was walking me back from school back when I was like 8 or 9" 
    
    e "she told me that if there is a car parked there, go to the opposite side of the road" 
    
    e "I mean, that is kind of logical. But this is literally the reason of my anxiety today..."
    
    e "...at 21 years old"
    
    e "I also think my mum lowkey has a problem with saran wraps" 
    
    image plasticwrap = "plasticwrap.png" 
    
    e "everything is saran wrapped in my house" 
    
    show plasticwrap at topright 
    
    e "I mean I wouldn't have a problem with it if she didn't use a crap ton of rolls on the sofa."
    
    
    e "honestly, the saran wrap keeps me chills and nightmare at times almost as if it is haunting me" 
    
    e "gotta keep em dust free ya know?" 
    
    hide plasticwrap at topleft
    
    hide plasticwrap at truecenter
    
    hide plasticwrap at topright 
    
    hide plasticwrap at center
    
    m "are you talking **** about me again?"
    
    show mum angy at right
    
    e "no of course not!" 
    
    e "But hi guys! this is my mum I love her dearly but less than my pupper" 
    
    show cute dog 
    
    m "I still think his breath smelly" 
    
    hide cute dog 
    
    e "shush, I'm being observed ma" 
    
    m "okay how about I observe you washing dishes???????"
    
    e "in a bit please...?"
    
    m "look at this child, talking back to me already la, no manners la, raise 21 years for no good ah"
    
    e "..." 
    
    m "..." 
    
    e "ma, can I-"
    
    m "no"
    
    e "but ma, Cha-" 
    
    m "no."
    
    e "hey look at this tiktok I found, isn't it hilarious?" 
    
    m "look at that girl, dress so clean, hair combed nicely ah, this is why you no have boyfriend la!"
    
    e "but I just wanted to show you the person... not a lecture" 
    
    m "just go play with that guy in League of Legends, what's his name again...? Right, Baker"
   
    show faker
    
    e "no ma, it's Faker... " 
   
    hide faker
    
    show bread
    
    m "not baker?" 
    
    hide bread 
    
    show faker
    
    e "faker."
    
    hide faker
    
    show bread
    
    m "baker?"
    
    hide bread
    
    show faker
  
    e "no, Faker" 
    
    hide faker  
    
    show bread
    
    m "I am saying Baker la!!"
    
    hide bread 
    
    e "say it with me: fay-"
    
    m "fay" 
    
    e "ker"
    
    m "ker"
    
    e "Faker! :D " 
    
    show faker 
    
    m "Baker :D "
    
    hide faker 
    
    show bread
    
    e "..." 
    
    hide Eileen neutral
 
