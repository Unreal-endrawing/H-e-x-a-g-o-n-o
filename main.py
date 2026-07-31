from tkinter import *
from tkinter import ttk #need to change to pyQt
import runpy
from pathlib import Path
from PIL import Image
import os as os
from rembg import remove

import sys  #For command
import time
import os.path
from PySide6 import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from datetime import datetime
#from PySide6,Q
#TF am i doing
PicTp = "IMG_1309.png"
BuildVersion = "0.1.0b2 Azucar morena"
CarbonIndexEntries = []
NameValue = [] #This list will be flushed repeteadly
BufferChar = "#"
CPD = r"registry\Presets/"
PresetIndex = "Presets.comment"
DummyList = ["Alfa", "Beta", "1", "Omega", "0"]
DummyPresetList = ["AlfaPreset", "1", "0"]
DummyName = "Ingenio"
Extension =".comment"
DummyDate = "01/01/01"
#print("Welcome to HEXAGONO command line fallback, this is not the way it should be used, but anyways")
#Code for the BackEnd goes here
def GetSubjectPicture():
    print("Not functional yet...")

def removeBackground():
    input = Image.open(PicTp)
    output = remove(input)
    output.save("Output.png")

#def setdate(Date):

def BackendCarbonEntryCreator(Date, List, HasPreset, PresetName):
   print("We called the function, hooray")
   if HasPreset == True:
    with open(f"{CPD}{PresetName}{Extension}") as I:
     PreListString = I.read()
     PresetList = PreListString.split(BufferChar)
     PresetList.pop()
     print(PresetList)   
     b = 1
     time.sleep(1)
     print(Date)
     time.sleep(1)
     print(List[b - 1])
     time.sleep(1)
     for b in range(len(List) - 1):
       print("Name from preset")
       time.sleep(1)
       print(PresetList[b - 1])
       time.sleep(1)
       print("Value")
       time.sleep(1)
       print(List[b + 1])
       time.sleep(1)
       return 0
   else:
      b = 1
      print(f"registry/{List[b - 1]}{Extension}")
      f = os.path.isfile(f"registry/{List[b - 1]}{Extension}")
      print(f)
      if f == True:
        print("Whoops, there is already such file")
        return 1
      else:
        with open(f"registry/{List[b - 1]}{Extension}", "a") as s:
         print(s)
         time.sleep(1)
         s.write(Date)
         s.write(BufferChar)
         print(Date)
         time.sleep(1)
         s.write(List[b - 1])
         print(List[b - 1])
         s.write(BufferChar)
         for b in range(len(List) - 1):
          s.write(List[b + 1])
          s.write(BufferChar)
          print(List[b + 1])
         

        return 0

def BackendCarbonPresetIndexMake():
   try:
    with open(f"{CPD}Presets.comment", "w") as p:
      print("writing to file")
      p.write("Null")
      p.write(BufferChar)
      return 0
   except:
      print("file already exists,")

def BackendCarbonPresetMake(Name, List):
   print("Workin' on it")
   print(List)
   presetfile = str(f"{CPD}{Name}.comment")
   indexFile = str(f"{CPD}Presets.comment")
   print(presetfile)
   try:
    with open(presetfile, "w") as r:
       print("the file opened succesfully")
       b = 1
       for b in range(len(List)):
          print("Writing to file")
          r.write(List[b - 1])
          r.write(BufferChar)
       print("The file got written to")
    with open (indexFile, "a") as i:
          print(i)
          print("Adding Preset to index")
          i.write(Name)
          i.write(BufferChar)
          print("Added to database")
    return 0
   except:
     print("Failure")
     return 1     
 
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

def CarbonMidFrontEndPresetMake():
   print("Allrigthy, lets create a new preset")
   print("Give it a super memorable name")
   namePreset = input()
   print("How many values are you gonna track?")
   numb = int(input())
   u = 1
   PreList = []
   for u in range(numb):
      print(f"What is the name of the value nuber {u + 1}?")
      name = input()
      PreList.append(name)
      print(PreList)
   BackendCarbonPresetMake(namePreset, PreList)
   


      
    
def CarbonMidFrontEndShow():
    Entries = BackendCarbonRead()
    print(Entries)
    y = 1
    if Entries > 0:
     #This part is Not finished, you can't edit
     print("Looks like we found some entries")
     while y <= Entries:
        print(CarbonIndexEntries[x])
        print(x)
        y = y + 1
    else:
       print("Looks like you have no entries :()")
       print("Lets Fix that, if you wish")
       Choice = input("1- Make a preset (recommended if you're gonna track large quantities) 2 - Straight to creation")
       if Choice == "1":
          BackendCarbonPresetIndexMake()
          CarbonMidFrontEndPresetMake()
       else:
        print("you do you")
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
#MidFrontEndChoiceModule()
BackendCarbonEntryCreator(DummyDate, DummyList, False, "" )
#Installer = Tk() #Create window for gui boot
#Installer.geometry("1280x720") #Set resolution
#Installer.title("")
#ttk.Label(Installer, text="Wellcome to HEXAGONO setup, this program will guide you through stup for HEXAGONO ").pack(pady=20)
#ttk.Button(Installer, text="Install HEXAGONO", command=print("Hiiii")).pack(pady=20)
#ttk.Button(Installer, text="Quit installer", command=Installer.destroy).pack(pady=20)


#Installer.mainloop()
