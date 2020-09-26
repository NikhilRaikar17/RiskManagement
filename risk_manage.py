# !/usr/bin/python3
import tkinter as tk  
from functools import partial  
   
   
def call_result(label_result,labelResult_new,labelResult_stoploss, n1, n2,n3,n4):  
    num1 = (n1.get())  
    num2 = (n2.get())
    num3 = (n3.get())
    num4 = (n4.get())
    
    if "." in num1 or "." in num2 or "." in num4 or "." in num3:
        num1= float(num1)
        num2 = float(num2)
        num3 = float(num3)
        num4 = float(num4)

    if type(num1) == float:
        num1 = round(num1)
    
    if type(num2) == float:
        num2 = round(num2)
    
    if type(num3) == float:
        num3 = round(num3)
    
    if type(num4) == float:
        num4 = round(num4)

    actual_capital = int(num1)*0.03

    if num3!= 0:
        updated_capital = actual_capital*int(num3)
        risk = updated_capital/int(num2)
    else:
        updated_capital = actual_capital
        risk = updated_capital/int(num2)

    result = (int(num1)*int(num3))/int(num4)

    label_result.config(text="Maximum shares you can take per trade = %d" % result)  
    labelResult_new.config(text="Your capital for the day= %d" % updated_capital)  
    labelResult_stoploss.config(text="Your risk per trade = %d, **DO-NOT risk more than this!" % risk)  
    return  
   
root = tk.Tk()  
root.geometry('500x500')  
  
root.title('Risk Management Calculator')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
number3 = tk.StringVar()  
number4 = tk.StringVar()  
  
labelNum1 = tk.Label(root, text="Total Capital").place(x = 30,y = 50)   
  
labelNum2 = tk.Label(root, text="Stoploss Points").place(x = 30, y = 90)   

labelNum3 = tk.Label(root, text="Margin %").place(x = 30, y = 120)

labelNum4 = tk.Label(root, text="Stock Value").place(x = 30, y = 150)   
  
labelResult = tk.Label(root) 
labelResult_new = tk.Label(root) 
labelResult_stoploss = tk.Label(root) 
  
labelResult.place(x = 130, y = 260) 
labelResult_new.place(x = 130, y = 290)  
labelResult_stoploss.place(x = 130, y = 310)  
  
entryNum1 = tk.Entry(root, textvariable=number1).place(x = 130, y = 50)    
  
entryNum2 = tk.Entry(root, textvariable=number2).place(x = 130, y = 90)     

entryNum3 = tk.Entry(root, textvariable=number3).place(x = 130, y = 120)     

entryNum4 = tk.Entry(root, textvariable=number4).place(x = 130, y = 150)     
  
call_result = partial(call_result, labelResult,labelResult_new,labelResult_stoploss, number1, number2,number3,number4)  
  
buttonCal = tk.Button(root, text="Calculate Risk", command=call_result).place(x = 130, y = 220)  
  
root.mainloop()