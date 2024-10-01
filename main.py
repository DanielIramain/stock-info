from tkinter import Tk, ttk, StringVar

from stock import Fundamentals

#GUI
class Viewer:
        def __init__(self, master) -> None:
                self.master = master
                
                master.title('Stock Information')

                self.label_service = ttk.Label(master, text='Choose service').pack(side='top')
                self.options = {'Fundamentals': ['overview',
                                            'income_statement', 
                                            'balance_sheet',
                                            'cash_flow',
                                            'earnings',
                                            'dividends',
                                            'splits',
                                            'etf_profile'], 'B': [4, 5, 6]}
                
                ### Combobox 1
                self.cb1_values = list(self.options.keys())
                self.cb1_var = StringVar()
                self.cb1_var.set(self.cb1_values[0])
                self.cb1 = ttk.Combobox(master, values=list(self.options.keys()), textvariable=self.cb1_var)
                self.cb1.pack(side='top')
                self.cb1.bind('<<ComboboxSelected>>', self.get_var_cb)

                ### Combobox 2
                self.cb2_var = StringVar()
                self.cb2_var.set(self.options[self.cb1_values[0]][0])
                self.cb2 = ttk.Combobox(master, values=self.options[self.cb1_values[0]], textvariable=self.cb2_var)
                self.cb2.pack(side='bottom')

                ### Ticker entry
                self.label_ticker = ttk.Label(master, text='Enter ticker').pack(side='top')
                self.ticker = ttk.Entry(master)
                self.ticker.pack()

                ### API Key entry
                self.label_key = ttk.Label(master, text='Enter API KEY').pack(side='top')
                self.apikey = ttk.Entry(master)
                self.apikey.pack()

                ### Buttons
                self.save_button = ttk.Button(master, text='Get data', command=self.capture_data)
                self.save_button.pack()
                self.close_button = ttk.Button(master, text='Exit', command=master.quit)
                self.close_button.pack()
        
        def get_var_cb(self, event):
               '''
               Captures and set the values in the combobox
               '''
               value = self.cb1_var.get()
               self.cb2_var.set(self.options[value][0])
               self.cb2.config(values=self.options[value])
        
        def capture_data(self):
                '''
                Captures the input in the GUI and calls the method to get the data
                '''
                service = self.cb2.get()
                symbol = self.ticker.get()
                api_key = self.apikey.get()
                
                asset = Fundamentals(service, symbol, api_key)
                asset.get_data()

if __name__ == '__main__':
    root = Tk()
    my_gui = Viewer(root)
    root.mainloop()