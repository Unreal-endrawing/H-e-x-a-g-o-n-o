#Things that are currently missing in the image isolation (UTMOST PRIORITY):
#DO NOT REMOVE UNTIL FIXED/DONE
#-Make selection does nothing (you have the code, you just need to make the button work propperly)
#-Make sure selection is from isolated subject if that's enabled and from the regular picture otherwise
#-Select from image(Tutorial is on geeksforgeeks tab on Eliza fernanda's profile)
#-No save button
#-Association to carbon entry
#-DATES

#Overall missing stuff (In priority order)
#-Carbon Backend:
# - adding entry to subject
# - Delete subject
# - read data from subject.comment file
# - read data from preset
#-Carbon GUI
#-Create subject, create entry, create preset, read data from preset and subject.comment, delete files
#Settings tab
#Welcome tab


from pathlib import Path
from PIL import Image, ImageTk, ImageColor
import os
from rembg import remove
import customtkinter as ctk
from CTkColorPicker import *
import sys  #For command
import time
import os.path
import pathlib
from datetime import datetime
from customtkinter import filedialog
#from PySide6,Q
#TF am i doing
PicTp = "IMG_1309.png"
BuildVersion = "0.1.0b2 Azucar morena"
CarbonIndexEntries = []
NameValue = [] #This list will be flushed repeteadly
BufferChar = "#" #For storing ultiple values in a file and so split(#) can be used 
CPD = r"registry\Presets/"
PresetIndex = "Presets.comment"
DummyList = ["Delta", "Beta", "1", "Omega", "0"]
DummyPresetList = ["AlfaPreset", "1", "0"]
DummyName = "Ingenio"
Extension =".comment"
DummyDate = "01-06-19"
DummyPic = Image.open("Art/No Picture Found.png")
DummyPicTest = fr"Art/No.png"
ModeBeingRefined = ["Automatic (not recommended if your subject is not monochrome), just isolating the subject", "Mixed, isolate and then colors", "Just isolate colors"]
TODO = ["Selecting, viewing and editing carbon entries", "Argentum", "Gui"]
#print("Welcome to HEXAGONO command line fallback, this is not the way it should be used, but anyways")
#Code for the BackEnd goes here
#Finally time for argentum, woo-hoo
def notImplemented():
   raise Exception("Error -9,223,372,036,854,775,807, I said NOT IMPLEMENTED")
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File",filetypes = (("Image Files", "*.png *.jpeg *.heic *.avif *.webp"),("all files","*.*")))
    print(filename)
    return filename

def ArgentumManager():
   print ("Love")
def BackendGetSubjectPicture():
    print("Not functional yet...")

def BackEndremoveBackground(file, Date, Subject, Istemp): #AsociatedEntry):
    input = Image.open(file)
    output = remove(input)
    if os.path.isdir(f"processed/{Subject}") == True:
       pass
    else:
       os.makedirs(f"processed/{Subject}")
    if Istemp == False:
     output.save(f"processed/{Subject}/Output{BufferChar}{Date}.png")
     return (f"processed/{Subject}/Output{BufferChar}{Date}.png") 
    else:
     if os.path.isdir(f"processed/{Subject}/Temp") == False:
        os.makedirs(f"processed/{Subject}/Temp")
     output.save(f"processed/{Subject}/Temp/Output{BufferChar}{Date}{BufferChar}Temp.png")      
     return (f"processed/{Subject}/Temp/Output{BufferChar}{Date}{BufferChar}Temp.png") 

def BackendGetImageSize(Path):
   ItoMeasure = Image.open(Path)
   print(ItoMeasure.size)
   PreMeasure = ItoMeasure.size
   print(PreMeasure)
   Measure = list(PreMeasure)
   print(Measure)
   return Measure

def ReadEntry(Subject, date):
   with open(f"registry/{Subject}/{Subject}{BufferChar}{date}{Extension}") as r:
      print("TODO")

def BackEndCarbonListAllEntries(Subject):
   PreAll = os.listdir(f"registry/{Subject}")
   PreAll2 = []
   PreAll3 = []
   All = []
   for u in range(len(PreAll)):
    var = PreAll[u]
    print(var)
    var2 = pathlib.PurePath(var).stem
    print(var2)
    PreAll2.append(var2)
    print(PreAll2)
    var3 = PreAll2[u]
    print(var3)
    var4 = str(var3)
    PreAll3 = var4.split(BufferChar)
    print(PreAll3)
    All.append(PreAll3[1])
   print(All)
   return All
