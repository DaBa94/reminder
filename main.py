import tkinter as tk
import json

import core

with open('config.json','r')as file:
    data = json.load(file)

if __name__=="__main__":

    window=tk.Tk()
    window.title("Appointment")
    window.geometry("300x300")

    window.mainloop()