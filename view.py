from tkinter import Tk, ttk

from stock import Fundamentals

#GUI
class Viewer:
        def __init__(self, master) -> None:
                self.master = master
                
                master.title('Stock Information')

                self.combo = ttk.Combobox(master, state='readonly', 
                     values=['overview', 
                             'income_statement', 
                             'balance_sheet', 
                             'cash_flow',
                             'earnings'])
                self.combo.pack()

                self.label_ticker = ttk.Label(master, text='Enter ticker').pack(side='top')
                self.ticker = ttk.Entry(master)
                self.ticker.pack()

                self.label_key = ttk.Label(master, text='Enter API KEY').pack(side='top')
                self.api_key = ttk.Entry(master)
                self.api_key.pack()

                self.close_button = ttk.Button(master, text='Exit', command=master.quit)
                self.close_button.pack()

                self.save_button = ttk.Button(master, text='Get data', command=Fundamentals.get_fundamentals())
                self.save_button.pack()