#This is a gui for makepro

from tkinter import *



#set up variables to be assigned with gui parts
#folder = "Hasn't changed"

class WindowWidgets:
    def __init__(self):
        window = Tk()
        window.title("Makepro")

        folder = StringVar()
        strNumOfFiles = StringVar()

        entryFrm = Frame(window)
        entryFrm.pack()
        btnFrm = Frame(window)
        btnFrm.pack()

        btnMake = Button(btnFrm, text = "Make!")
        btnCancel = Button(btnFrm, text = "Cancel", command = window.quit)
        btnUpdate = Button(btnFrm, text = "Update", command = WindowWidgets.update)
        folderLbl = Label(entryFrm, text = "Folder: ")
        folderEnt = Entry(entryFrm, textvariable = folder)
        numFilesLbl = Label(entryFrm, text = "Number of Files: ")
        numFilesEnt = Entry(entryFrm, textvariable = strNumOfFiles)
        fr = Button(window, text = "few", command = window.quit)

        folderLbl.grid(row = 1, column = 1)
        folderEnt.grid(row = 1, column = 2)
        numFilesLbl.grid(row = 2, column = 1)
        numFilesEnt.grid(row = 2, column = 2)
        btnMake.grid(row = 1, column = 1)
        btnCancel.grid(row = 1, column = 2)
        btnUpdate.grid(row = 1, column = 3)
        fr.pack()

        window.mainloop()

    def update():
        print(folder.get())
        print(strNumOfFiles.get())
        numOfFiles = eval(strNumOfFiles.get())
        print(numOfFiles + 1)
        return

WindowWidgets()
