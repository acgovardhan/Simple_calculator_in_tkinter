#simple calculator using tkinter
import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("calculator")
root.geometry("500x500")

def my_func():
	a=int(enter1.get())
	b=int(enter2.get())
	c=combo.get()
	
	if c == "+":
		x=a+b
	
	elif c== "-":
		x=a-b
		
	elif c== "*":
		x=a*b
		
	elif c== "/":
		if b==0:
			if a==0:
				x="not defined"
			else :
				x="zero division error"
		else :
			x=a/b		
				   	   	  	   	    	
	else :
		x="ERROR"
		
	text4.config(text=x)
		
text0=tk.Label(root,text="CALCULATOR",bg="skyblue",fg="black")
text0.grid(row=0,column=2)

text1=tk.Label(root,text="1 st no : ",fg="red",bg="yellow",height=5)
text1.grid(row=1,column=1)

text2=tk.Label(root,text="2 nd no : ",fg="red",bg="yellow",height=5)
text2.grid(row=2,column=1)

text3=tk.Label(root,text="operation : ",fg="blue",bg="pink",height=5)
text3.grid(row=3,column=1)

enter1=tk.Entry(root,fg="blue")
enter1.grid(row=1,column=2)

enter2=tk.Entry(root,fg="blue")
enter2.grid(row=2,column=2)

combo=ttk.Combobox(root,values=["+","-","*","/"])
combo.grid(row=3,column=2)
combo.set("select_operation")
combo["state"]='readonly'

btn=tk.Button(root,command=my_func,text="equals",height=5,fg="purple",bg="pink",activebackground="lightgreen",activeforeground="white")
btn.grid(row=4,column=2)

text4=tk.Label(root,fg="white",bg="orange",height=3,width=20)
text4.grid(row=5,column=2)

root.mainloop()