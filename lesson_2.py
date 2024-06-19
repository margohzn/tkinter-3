#learning spinbox, menu bar, spin bar
from tkinter import * 
from tkinter.ttk import * 

window = Tk()
window.geometry("400x400")

#creating progress bar widget
progress = Progressbar(window, orient = HORIZONTAL, length = 300, mode = "indeterminate")

#fonction resbonsible for updating the progress bar value 
def bar():
    import time
    progress["value"] = 20
    window.update_idletasks()
    time.sleep(1)

    progress["value"] = 40
    window.update_idletasks()
    time.sleep(1)

    progress["value"] = 50
    window.update_idletasks()
    time.sleep(1)

    progress["value"] = 60
    window.update_idletasks()
    time.sleep(1)

    progress["value"] = 80
    window.update_idletasks()
    time.sleep(1)

    progress["value"] = 100


progress.pack(pady = 10)

button1 = Button(window, text = "Start", command = bar).pack(pady = 10)

#creating spinerbox 
spin = Spinbox(window, from_ = 0, to = 10)
spin.pack()

window.mainloop()