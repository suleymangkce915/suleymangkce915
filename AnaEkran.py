
import datetime
import tkinter as tk
import HesapMakinası


x = datetime.datetime.now()

 
pencere = tk.Tk()
pencere.title('Ana Ekran')
ekrangenisligi=pencere.winfo_screenwidth()//2-175
ekranyuksekligi=pencere.winfo_screenheight()//2-350
pencere.geometry("350x650+{}+{}".format(ekrangenisligi, ekranyuksekligi))

button0 = tk.Label(pencere, text=x, font="Courier 8 bold", width=30, justify="center")
button0.place(x=70, y=20)

button1 = tk.Button(pencere, text="Hava Durumu", font="Courier 16 bold", width=15, justify="center")
button1.place(x=70, y=75)

button2 = tk.Button(pencere, text="Takvim", font="Courier 16 bold", width=8, justify="center")
button2.place(x=120, y=125)

button3 = tk.Button(pencere, text="Hesap Makinesi", font="courier 16 bold", width=15, justify="center")
button3.place(x=80, y=175)

button4 = tk.Button(pencere, text="Oyunlar", font="Courier 16 bold", width=10, justify="center")
button4.place(x=120, y=225)

button5 = tk.Button(pencere, text="Çıkış", font="Courier 16 bold", justify="center", command=exit)
button5.place(x=125, y=550)

pencere.mainloop()  
tton