#def setdate(Date):
#Any print statements were just for debugging purposes during the function development
def BackendCarbonEntryCreator(Date, List, HasPreset, PresetName):
   print("We called the function, hooray")
   if HasPreset == True: #First two values reserved for just this
    with open(f"{CPD}{PresetName}{Extension}") as I:
     PreListString = I.read()
     PresetList = PreListString.split(BufferChar)
     PresetList.pop()
     print(PresetList)   
     b = 1
     u = os.path.isdir(f"registry/{List[0]}/")
     print(u)
     if u == False:
        print("We first need to make the directory silly")
        os.makedirs(f"registry/{List[0]}")
     f = os.path.isfile(f"registry/{List[0]}/{List[0]}{BufferChar}{Date}{Extension}")
     if f == True:
      print("Whoops, such a file is already a thing")
      return 1
     else:
      with open(f"registry/{List[b - 1]}/{List[b - 1]}{BufferChar}{Date}{Extension}", "a") as p:
       print(p)
       p.write(str(HasPreset))
       p.write(BufferChar)
       print(HasPreset)
       p.write(PresetName)
       p.write(BufferChar)
       print(PresetName)
       p.write(Date)
       p.write(BufferChar)
       print(Date)
       time.sleep(1)
       print(List[b - 1])
       time.sleep(1)
       for b in range(len(List) - 1):
        print(b)
        print("Name from preset")
        time.sleep(1)
        print(PresetList[b - 1])
        time.sleep(1)
        print("Value")
        time.sleep(1)
        p.write(str(List[b + 1]))
        p.write(BufferChar)
        print(List[b + 1])
        time.sleep(1)
       print("Now adding to registry")
       with open("registry/CarbonIndex.txt", "a+") as t:
          print(t)
          t.seek(0)
          EamIareadyRegistered = t.read()
          LAmialreadyRegistered = EamIareadyRegistered.split(BufferChar)
          print(LAmialreadyRegistered)
          if List[0] in LAmialreadyRegistered:
             print("We skipping this one, Carbon knows you already")
             return 0
          else:
             print("adding you")
             t.write(BufferChar)
             t.write(List[0])
             return 0
   else: #Even with no preset, the program still needs to know they aren't using them to prevent corrupt readings
      b = 1
      print(fr"registry\{List[b - 1]}\{List[b -1]}-{Date}{Extension}")
      u = os.path.isdir(f"registry/{List[b - 1]}")
      print(u)
      if u == False:
         os.makedirs(f"registry/{List[b - 1]}")
      f = os.path.isfile(f"registry/{List[b - 1]}/{List[b - 1]}{BufferChar}{Date}{Extension}")
      if f == True:
        print("Whoops, there is already such file")
        return 1
      else:
        with open(f"registry/{List[b - 1]}/{List[b - 1]}{BufferChar}{Date}{Extension}", "a") as s:
         print(s)
         s.write(str(HasPreset)) #For standarizing
         s.write(BufferChar)
         s.write(PresetName)
         s.write(BufferChar)
         #print(Date)
         s.write(List[0])
         #print(List[b - 1])
         s.write(BufferChar)
         print("Writing to file soon")
         for b in range(len(List) - 1):
          s.write(str(List[b + 1]))
          s.write(BufferChar)
         print("Now adding to registry")
         with open("registry/CarbonIndex.txt", "a+") as t:
            print(t)
            t.seek(0)
            PreAmIAlreadyRegistered = t.read()
            print(PreAmIAlreadyRegistered)
            AmIAlreadyRegistered = PreAmIAlreadyRegistered.split(BufferChar)
            print(AmIAlreadyRegistered)
            if List[0] in AmIAlreadyRegistered:
              print("Carbon already knows you exist, we skipping this one")
              return 0
            else:
             t.write(BufferChar)
             t.write(List[0])
             return 0
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
    Entries.seek(0)
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
def MakeColorSelection(List, FusionImage, colorHexA, allowance): #Mode 1 = Selection generation, mode 2 = output generation
   a = List[0]
   b = List[1]
   c = 1
   d = 1
   coor = []
   col = ImageColor.getrgb(colorHexA)
   selection = Image.new(mode="RGBA", size=(a,b), color=(0,0,0,0))
   #selection.show()
   selected = Image.open(FusionImage)
   selected_color = selected.convert("RGBA")
   for c in range(b):
      print(c)
      for d in range(a):
       print(d)
       cor = (d, c)
       color = selected_color.getpixel(cor)
       print(color) #Makr a selection outline around your image
       if color < (col[0] + allowance, col[1] + allowance, col[2] + allowance, col[3] + allowance) and color > (col[0] - allowance, col[1] - allowance, col[2] - allowance, col[3] - allowance):
          selection.putpixel((d, c), (0, 247, 255, 128))
          if d > 0 and d < List[0]:
           if c > 0 and c < List[1]:
              borderleft = selection.getpixel((d - 1, c))
              if borderleft == (0, 0, 0, 0):
                 if d%2 == 0 and c%2 == 0:
                  selection.putpixel((d -1, c ),(0, 0, 0, 255))
                 elif d%2 == 0 and c%2 != 0:
                    selection.putpixel((d -1, c ), (255,255,255,255))
                 elif d%2 != 0 and c%2 == 0:
                    selection.putpixel((d -1, c ),(0, 0, 0, 255))
                 else:
                    selection.putpixel((d -1, c ), (255,255,255,255))                    
              borderRight = selection.getpixel((d + 1, c))
              if borderRight == (0, 0, 0, 0):
                 if d%2 == 0 and c%2 == 0:
                    selection.putpixel((d + 1, c), (0, 0, 0, 255))
                 elif d%2 == 0 and c%2 != 0:
                    selection.putpixel((d +1, c ), (255,255,255,255))
                 elif d%2 != 0 and c%2 == 0:
                    selection.putpixel((d +1, c ),(0, 0, 0, 255))
                 else:
                    selection.putpixel((d +1, c ), (255,255,255,255))         
              borderTop = selection.getpixel((d, c -1))
              if borderTop == (0,0,0,0):
                 if d%2 == 0 and c%2 == 0:
                  selection.putpixel((d , c - 1),(0, 0, 0, 255))
                 elif d%2 != 0 and c%2 == 0:
                    selection.putpixel((d , c - 1), (255,255,255,255))
                 elif d%2 == 0 and c%2 != 0:
                    selection.putpixel((d , c - 1),(0, 0, 0, 255))
                 else:
                    selection.putpixel((d , c - 1 ), (255,255,255,255))                      
              borderBottom = selection.getpixel((d, c+1))
              if borderBottom == (0,0,0,0):
                 if d%2 == 0 and c%2 == 0:
                  selection.putpixel((d , c + 1),(0, 0, 0, 255))
                 elif d%2 != 0 and c%2 == 0:
                    selection.putpixel((d , c + 1), (255,255,255,255))
                 elif d%2 == 0 and c%2 != 0:
                    selection.putpixel((d , c + 1),(0, 0, 0, 255))
                 else:
                    selection.putpixel((d , c + 1 ), (255,255,255,255))                   
                 
          coor.append(d)
          coor.append(c)
   final = Image.alpha_composite(selected_color, selection)
   selection.show()
   print("see the finale")
   time.sleep(7)
   final.show()
   final.save("import/Final.png")
   return coor


