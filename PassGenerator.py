from tkinter import *
from tkinter import ttk
import random
import string
import pyperclip

class PassGenerator():
     def __init__(self):
          self.okno=Tk()
          self.okno.title('Generator haseł')
          self.okno.geometry('500x400-100-100')

          self.font_big='Helavica 16 normal'
          self.font='Helavica 12 normal'

          self.sl=IntVar() ## small letter
          self.bl=IntVar() ## big letter
          self.num=IntVar()
          self.sp=IntVar() ## spacial symbols
          
          lab1 = Label(self.okno, text="Prosty generator haseł", font=self.font_big)
          lab1.grid(row=1, column=1, columnspan=2, pady=10, padx=15)

          lab=Label(self.okno, text="Małe litery", font=self.font)
          lab.grid(row=2, column=1, padx=15, pady=4)
 
          small_leter = ttk.Scale(self.okno, from_=0, to=10, orient = HORIZONTAL, variable= self.sl, command=self.slider_changed1)
          small_leter.grid(row=2, column=2)

          self.lab2=Label(self.okno, text=0, font=self.font)
          self.lab2.grid(row=2, column=3)

          lab=Label(self.okno, text="Duże litery", font=self.font)
          lab.grid(row=3, column=1, padx=15, pady=4)
 
          small_leter = ttk.Scale(self.okno, from_=0, to=10, orient = HORIZONTAL, variable= self.bl, command=self.slider_changed2)
          small_leter.grid(row=3, column=2)

          self.lab3=Label(self.okno, text=0, font=self.font)
          self.lab3.grid(row=3, column=3)

          lab=Label(self.okno, text="Cyfry", font=self.font)
          lab.grid(row=4, column=1, padx=15, pady=4)
 
          small_leter = ttk.Scale(self.okno, from_=0, to=10, orient = HORIZONTAL, variable= self.num, command=self.slider_changed3)
          small_leter.grid(row=4, column=2)

          self.lab4=Label(self.okno, text=0, font=self.font)
          self.lab4.grid(row=4, column=3)

          lab=Label(self.okno, text="Znaki specjalne", font=self.font)
          lab.grid(row=5, column=1, padx=15, pady=4)
 
          small_leter = ttk.Scale(self.okno, from_=0, to=10, orient = HORIZONTAL, variable= self.sp, command=self.slider_changed4)
          small_leter.grid(row=5, column=2)

          self.lab5=Label(self.okno, text=0, font=self.font)
          self.lab5.grid(row=5, column=3)


          bnt=Button(self.okno, text="Utwórz hasło" , padx=3, pady=3, bg='lightblue', relief='solid', borderwidth=0.5, font=self.font_big, command = self.password_generate)
          bnt.grid(row=6, column=1, columnspan=3, sticky='news', padx=15, pady=10)

          self.okno.mainloop()


     def slider_changed1(self, *event):
         #pass
          self.lab2.config(text=self.sl.get())

     def slider_changed2(self, *event):
         #pass
          self.lab3.config(text=self.bl.get())

     def slider_changed3(self, *event):
         #pass
          self.lab4.config(text=self.num.get())

     def slider_changed4(self, *event):
         #pass
          self.lab5.config(text=self.sp.get())

     def password_generate(self, *event):
          lowercase = string.ascii_lowercase
          uppercase = string.ascii_uppercase
          punctuation = string.punctuation
          digits = string.digits
          
          losowe_lowercase= random.sample(lowercase, self.sl.get())
          losowe_uppercase=random.sample(uppercase, self.bl.get())
          losowe_puncation=random.sample(punctuation, self.sp.get())
          losowe_digits=random.sample(digits , self.num.get())
          losowe_znaki =losowe_lowercase+losowe_uppercase+losowe_puncation+losowe_digits
          #print(losowe_znaki)
          haslo = ''.join(losowe_znaki)
          

          haslo_kopia = list(haslo)
          nowe_haslo=''
          for a in range(len(haslo_kopia)):
               x= random.choice(haslo_kopia)
               haslo_kopia.remove(x)
               nowe_haslo=nowe_haslo+str(x)
         

          self.password = Entry(self.okno, font=self.font_big, relief='flat', borderwidth=3)
          self.password.grid(row=7, column=1, columnspan=3, pady=2, padx=15)
          self.password.insert(1, nowe_haslo)

          copy =Button(self.okno, text="kopiuj do schowka",  padx=3, pady=3, bg='lightblue', relief='solid', borderwidth=0.5, font=self.font_big, command = self.password_copy)
          copy.grid(row=8, column=1, columnspan=3, sticky='news', padx=15, pady=5)




     def password_copy(self, *event):
          a= self.password.get()
          pyperclip.copy(a)
          self.password.delete(0, END)

          self.password.insert(4, 'skopikowano')
          




          

PassGenerator()
