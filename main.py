import time

# The title screen
print("They Forgot (Official Game)")
START = input("Do you wish to play this game? (y/n) ")

if START == "y":
  print("Processing UN...")
  print("Welcome valid user!")
  user = input("Enter your username: ")
  print("Welcome", user)
  time.sleep(3)
  print("...")
  time.sleep(3)
  print("*Your head starts to heal as you wake up from your little coma.")
  time.sleep(2)
  print("*Your senses start to find you..")
  time.sleep(2)
  print("*With the sunlight beaming on your face, you get up.")
  time.sleep(2)
  print("*You analyse your surroundings...")
  time.sleep(3)
  print("*Looks like you are gonna be here a while...")
  time.sleep(3)
  print("*You feel very hungry..")
  time.sleep(3)
  answer = input("Should you look for food? (y/n) ")

  if answer == "y":
    print("*You search the island for trees that contain papayas..")
  elif answer == "n":
    print("*You start to feel faint.")
    time.sleep(2)
    print("*You black out.")
    time.sleep(1)
    print("You feel that you are waking up, but in a different form...")
    time.sleep(3)
    print("...")
    time.sleep(2)
    print("*You hear someone calling you..")
  
else:
  print("Have a good rest of your day!")