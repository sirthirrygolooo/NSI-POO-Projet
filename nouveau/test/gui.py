from tkinter import *

class Window:
    def __init__(self, title, resolution, resizable):
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(resolution)
        self.window.resizable(width=resizable, height=resizable)
        self.navbar = None
        self.window.config(menu=self.navbar)
        self.frame = None

    def showFrame(self, Frame):
        """Show a frame
        {Frame} -> Object"""
        Frame.window = self.window
        for i in Frame.elements:
            i.pack(expand=YES)
        self.frame = Frame

    def hideFrame(self, Frame):
        """Hide a frame
        {Frame} -> Object"""
        Frame.window = None
        Frame.destroy()
        self.frame = None

    def changeFrame(self, Frame):
        """Change the current frame to another
        {Frame} -> Object"""
        self.hideFrame(self.frame)
        self.showFrame(Frame)

    def setNavbar(self, Navbar):
        """Set a navbar to the window
        {Navbar} -> Object"""
        self.navbar = Navbar

    def removeNavbar(self):
        """Remove the navbar from the window"""
        self.navbar = None

    def show(self):
        """Show the window"""
        self.window.mainloop()


class Frame:
    def __init__(self):
        self.window = None
        self.elements = []

    def addLabel(self, text, fontfamily, fontsize, expand=NO):
        """Add a label to the frame
        {text} -> String
        {fontfamily} -> String
        {fontsize} -> Integer
        {expand} -> Boolean"""
        self.elements.append(Label(self.window, text=text, font=(fontfamily, fontsize)))

    def addButton(self, text, fontfamily, fontsize, command, expand=NO, pady=0):
        """Add a button to the frame
        {text} -> String
        {fontfamily} -> String
        {fontsize} -> Integer
        {command} -> Function
        {expand} -> Boolean
        {pady} -> Integer"""
        self.elements.append(Button(self.window, text=text, font=(fontfamily, fontsize), command=command))

    def addEntry(self, fontfamily, fontsize, expand=NO, pady=0):
        """Add an entry to the frame
        {fontfamily} -> String
        {fontsize} -> Integer
        {expand} -> Boolean
        {pady} -> Integer"""
        self.elements.append((Entry(self.window, font=(fontfamily, fontsize))).focus_set()).pack(pady=pady, expand=expand)


class Navbar:
    def __init__(self):
        self.window = None
        self.navbar = Menu(self.window) 
        self.listNavbar = []
    
    def addNavbar(self):
        """Add a navbar to the navbar"""
        self.listNavbar.append(Menu(self.navbar, tearoff=0))

    def addCommand(self, name, command):
        """Add a command to the navbar
        {name} -> String
        {command} -> Function"""
        self.listNavbar[-1].add_command(label=name, command=command)

    def addSeparator(self):
        """Add a separator to the navbar"""
        self.listNavbar[-1].add_separator()

    def closeNavbar(self, name):
        """Close a navbar
        {name} -> String"""
        self.navbar.add_cascade(label=name, menu=self.listNavbar[-1])


