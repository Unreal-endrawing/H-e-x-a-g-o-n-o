import os as os
import shutil
from tkinter import *
from tkinter import ttk
import runpy
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6 import QtCore, QtGui
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QGridLayout,
    QWidget,
)
import sys  #For command
import PyQt6
global hasruninstaller
hasruninstaller = 0
installerVer = "1.0.0b1 cañaveral" #Build number
Guiboot = 1
Main = r"C:\Hexagono" #install goes here
Rawpics = r"C:\Hexagono\import" #Imported pictures as is go here
Pics = r"C:\Hexagono\processed" #Pictures without background go here (Finished or not, not finished get marked for deletion)
Saveflags = r"C:\Hexagono\registry" #Registry of program settings and sujects go here
program = r"C:\Hexagono\Program" #Main.py (argentum and caron go here)
Bc = "#" #Character to separate installer flags
ErrorCodes = ["HEXAGONO is already installed, uninstall it and try again", "Unknown error", "The installer is abandoned, it will be remade from scratch soon, maybe even MSI! stay patient"]
class ModernErrorWindow(QWidget,):
  def __init__(self, Code):
   super().__init__()
   strCd = str(Code)
   layout = QVBoxLayout()
   self.setWindowTitle("An error has ocurred, whoops")
   Label = QLabel("An error has ocurred, with code i-")
   label2 = QLabel(strCd)
   label3 = QLabel(ErrorCodes[Code])
   returnB = QPushButton("Ok")
   returnB.clicked.connect(self.close)
   layout.addWidget(Label)
   layout.addWidget(label2)
   layout.addWidget(label3)
   self.setLayout(layout)

def modernError(Mode, self, checked):
  self.a = ModernErrorWindow(Mode)
  self.a.show()

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
  Button(Finished, text="Quit", command=Finished.destroy).pack(pady=20) #Will figure out auto executing later
  Finished.mainloop()
#  Button(Finished, text="Run hexagono", command=(runpy.run_path(r"C:\Hexagono\Program\main.py" ))).pack(pady=20)
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

def ModernIsflagsAthingyet():
  global hasruninstaller
  try: 
    with open(r"C:\Hexagono\registry\Installerflags.txt") as Sr: #was temporary, now is permanent :(
     print(Sr.read())
     hasruninstaller = 1
     modernError(0)
  except OSError:
     print("proceed")
     InstallHexagono()
  except IOError:
    print("No previous install, proceeding...")
  if hasruninstaller == 1:
   ModernErrorWindow(0)
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
       #os.makedirs(program)
       shutil.copyfile(r"main.py",r"C:\Hexagono\main.py" )
       shutil.copyfile(r"icon.png", r"C:\Hexagono\icon.png")
       shutil.copyfile(r"IMG_1309.png", r"C:\Hexagono\IMG_1309.png")
       hasruninstaller = 1
       inst = str(hasruninstaller)
       save = open(r"C:\Hexagono\registry\Installerflags.txt", "w",) 
       save.write(inst)
       save.write(Bc)
       save.write(installerVer)
       carbon = open(r"C:\Hexagono\registry\CarbonIndex.txt", "w",)
       carbon.write("0")
#       Installer.destroy
       SuccesWindow()
      except:
       print("How r u here")
       os.makedirs(Main, exist_ok=True)
       os.makedirs(Rawpics)
       os.makedirs(Pics)
       os.makedirs(Saveflags)       
       shutil.copyfile(r"main.py",r"C:\Hexagono\main.py" )
       shutil.copyfile(r"icon.png", r"C:\Hexagono\icon.png")
       shutil.copyfile(r"IMG_1309.png", r"C:\Hexagono\IMG_1309.png")       
       hasruninstaller = 1
       inst = str(hasruninstaller)
       save = open(r"C:\Hexagono\registry\Installerflags.txt", "w")
       save.write(inst)
       save.write(Bc)
       save.write(installerVer)
       carbon = open(r"C:\Hexagono\registry\CarbonIndex.txt", "w",)
       carbon.write("0")
       SuccesWindow()
 #      Installer.destroy



 else: 
  print("Error - Installer has been run already (Code i-0)")



#You can enable the legacy installer if you must, but its broken




class InstallerWindow(QMainWindow):
  def __init__(self):
   super().__init__()
   self.setWindowTitle("Hexagono Setup - obsolete")
   layout1 = QVBoxLayout()
   self.obsolete = QLabel("This program is obsolete and no longer updated, it was just a test; to be rebuilt later")
   self.obsolete2 = QLabel("This doesn't support installing anywhere else than c:Hexagono, please download standalone for custom paths")
   self.label = QLabel("Wellcome to HEXAGONO setup, this program will guide you through stup for HEXAGONO ")
   Install = QPushButton("Install Hexagono")
   Install.clicked.connect(isFlagsAthingyet)
   Quit = QPushButton("Quit installer")
   Quit.clicked.connect(self.close)
   About = QPushButton("About installer")
   About.clicked.connect(self.OpenAbout)
   test = QPushButton("Test super secret stuff...")
   test.clicked.connect(self.TestingWindowOpen)
   layout1.addWidget(self.obsolete)
   layout1.addWidget(self.obsolete2)
   layout1.addWidget(self.label)
   layout1.addWidget(Install)
   layout1.addWidget(Quit)
   layout1.addWidget(About)
   layout1.addWidget(test)
   self.setLayout(layout1)
   widget = QWidget()
   widget.setLayout(layout1)
   self.setCentralWidget(widget)
  def OpenAbout(self, checked):
   self.w = AboutInstaller()
   self.w.show()
  def TestingWindowOpen(self, checked):
   self.y = ModernErrorWindow(2)
   self.y.show()

   

class AboutInstaller(QWidget):
 def __init__(self):
  super().__init__()
  layout = QVBoxLayout()
  self.setWindowTitle("About installer")
  self.label = QLabel(installerVer)
  Legacy = QPushButton("Open Legacy Installer (Not recommended)")
  Legacy.clicked.connect(self.LegacyMenu)
  layout.addWidget(self.label)
  layout.addWidget(Legacy)
  self.setLayout(layout)
 def LegacyMenu(tkinter):
  Installer = Tk() #Create window for gui boot
  Installer.geometry("1280x720") #Set resolution
  Installer.title("H-E-X-A-G-O-N-O Setup version")

  ttk.Label(Installer, text="Wellcome to HEXAGONO setup, this program will guide you through stup for HEXAGONO ").pack(pady=20)
  ttk.Label(Installer, text="Don't use me please, i was legacy before relase; the modern (PyQt) installer should not break anything").pack(pady=20)
  ttk.Button(Installer, text="Install HEXAGONO", command=isFlagsAthingyet).pack(pady=20)
  ttk.Button(Installer, text="Quit installer", command=Installer.destroy).pack(pady=20)

  Installer.mainloop()



app = QApplication([])
window = InstallerWindow()
window.show()

sys.exit(app.exec())