#print(DummyPic.size)
#print("Welcome to command line hexagono")
#print("You're in build...")
#print(BuildVersion)
#time.sleep(1)
#print("Right now we have to do..")
#print(TODO)

def CarbonSegment(root, count): #will add count for variable's in the future
   for a in range (count):
    Subframe = ctk.CTkFrame(root,fg_color="#c2c2c2", width=100, height=100)
    Subframe.pack(pady=10, padx=40, side="left")
    Subject = ctk.CTkLabel(Subframe, text=str(CarbonIndexEntries[a +1])).pack(pady=10)
    NoPicture = ctk.CTkImage(light_image=Image.open("art/no.png"), dark_image=Image.open(DummyPicTest), size=(400,225))
    Pic = ctk.CTkLabel(Subframe, text=None, image=NoPicture).pack(pady=10)
    for c in range(3):#Need to add actual data
       label = ctk.CTkLabel(Subframe, text="Dummy Variable").pack(pady=10)
    ViewAll = ctk.CTkButton(Subframe, text="List all entries").pack(pady=20)

def ColorPicker():
   pick_color = AskColor()
   ColorCode = pick_color.get()
   return ColorCode

def MakeGui():
   app = ctk.CTk()
   app.geometry("1280x720")
   app.maxsize(1920, 1080)
   app.minsize(1280,720)
   app.maxsize
   Tabs = ctk.CTkTabview(master=app, width=1920, height=1080)
   Tabs.pack(padx=20, pady=20)
   Tab1 = Tabs.add("Welcome",)
   Tab2 = Tabs.add("Carbon")
   Tab3 = Tabs.add("Argentum")
   Tab5 = Tabs.add("Settings")
   Tab4 = Tabs.add("About")

   Test = ctk.CTkButton(Tab1, text="Test the newest function in progress with dummy data", command=lambda : UpdateWindow(app)).pack(pady=20)
