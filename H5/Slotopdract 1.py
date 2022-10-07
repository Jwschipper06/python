import tkinter as tk
from tkinter import ttk
from turtle import bgcolor
root = tk.Tk()
def berekenbmi():
    length = ety1.get()
    length = int(length)
    length = length/100
    weight = ety2.get()
    weight = int(weight)
    bmi = int(weight/length**2)
    kleur = "white"
    if bmi < 18.5:
        kleur = "#4db9a8"
    elif bmi < 25:
        kleur = "#41ab34"
    elif bmi < 30:
        kleur = "#f7ae12"
    elif bmi < 35:
        kleur = "#ec6819"
    else:
        kleur = "#e52d20"
    
    bmilbl = ttk.Label(root, background = kleur, text = "Uw BMI is:  " + str(bmi))
    bmilbl.place(x = 50, y = 400, width = 100, height = 50)
root.title("BMI calculator")
root.geometry("800x600")
lbl1 = ttk.Label(root, text = "Voer uw lengte in:")
lbl1.place(x = 50, y = 100, width = 100, height = 50)

text1 = tk.StringVar()
ety1 = ttk.Entry(root, textvariable = text1)
ety1.place(x = 150, y = 100, width = 100, height = 50)

lbl2 = ttk.Label(root, text = "CM")
lbl2.place(x = 250, y = 100, width = 100, height = 50)

lbl3 = ttk.Label(root, text = "Voer uw gewicht in:")
lbl3.place(x = 40, y = 200, width = 110, height = 50)

text2 = tk.StringVar()
ety2 = ttk.Entry(root, textvariable = text2)
ety2.place(x = 150, y = 200, width = 100, height = 50)

lbl4 = ttk.Label(root, text = "KG")
lbl4.place(x = 250, y = 200, width = 100, height = 50)

btn = ttk.Button(root, text = "Bereken", command = lambda : berekenbmi())
btn.place(x = 50, y = 300, width = 100, height = 50)

lbl5 = ttk.Label(root, background="#4db9a8", text = "Ondergewicht")
lbl5.pack()
lbl5.place(x = 400, y = 100, width = 100, height = 20)

lbl5 = ttk.Label(root, background="#41ab34", text = "Gezond gewicht")
lbl5.pack()
lbl5.place(x = 400, y = 120, width = 100, height = 20)

lbl5 = ttk.Label(root, background="#f7ae12", text = "Overgewicht")
lbl5.pack()
lbl5.place(x = 400, y = 140, width = 100, height = 20)

lbl5 = ttk.Label(root, background="#ec6819", text = "Obesitas")
lbl5.pack()
lbl5.place(x = 400, y = 160, width = 100, height = 20)

lbl5 = ttk.Label(root, background="#e52d20", text = "Extreme obesitas")
lbl5.pack()
lbl5.place(x = 400, y = 180, width = 100, height = 20)
root.mainloop()