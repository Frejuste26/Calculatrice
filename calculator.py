from tkinter import *


root = Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += value
    label_screen.config(text=equation)

def clear():
    global equation
    equation = ""
    label_screen.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
            equation = str(result)
        except:
            result = "Erreur"
            equation = ""
    label_screen.config(text=result)

label_screen = Label(root, width=30, height=2, text="", font=("Arial", 20, "bold"))
label_screen.place(x=30, y=20)

Button(root, text="C", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#3697f5", fg="white", cursor="hand2", command=lambda: clear()).place(x=30, y=120) 
Button(root, text="/", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("/")).place(x=175, y=120)
Button(root, text="%", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("%")).place(x=315, y=120)   
Button(root, text="*", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("*")).place(x=455, y=120)

Button(root, text="7", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("7")).place(x=30, y=220) 
Button(root, text="8", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("8")).place(x=175, y=220)
Button(root, text="9", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("9")).place(x=315, y=220)   
Button(root, text="-", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("-")).place(x=455, y=220)

Button(root, text="4", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("4")).place(x=30, y=320) 
Button(root, text="5", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("5")).place(x=175, y=320)
Button(root, text="6", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("6")).place(x=315, y=320)   
Button(root, text="+", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("+")).place(x=455, y=320)

Button(root, text="1", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("1")).place(x=30, y=420) 
Button(root, text="2", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("2")).place(x=175, y=420)
Button(root, text="3", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("3")).place(x=315, y=420)   
Button(root, text="0", width=13, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show("0")).place(x=30, y=515)

Button(root, text=".", width=5, height=1, font=("Arial", 20, "bold"), bd=1, bg="#383838", fg="white", cursor="hand2", command=lambda: show(".")).place(x=315, y=515)   
Button(root, text="=", width=5, height=4, font=("Arial", 20, "bold"), bd=1, bg="#fe9037", fg="white", cursor="hand2", command=lambda: calculate()).place(x=455, y=420)

root.mainloop()