import os as os
import shutil
from tkinter import *
from tkinter import ttk
import runpy
global hasruninstaller
hasruninstaller = 0
installerVer = "0.0.0 azucar" #Build number
Guiboot = 1
Main = r"C:\Hexagono" #install goes here
Rawpics = r"C:\Hexagono\import" #Imported pictures as is go here
Pics = r"C:\Hexagono\processed" #Pictures without background go here (Finished or not, not finished get marked for deletion)
Saveflags = r"C:\Hexagono\registry" #Registry of program settings and sujects go here
program = r"C:\Hexagono\Program" #Main.py (argentum and caron go here)
Bc = "#" #Character to separate installer flags
ErrorCodes = ["HEXAGONO is already installed, uninstall it and try again", "Unknown error"]
def errorWindow(Code): #Console and gui error logging
 print("Installer has found an error, with code i-")
 print(Code)
 print(ErrorCodes[Code])
 Error = Tk()
 Error.geometry("500x500")
 Error.title("An error has ocurred, whoops")
 ttk.Label(Error, text="An error has ocurred, with code i-").pack(pady=20)
 ttk.Label(Error, text=Code).pack(pady=20)
 ttk.Label(Error, text=ErrorCodes[Code]).pack(pady=20)
 ttk.Button(Error, text="Quit", command=Error.destroy).pack(pady=20)
 Error.mainloop()
def SuccesWindow():
  Finished = Tk()
  Finished.geometry("500x500")
  Finished.title("Installer is done")
  Label(Finished, text="The installer has succesfully installed HEXAGONO in path ").pack(pady=20)
  Label(Finished, text=Main).pack(pady=20)
  Button(Finished, text="Quit", command=SuccesWindow.destroy).pack(pady=20) #Will figure out auto executing later

  Button(Finished, text="Run hexagono", command=(runpy.run_path(r"C:\Hexagono\Program\main.py" ))).pack(pady=20)
def isFlagsAthingyet():
 global hasruninstaller
 try: 
  with open(r"C:\Hexagono\registry\Installerflags.txt") as Sr: #was temporary, now is permanent :(
   print(Sr.read())
   hasruninstaller = 1
   errorWindow(0)
 except OSError:
  print("proceed")
  InstallHexagono()
 except IOError():
  print("No previous install, proceeding...")
  if hasruninstaller == 1:
   errorWindow(0)
  else:
   print("No errors")
  InstallHexagono()
def InstallHexagono():
 global hasruninstaller
 if hasruninstaller == 0:
      try:
       os.makedirs(Main)
       os.makedirs(Rawpics)
       os.makedirs(Pics)
       os.makedirs(Saveflags)
       os.makedirs(program)
       shutil.copyfile(r"main.py",r"C:\Hexagono\Program\main.py" )
       shutil.copyfile(r"icon.png", r"C:\Hexagono\Program\icon.png")
       shutil.copyfile(r"IMG_1309.png", r"C:\Hexagono\Program\IMG_1309.png")
       hasruninstaller = 1
       inst = str(hasruninstaller)
       save = open(r"C:\Hexagono\registry\Installerflags.txt", "w",) 
       save.write(inst)
       save.write(Bc)
       save.write(installerVer)
       Installer.destroy
       SuccesWindow()
      except:
       print("How r u here")
       shutil.copyfile(r"main.py",r"C:\Hexagono\Program\main.py" )
       shutil.copyfile(r"icon.png", r"C:\Hexagono\Program\icon.png")
       shutil.copyfile(r"IMG_1309.png", r"C:\Hexagono\Program\IMG_1309.png")       
       hasruninstaller = 1
       inst = str(hasruninstaller)
       save = open(r"C:\Hexagono\registry\Installerflags.txt", "w")
       save.write(inst)
       save.write(Bc)
       save.write(installerVer)
       Installer.destroy



 else: 
  print("Error - Installer has been run already (Code i-0)")

if Guiboot == 1:
 Installer = Tk() #Create window for gui boot
 Installer.geometry("1280x720") #Set resolution
 Installer.title("H-E-X-A-G-O-N-O Setup version")

 ttk.Label(Installer, text="Wellcome to HEXAGONO setup, this program will guide you through stup for HEXAGONO ").pack(pady=20)
 ttk.Button(Installer, text="Install HEXAGONO", command=isFlagsAthingyet).pack(pady=20)
 ttk.Button(Installer, text="Quit installer", command=Installer.destroy).pack(pady=20)



Installer.mainloop()