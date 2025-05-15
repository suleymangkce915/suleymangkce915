
import datetime
import tkinter as tk


x = datetime.datetime.now()

pencere = tk.Tk()
pencere.title('Takvim')
ekrangenisligi=pencere.winfo_screenwidth()//2-150
ekranyuksekligi=pencere.winfo_screenheight()//2-200
pencere.geometry("300x400+{}+{}".format(ekrangenisligi, ekranyuksekligi))

takvim = tk.Label(pencere, text=datetime.datetime.now(), font="Courier 8 bold", width=30, justify="center")
takvim.place(x=10, y=5)



 

pencere.mainloop()
