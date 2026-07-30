from tkinter import *
from tkinter import ttk #need to change to pyQt
import runpy
from pathlib import Path
from PIL import Image
import os as os
from rembg import remove

import sys  #For command

from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
#from PySide6,Q
#TF am i doing
PicTp = "IMG_1309.png"
BuildVersion = "0.1.0b2 Azucar morena"
CarbonIndexEntries = []
NameValue = [] #This list will be flushed repeteadly

#print("Welcome to HEXAGONO command line fallback, this is not the way it should be used, but anyways")
#Code for the BackEnd goes here
def GetSubjectPicture():
    print("Not functional yet...")

def removeBackground():
    input = Image.open(PicTp)
    output = remove(input)
    output.save("Output.png")

def BackendCarbonEntryCreator(List):
   print("We called the function, hooray")
    



def BackendCarbonRead():
  with open(r"registry\CarbonIndex.txt") as Entries:
    print(Entries)  #UI Code Goes Here    
    PreList = Entries.read()
    print(PreList)
    global CarbonIndexEntries
    CarbonIndexEntries = PreList.split("#")
    print(CarbonIndexEntries)
    if (len(CarbonIndexEntries) - 1 ) > 0: #Reserve first
         return (len(CarbonIndexEntries) - 1)
    else:
         return 0
#to be obliterated in milestone 6
#Welcome to the weird mid-front end, it will be here until Milestone 6
def CarbonMidFrontEndCreate():
    print("Let's start the writing")
    print("What will you name your subject?")
    Name = input()
    print(Name, ", I like it")
    print("How many values will you track?")
    Vtotrack = int(input())
    a = 1
    global NameValue
    for a in range(Vtotrack):
       print("what shall this thing to track be called?")
       Value1 = input()
       NameValue.append(Value1)
       print("What is its value?")
       Value2 = float(input())
       print(Value2)
       NameValue.append(Value2)
       print("Just wait for the backend to be made")
       BackendCarbonEntryCreator(NameValue)
       NameValue = [] #Flush the value to prevent corrupt writings
    
def CarbonMidFrontEndShow():
    Entries = BackendCarbonRead()
    print(Entries)
    x = 1
    if Entries > 0:
     #This part is Not finished, you can't edit
     print("Looks like we found some entries")
     while x <= Entries:
        print(CarbonIndexEntries[x])
        print(x)
        x = x + 1
    else:
       print("Looks like you have no entries :()")
       print("Lets Fix that, if you wish")
       CarbonMidFrontEndCreate()

def MidFrontEndChoiceModule():
   print("Choose what module to load")
   choose = int(input("1 - Carbon, 2 - Argentum"))
   if choose  == 1:
      BackendCarbonRead()
      CarbonMidFrontEndShow()



print("Welcome to command line hexagono")
print("You're in build...")
print(BuildVersion)
print("this will be the front-end for now")
print("I don't want a backend tangled with the front")
print("It just kills programs, ask the installer")
MidFrontEndChoiceModule()

#Installer = Tk() #Create window for gui boot
#Installer.geometry("1280x720") #Set resolution
#Installer.title("")
#ttk.Label(Installer, text="Wellcome to HEXAGONO setup, this program will guide you through stup for HEXAGONO ").pack(pady=20)
#ttk.Button(Installer, text="Install HEXAGONO", command=print("Hiiii")).pack(pady=20)
#ttk.Button(Installer, text="Quit installer", command=Installer.destroy).pack(pady=20)


#Installer.mainloop()
