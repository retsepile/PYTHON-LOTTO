# Retsepile Koloko class 2

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
window = Tk()
window.geometry("500x500")
window.title("LOTTO")
window.geometry("1200x800")
loader = Image.open("balls.jpg")
render = ImageTk.PhotoImage(loader)
image = Label(window, image=render)
image.place(x=0, y=0)


class InforMation:
    def __init__(self, master):
        self.window = window
        self.name_label = Label(window, text="Enter your name:", bg="yellow")
        self.name_label.place(x=5, y=10)
        self.user_entry = Entry(window)
        self.user_entry.place(x=150, y=10)
        self.address_lbl = Label(window, text="Enter address:", bg="yellow")
        self.address_lbl.place(x=5, y=50)
        self.address_entry = Entry(window)
        self.address_entry.place(x=150, y=50)
        self.id_no_label = Label(window, text="Enter ID No:", bg="yellow")
        self.id_no_label.place(x=5, y=100)
        self.identity_entry = Entry(window)
        self.identity_entry.place(x=150, y=100)
        self.email_label = Label(window, text="Email:", bg="yellow")
        self.email_label.place(x=10, y=150)
        self.mail_entry = Entry(window)
        self.mail_entry.place(x=150, y=150)
        self.btn_exit = Button(window, text="Exit", command=self.exit, borderwidth="10", bg="gold")
        self.btn_exit.place(x=150, y=200)
        self.btn_log = Button(window, text="Log in", command=self.login, borderwidth="10", bg="gold")
        self.btn_log.place(x=10, y=200)
        self.btn_clear = Button(window, text="Clear", command=self.clear, borderwidth="10", bg="gold")
        self.btn_clear.place(x=250, y=200)

    def login(self):
        self.name = ["Zoe"]
        self.address = [ "1055 Black street"]
        self.ID_NO = ["991010 5708 084"]
        self.email = ["zoe@gmail.com"]

        found = False
        for x in range(len(self.name)):
            if self.user_entry.get() == self.name[x] and self.address_entry.get() == self.address[x] and \
                    self.identity_entry.get() == self.ID_NO[x] and self.mail_entry.get() == self.email[x]:
                found = True

        if found == True:
            window.destroy()
            import newpage

    def exit(self):
        self.ask = messagebox.askquestion("Ithuba National Lottery - Login", "Do you really want to exit the app?")
        if self.ask == "yes":
            self.window.destroy()

    def clear(self):
        self.user_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.mail_entry.delete(0, END)
        self.identity_entry.delete(0, END)

    def age(self, age):
        self.age = age
        if age >= 18:
            messagebox.showinfo("", "Let's play!!!")
        elif age < 18:
            messagebox.showinfo("", "You are to young play. Please try again in ")
        else:
            messagebox.showinfo("", "Invaild ID number. Try again")

    def id_no(self):
     pass


i = InforMation(window)
window.mainloop()
