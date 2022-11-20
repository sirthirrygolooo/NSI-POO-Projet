from tkinter import *

window = Tk()
window.title("Tableau des scores")

lst = [[1,'Raj','Mumbai',19, 'Oui'],
	[2,'Aaryan','Pune',18, 'Non'],
	[3,'Vaishnavi','Mumbai',20, 'Pk pas'],
	[4,'Rachna','Mumbai',21, 'Feur'],
	[5,'Shubham','Delhi',21, 'Doze']]

entryList = []

for i in range(len(lst)):
    for j in range(5):
        entry = Entry(window, width=20, fg='blue', font=('Arial',16,'bold'))
        entryList.append(entry)
        entry.grid(row=i, column=j)
        entry.insert(END, lst[i][j])


window.mainloop()
