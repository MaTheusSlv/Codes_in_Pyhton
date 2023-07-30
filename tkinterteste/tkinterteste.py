#App de teste pra estudar tkinter

import tkinter as tk
import tkinter.ttk as ttk

#Windows
root = tk.Tk()
root.title('App feito com Tkinter')
root.geometry('600x400')
frame1 = tk.Frame(master=root, relief= 'groove', borderwidth=2, height=200)
frame1.pack(fill=tk.X)
frame2 = tk.Frame()

#Widgets
widlabel = tk.Label(text='Esse é um Label', master=frame1)
widlabel.pack()

widlabel2 = tk.Label(text='Esse é um Label personalizado', fg='white', bg='black', master=frame1, relief='flat')
widlabel2.pack()

btn = tk.Button(text='Clique-me!', master=frame1)
btn.pack()

root.mainloop()