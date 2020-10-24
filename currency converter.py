import requests
import json
from tkinter import *

root = Tk()
variable1 = StringVar(root)
variable2 = StringVar(root)
variable1.set("currency")
variable2.set("currency")


def RealTimeCurrencyConversion():
    from_currency = variable1.get()
    to_currency = variable2.get()
    api_key = "EKP3RDOG0WXQEOWJ"
    base_url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    main_url = base_url+"&from_currency="+from_currency+"&to_currency="+to_currency+"&apikey="+api_key
    req_ob = requests.get(main_url)
    data = req_ob.text
    parsed = json.loads(data)
    Exchange_Rate = float(parsed["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    amount = float(Amount1_field.get())
    new_amount = round(amount * Exchange_Rate, 3)
    Amount2_field.insert(0, str(new_amount))


def clear_all():
    Amount1_field.delete(0, END)
    Amount2_field.delete(0, END)

if __name__ == "__main__":
    root.configure(background="white")
    root.geometry()
    headlabel = Label(root, text='welcome to Real Time Currency Converter', fg='black', bg='light blue')
    label1 = Label(root, text="Amount: ", fg='black', bg='dark grey')
    label2 = Label(root, text="From Currency", fg='black', bg='dark grey')
    label3 = Label(root, text="To Currency", fg='black', bg='dark grey')
    label4 = Label(root, text="Converted Amount: ", fg='black', bg='dark grey')
    headlabel.grid(row=0, column=1)
    label1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    label3.grid(row=3, column=0)
    label4.grid(row=4, column=0)
    Amount1_field = Entry(root)
    Amount2_field = Entry(root)
    Amount1_field.grid(row=1, column=1, ipadx='25')
    Amount2_field.grid(row=5, column=1, ipadx='25')
    CurrencyCode_list = ['INR', 'USD', 'CAD', 'CNY', 'DKK', 'EUR', 'NGN']
    FromCurrency_option = OptionMenu(root, variable1, *CurrencyCode_list)
    ToCurrency_option = OptionMenu(root, variable2, *CurrencyCode_list)
    FromCurrency_option.grid(row=2, column=1, ipadx=10)
    ToCurrency_option.grid(row=3, column=1, ipadx=10)
    button1 = Button(root, text='Convert', bg='light blue', fg="black", command=RealTimeCurrencyConversion)
    button1.grid(row=4, column=1)
    button2 = Button(root, text='Clear', bg='light blue', fg="black", command=clear_all)
    button2.grid(row=6, column=1)
    root.mainloop()
