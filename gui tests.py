#Self-explanatory lol
import tkinter as tk

title = "App"
dims = "700x700"
bgColor = "#000000"
textColor1 = "#FFFF00"
bdSize = 10

window = tk.Tk()
window.geometry("500x500")
window.title(title)
window.config(background=bgColor)

labelIntro = tk.Label(window,text="This is an app",
                      font=("Consolas",40,"bold"),
                      fg=textColor1,
                      bg=bgColor,
                      relief="sunken",
                      bd=10,
                      compound="top"
                      )
labelIntro.pack()

def click():
    window2 = tk.Tk()
    window2.title("you clicked the button")
    window2.geometry("600x500")
    window2.config(background=bgColor)

    labelButton = tk.Label(window2,text="You clicked the button!",font=("Consolar", 40, "bold"),fg=textColor1,bg=bgColor)
    labelButton.pack()
    window2.mainloop()

button = tk.Button(window,
                   text="Click this",
                   command=click,
                   font=("Consolas",40,"bold"),
                   fg=textColor1,
                   bg=bgColor,
                   bd=10
                   )
button.pack()

window.mainloop()