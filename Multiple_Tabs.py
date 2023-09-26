import tkinter as tk
from tkinter import ttk as ttk

window=tk.Tk()
window.geometry("1270x720")
notebook=ttk.Notebook(window)  # widget that manages a collection of windows /displays

tab1=tk.Frame(notebook,bg="red")
tab2=tk.Frame(notebook)

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack()

tab1_label =tk.Label(tab1,text="Welcome to tab -1")
tab1_label.pack()

window.mainloop()