#About page code
   L1 = ctk.CTkLabel(Tab4, text="You are running version").pack(side="top")
   Version = ctk.CTkLabel(Tab4, text=BuildVersion).pack(pady=120)
   Maker = ctk.CTkLabel(Tab4, text="By Unreal Endrawings, with love from Mexico").pack(side="bottom")
#Carbon page code (NOt finished, need code to read from entries to actually display anything)
   b = BackendCarbonRead()
   frame = ctk.CTkScrollableFrame(Tab2, orientation="horizontal", width=(1920), height=1080)
   frame.pack(pady=20)
   CarbonSegment(frame, b)
   ArgentumSelect(Tab3)
   #Welcome tab will be a picture, no need for fancy stuff
   Tabs.set("Welcome")
   app.mainloop()
#Argentum tab code in here
def ArgentumSelect(Tab3):
   u = BackendCarbonRead()
   Pframe = ctk.CTkFrame(Tab3)
   Pframe.pack(pady=20)
   Foreign = ctk.CTkLabel(Pframe, text="Choose an entry to begin")
   Foreign.pack(pady=20)
   d = {}
   for l in range(u):
      d["ChooseEntry{0}".format(l)] = ctk.CTkButton(Pframe, text=str(CarbonIndexEntries[l + 1]))
      d["ChooseEntry{0}".format(l)].configure(command=lambda button = d["ChooseEntry{0}".format(l)], enttryName = str(CarbonIndexEntries[l + 1]): chooseFile(enttryName, Pframe))
      d["ChooseEntry{0}".format(l)].pack(pady=20) #need to create a dedicated function for the color isolation
def chooseFile(entry, tab):
   windowSize = 800
   ColorCode = "#ffffff"
   var = ctk.BooleanVar()
   a = browseFiles()
   print(a)
   b = BackendGetImageSize(a)
   for widget in tab.winfo_children():
    widget.destroy()
   Dlabel = ctk.CTkLabel(tab, text=entry)
   NoPicture = ctk.CTkImage(light_image=Image.open(a), dark_image=Image.open(a), size=(b[0], b[1]))
   global Opicture
   PrePicturre = Image.open(a)
#   print(str(int((b[1])/(b[0])) * windowSize))
   RPicture = PrePicturre.resize((windowSize,int(((b[1])/(b[0])) * windowSize)))

   Opicture = ImageTk.PhotoImage(RPicture)
   Pcanvas = ctk.CTkCanvas(tab,width=windowSize, height = ((b[1])/(b[0]) * windowSize))
   Pcanvas.create_image(0, 0, image=Opicture, anchor='nw')
