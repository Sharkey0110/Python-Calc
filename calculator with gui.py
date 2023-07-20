#IMPORTS

from tkinter import *
import functools as ft
app = Tk()

app.title("Calculator")

#FUNCTIONS


#Error checks the character being inputted to ensure equations remain logical
def number_input(num):
    if len(math["text"]) > 0:
        #if the current inputs length is bigger than 0, it identifies double operators and deletes them
        if math["text"][-1] in ["+","*","//"] and num in ["+","*","//"]:
            return
        else:
            #Checks for any number after a 0 after an operator
            if num == "0" and math["text"][-1] in ["+","-","*","//"]:
                return
            else:
                math["text"]= math["text"] + num
    #if the current inputs length is less than 0, it checks for starting equations with 0s or operators        
    elif num not in ["+","*","//"]:
        if num != "0":
            math["text"]= math["text"] + num
            answer["text"] = answer["text"][:-999]



def clear_func(amount):
    #clears the function by 1 or max depending on button pressed
    math["text"]= math["text"][:-(amount)]
    if amount == 999:
        answer["text"]=answer["text"][:-(amount)]



def calculate():
    #calculates the number
    try:
        #turns equation into int to solve, then back into string
        answer["text"] = str(eval(math["text"]))
        #doesnt send the answer back into the equation if it is equal to 0 
        if answer["text"] != "0":
            math["text"] = answer["text"]
        else:
            math["text"]= math["text"][:-(999)]
    except:
        pass


#The code that creates all of the buttons and windows
app.configure(bg="#9cf7ca")
math = Label(app,text="",width=12, bg = "#9cf7ca")
answer = Label(app,text="",width=5,bg = "#9cf7ca")
for x in range(10):
    Button(app,text = str(x),relief=RIDGE,bd=5,command=ft.partial(number_input,str(x)),width = 5,bg = "cyan").grid(row= (x+3)//3,column=x%3)
       
Button(app,text="0",relief=RIDGE,bd=5,command=ft.partial(number_input,"0"),width = 20,bg = "cyan").grid(row=4,column=0,columnspan=3)
Button(app,text="+",relief=RIDGE,bd=5,command=ft.partial(number_input,"+"),width = 5,bg = "cyan").grid(row=1,column=3)
Button(app,text="-",relief=RIDGE,bd=5,command=ft.partial(number_input,"-"),width = 5,bg = "cyan").grid(row=2,column=3)
Button(app,text="x",relief=RIDGE,bd=5,command=ft.partial(number_input,"*"),width = 5,bg = "cyan").grid(row=3,column=3)
Button(app,text="//",relief=RIDGE,bd=5,command=ft.partial(number_input,"//"),width = 5,bg = "cyan").grid(row=4,column=3)
Button(app,text="C",relief=RIDGE,bd=5,command=ft.partial(clear_func,1),width = 5,bg = "cyan").grid(row=1,column=4)
Button(app,text="CE",relief=RIDGE,bd=5,command=ft.partial(clear_func,999),width = 5,bg = "cyan").grid(row=2,column=4)
Button(app,text="=",relief=RIDGE,bd=5,command=calculate,width= 5,height=3,bg = "cyan").grid(row=3,column=4,rowspan=4)


#The code that formats the labels stored as variables onto the window
math.grid(row=0,column=0,columnspan=3)
answer.grid(row=0,column=3,columnspan=4)

app.mainloop()
