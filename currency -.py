from tkinter import *
import requests
from tkinter import ttk

names = [
        "USD",
        "AED",
        "AFN",
        "ALL" ,
        "AMD" ,
        "ANG" ,
        "AOA" ,
        "ARS" ,
        "AUD" ,
        "AWG" ,
        "AZN" ,
        "BAM" ,
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTN",
        "BWP",
        "BYN",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",
        "FJD",
        "FKP",
        "FOK",
        "GBP",
        "GEL",
        "GGP",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "IMP",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KID",
        "KMF",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRU",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SLL",
        "SOS",
        "SRD",
        "SSP",
        "STN",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TVD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "UYU",
        "UZS",
        "VES",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XCD",
        "XDR",
        "XOF",
        "XPF",
        "YER",
        "ZAR",
        "ZMW",
]

window = Tk()


def window_config():
        #window-configuration
        window.geometry("600x400")
        window.resizable(width=0,height=0)
        window.title('Currency Converter')
        window.config(background="#42aaf5")
        icon = PhotoImage(file='D:\Python Stuff Goes here\money.png')
        window.iconphoto(True,icon)


#currency-calculating-logic
def calccurrency(currencyname,amount,to_currency):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    currency = requests.get(url).json()    
    exchange_rate = currency['rates'][currencyname]

    amount = float(amount / exchange_rate)
    amount = round(amount * currency['rates'][to_currency],4)
    #result = Label(window,font = ("Arial",11,"bold"),borderwidth=5,text=amount,bg="white",relief=RAISED)
    #result.place(x=350,y=325)
    result.config(text = str(amount))
        

def gui():
        #Intro-Label 
        Title = Label(window ,text="Welcome To Currency Converter",font=("Arial",25,"bold"),bg="#3165e8",relief=RAISED,border= 3)
        Title.place(x=50,y=70)

        #From-currency-box
        combo = ttk.Combobox(window,values=names,state="readonly",font = ("Courier",11))
        combo.current(112) #Default Value
        combo.place(x=50,y=300)

        #To-Currency-Box
        combo2 = ttk.Combobox(window,values=names,state="readonly",font = ("Courier",12))
        combo2.current(0) #Default Value
        combo2.place(x=350,y=300)

        #entry-box
        entry = float
        entry = Entry(window,font = ("Arial",11),borderwidth=3)
        entry.insert(0,"Enter Amount here")
        entry.place(x=82,y=325)

        #convert-button
        def convert():      
            from_currency = combo.get()
            to_currency =  combo2.get()
            amount = float(entry.get())
            calccurrency(from_currency,amount,to_currency)  #calling the main function here

        convert = Button(window,text="Convert!",font = ("Comic Sans",16),command=convert,bg="#545c58",activebackground="#7d827f")
        convert.place(x=250,y=220)

        #result box
        global  result
        result = Label(window,font = ("Arial",11,"bold"),borderwidth=5,text='                                       ',bg="white",relief=RAISED)
        result.place(x=350,y=325)

window_config()
gui()
window.mainloop()

