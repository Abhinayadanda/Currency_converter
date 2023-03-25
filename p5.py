from tkinter import *
from requests import *

root=Tk()
root.title("Currency Converter")
root.geometry("1000x600+100+100")
f=("Arial",40,"bold")

def convert():
	try:
		aid=float(ent.get())
		if aid>0.0:
			wa="https://api.exchangerate-api.com/v4/latest/USD"
			res=get(wa)
			data=res.json()
			INR=data["rates"]["INR"]
			air=aid*INR
			air=round(air,2)
			msg="\u20B9"+str(air)
			ans.configure(text=msg)
		else:
			ans.configure(text="invalid amount")

	except ValueError:
		ans.configure(text="numbers only ")



lab1=Label(root,text="enter amt in $$",font=f)
ent=Entry(root,font=f)
btn=Button(root,text="Convert",font=f,command=convert)
ans=Label(root,font=f)

lab1.pack(pady=10)
ent.pack(pady=10)
btn.pack(pady=10)
ans.pack(pady=10)

root.mainloop()