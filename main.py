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
BuildVersion = "0.1.0 Azucar morena"
CarbonIndexEntries = []

#print("Welcome to HEXAGONO command line fallback, this is not the way it should be used, but anyways")
#Code for the BackEnd goes here
def GetSubjectPicture():
    print("Not functional yet...")
def removeBackground():
    input = Image.open(PicTp)
    output = remove(input)
    output.save("Output.png")
def BackendCarbonRead():
  with open(r"registry\CarbonIndex.txt") as Entries:
    print(Entries)  #UI Code Goes Here    
    PreList = Entries.read()
    print(PreList)
    CarbonIndexEntries = PreList.split()
    print(CarbonIndexEntries)
    if (len(CarbonIndexEntries) - 1 ) > 0:
        for t in range(len(CarbonIndexEntries) - 1):
         print("Here are the entries in the Carbon Editor")
         print(t)
         #Need to add edit function for existing entries
    else:
        print("hmm, no entries yet") 
        print("Should we create an entry to start")
        YesNoCreate = input("1 - yes, 2 - no")
        if YesNoCreate == "1":
            print("Need to add a CarbonEntryCreator() function upstream")
#to be obliterated in milestone 6
class Mainwindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hexagon QDDemo")
        layout3 = QGridLayout()
        self.label = QLabel("Hexagono GUI tool")
        self.label.setFixedSize(100, 30)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        button = QPushButton("Argentum") #, currently pre-milestone 1; the future milestones are \n Milestone 1 - The main menu gets a layout \n Milestone 2 - Carbon is up and running \n Milestone 3 - Multiple File Output support \n Milestone 4 - File selection \n Milestone 5 - Color isolation \n Milestone 6 - Finished UI and graphics")
        #button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked) #Laugh at me following tutorials all ypu want
        button.setFixedSize(QSize(100, 30))
        Button2 = QPushButton("Carbon")
        #Button2.setCheckable(True)
        Button2.clicked.connect(self.Button2_click)
        Button2.setFixedSize(QSize(100, 30))
        Button3 = QPushButton("Cool Stuf for the future")#"Cool Stuf for the future"
        Button3.clicked.connect(self.Button3_click)
        VersionString = QLabel(BuildVersion)
        VersionString.setFixedSize(QSize(140, 30))
        layout3.addWidget(self.label, 0, 2)
        layout3.addWidget(button, 1, 2)
        layout3.addWidget(Button2, 2, 2 )
        layout3.addWidget(Button3, 3, 2)
        layout3.addWidget(VersionString, 4, 2 )
        widget = QWidget()
        widget.setLayout(layout3)
        self.setCentralWidget(widget)
        #self.setCentralWidget(button)
        self.setFixedSize(QSize(1280, 700))
    def the_button_was_clicked(self, checked):
        removeBackground()
        self.w = FileSelectArgentum()
        self.w.show()
    def Button2_click(self, checked):
        BackendCarbonRead()
    def Button3_click(self, checked):
        self.y = FutureCoolStuf()
        self.y.show()

class FileSelectArgentum(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Argentum file select will go here in milestone 4!")
        layout.addWidget(self.label)
        self.setLayout(layout)

class CarbonEntryCreator(QWidget):
    def __init__(self):
        super().__init__()
        layout1 = QVBoxLayout()
        self.label = QLabel("Carbon editor to be up and running in milestone 2!!")
        layout1.addWidget(self.label)
        self.setLayout(layout1)

class FutureCoolStuf(QWidget):
    def __init__(self):
        super().__init__()
        layout4 = QVBoxLayout()
        self.label = QLabel("Milestone 1 - A Menu you can click! - done")
        self.label1 = QLabel("Milestone 2 - Carbon saves files - You are (almost) here")
        self.label2 = QLabel("Milestone 3 - Now this is not just a slipper isolator")        
        self.label3  = QLabel("Milestone 4 - Now you have File selection")
        self.label4  = QLabel("Milestone 5 - Color isolator")
        self.label5 = QLabel("Milestone 6 - Finishing touches for full relase")
        layout4.addWidget(self.label)
        layout4.addWidget(self.label1)
        layout4.addWidget(self.label2)
        layout4.addWidget(self.label3)
        layout4.addWidget(self.label4)
        layout4.addWidget(self.label5)        
        self.setLayout(layout4)
 #, currently pre-milestone 1; the future milestones are \n Milestone 1 - The main menu gets a layout \n Milestone 2 - Carbon is up and running \n Milestone 3 - Multiple File Output support \n Milestone 4 - File selection \n Milestone 5 - Color isolation \n Milestone 6 - Finished UI and graphics")
        
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app= QApplication([])
#Create a window
window = Mainwindows()
window.show()#Show the window (Why hide it tho?)

app.exec()
#Installer = Tk() #Create window for gui boot
#Installer.geometry("1280x720") #Set resolution
#Installer.title("")
#ttk.Label(Installer, text="Wellcome to HEXAGONO setup, this program will guide you through stup for HEXAGONO ").pack(pady=20)
#ttk.Button(Installer, text="Install HEXAGONO", command=print("Hiiii")).pack(pady=20)
#ttk.Button(Installer, text="Quit installer", command=Installer.destroy).pack(pady=20)


#Installer.mainloop()