#   Plabel = ctk.CTkLabel(tab, text=None, image=NoPicture)
   Dlabel.pack(pady=20)
   MetaFrame = ctk.CTkFrame(tab)
   ToolFrame = ctk.CTkFrame(MetaFrame, fg_color="light gray")
   ColorFrame = ctk.CTkFrame(MetaFrame, fg_color="light gray")
   Mode = ctk.CTkCheckBox(ToolFrame, text="Isolate subject")
   Mode2 = ctk.CTkCheckBox(ToolFrame, text="Isolate by Color", variable=var, onvalue=True ,offvalue=False, command=lambda: ToggleColorselect(var.get(), ColorFrame, tab))
   #Label = ctk.CTkLabel(tab, textvariable=var)
   Tlabel = ctk.CTkLabel(ToolFrame, text="Please input a date in yy-mm-dd",)
   Tinput = ctk.CTkTextbox(ToolFrame, height=20)
   RLabel = ctk.CTkLabel(ToolFrame, text="Or select an entry to associate it to")
   Available = BackEndCarbonListAllEntries(entry)
   EntrySelect = ctk.CTkComboBox(ToolFrame, values=Available)
   Preview = ctk.CTkButton(ToolFrame, text="Preview subject isolation", command=lambda: MakeIsolateImage(Pcanvas, a, entry, tab, b, windowSize))
   Submit = ctk.CTkButton(ToolFrame, text="Save your edits and submit")
   ColorDisplay = ctk.CTkFrame(ColorFrame,fg_color=ColorCode, height=100, width=100)
   Select = ctk.CTkButton(ColorFrame, text="Make selection", command=lambda: notImplemented(), state="disabled")
   TempLabel = ctk.CTkLabel(ColorDisplay, text="Your color goes here")
   Wheel = ctk.CTkButton(ColorFrame,text="Pick from color Wheel", command=lambda: getColor(ColorDisplay, tab), state="disabled")
   image = ctk.CTkButton(ColorFrame, text="Pick from current image", command=lambda: notImplemented())

#Pack all stuff and update
   MetaFrame.pack(padx=20, pady=20, side="right")
   ToolFrame.pack(padx=20, pady=20, side="top")
   Mode.pack(padx=20, pady=10, side="left")
   Mode2.pack(padx= 20, pady = 10, side="left")
   Preview.pack(pady=20, padx=20, side="bottom")
   Tlabel.pack(padx=20, pady=10, side="top")
   Tinput.pack(padx=20, pady=10, side="top")
   RLabel.pack(padx=20, pady=10)
   ColorFrame.pack(pady=20, padx=20)
   EntrySelect.pack(padx=20, pady=10, side="top")
   ColorDisplay.pack(padx=20,pady=20,side="right")
   TempLabel.pack(pady=20,padx=20)   
   Wheel.pack(pady=20, padx=20)
   Select.pack(padx=20, pady=20, side="top"),

   Pcanvas.pack(fill="both", expand=True)
   tab.update_idletasks()

def getColor(frame, tab):
   pick_color = AskColor()
   color = pick_color.get()
   frame.configure(fg_color=color)
   tab.update_idletasks()

def MakeIsolateImage(Canvasto, IsolateImage, subject, tab, size, WinSize):
   Ipicture = BackEndremoveBackground(IsolateImage,DummyDate,subject, True )
   print(Ipicture)
   UPicture = Image.open(Ipicture)
   Vpicture = UPicture.resize((WinSize, int(((size[1])/(size[0])) * WinSize)))
   global SPicture
   SPicture= ImageTk.PhotoImage(Vpicture)
   Canvasto.delete("all")
   Canvasto.create_image(0, 0, image=SPicture, anchor='nw')
   tab.update_idletasks

def ToggleColorselect(value, widget, tab):
 #  a = 
   if value == False:
      for child in widget.winfo_children():
         print("disabling")
         try:
          child.configure(state="disabled")
         except:
            print("Not available")
   else:
      for child in widget.winfo_children():
         print("enabling")
         try:
          child.configure(state="normal")
          #child.configure(hover=True)
         except:
            print("Not available")
   tab.update_idletasks()


#This will be used in the future
def CallApropiateMode(Arg1, Arg2, file):
   if Arg1 == True and Arg2 == True:
      NotImplemented()
   elif Arg1 == True and Arg2 == False:
      BackEndremoveBackground(a)
   elif Arg1 == False and Arg2 == True:
      NotImplemented
   else:
      print("Sometimes, the hooman mind is a mistery")

def UpdateWindow(Window):
   Window.destroy()
   MakeGui()


print("do you wanna stay on command line or open the gui")
MakeGui()
#BackEndCarbonListAllEntries("Alfa")
#picture = browseFiles()
#size = BackendGetImageSize(picture)
#listtest = MakeColorSelection(size, picture, "#ffffffff", 20,)
#print(listtest)
#BackendCarbonEntryCreator(DummyDate, DummyPresetList, True, "Tree tracking" )
#Installer = Tk() #Create window for gui boot
#Installer.geometry("1280x720") #Set resolution
#Installer.title("")
#ttk.Label(Installer, text="Wellcome to HEXAGONO setup, this program will guide you through stup for HEXAGONO 