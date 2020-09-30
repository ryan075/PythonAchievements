print("Vul je IGN in.")

naam = input()
print("IGN: " + " " + naam)

print("Leeftijd Character:")
age = input()
print("Dus " + naam +" is " + age)
print('Gender:')
geslacht = input()



from random import randint
speed = randint(15,20)
strength = randint(10,20)
hp = randint(150,350)
Height = randint(150,220)
import random
weapon = ['Sword', 'Spear' ,'Knife','Bow','Fist']
element = ['Fire','Water','Earth','Lightning','Wind']
playstyle = ['Defense','Offense','Passive']
Behaivior = ['Sad','Mad','Happy','Scared','Disgust']
travel = ['Horse','By Feet']

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print('Character Info:')
print(' ')
print('Name ' + naam)
print('Gender ' + geslacht)
print('Age: ' + age)
print('Height: '+ str(Height) +'CM')
print(' ')
print(' ')
print('Game Stats:')
print('HP: ' + str(hp))
print('Element: ' + random.choice(element))
print("Weapon: ", random.choice(weapon))
print('Speed: ' + str(speed))
print('Strength: ' + str(strength))
print('PlayStyle: '+ random.choice(playstyle))
print('Emotions: '+ random.choice(Behaivior))
print('Trasport: '+ random.choice(travel))
