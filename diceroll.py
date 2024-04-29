#bug: too many dices or faces can break the program

from tkinter import *
from random import randint


#divides "NUMdFACES" into "NUM FACES", computes the results and outputs it
def roll():
    try:
        form = str(entry.get())
        form = form.replace("d", " ").split()
    except:
        form = ["0", "0"]
    
    num = int(form[0])
    faces = int(form[1])

    results = []
    for i in range(num):
        n = randint(1, faces)
        results.append(n)
    
    result["text"] = results
    

#configs: not resizable, 600x600 pixels
window = Tk()
window.geometry("600x600")
window.resizable(False, False)

#context - what the program does
ctx = Label(window, text="Enter the number of dices you wish to roll and how many faces each one will have (NUMdFACES)", font=("TkDefaultFont", 10))
ctx.grid(column=0, row=0)

#input
entry = Entry(window)
entry.grid(column=0, row=1)

#filler to center the output
label = Label(text="", font=("TkDefaultFont", 120))
label.grid(column=0, row=3)

#output
result = Label(window, text="", font=("TkDefaultFont", 30))
result.grid(column=0, row=4)

#confirm
button = Button(window, text="ROLL", command=roll)
button.grid(column=0, row=2)

window.mainloop()