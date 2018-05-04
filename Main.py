import tkinter as tk 
import random

mainwindow = tk.Tk()
mainwindow.title('Dice game')

'''
clears Text widget and places roll result in its place
'''
def rolldice():
    rollresult = random.randint(1,6)
    txtresult.delete(1.0, tk.END) 
    txtresult.insert(tk.END, rollresult)
    
txtresult = tk.Text(mainwindow, width=10, height=2)
txtresult.insert(tk.END,'Roll for result')
txtresult.pack(side = tk.TOP)

btnroll = tk.Button(mainwindow, text='Roll the dice', width=10, height=2, command=rolldice)
btnroll.pack(side = tk.BOTTOM)

mainwindow.mainloop() 