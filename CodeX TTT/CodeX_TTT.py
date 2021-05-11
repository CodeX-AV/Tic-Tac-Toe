from tkinter import *
import tkinter.messagebox

app=Tk()
app.title("CodeX TTT")
app.iconbitmap("TTT.ico")

bclick = True

def ttt(buttons):
    global bclick
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True