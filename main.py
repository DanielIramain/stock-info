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
                self.apikey = ttk.Entry(master)
                self.apikey.pack()

                self.close_button = ttk.Button(master, text='Exit', command=master.quit)
                self.close_button.pack()

                self.save_button = ttk.Button(master, text='Get data', command=self.capture_data)
                self.save_button.pack()
        
        def capture_data(self):
                '''
                Captures the input in the GUI and calls the method to get the data
                '''
                service = self.combo.get()
                symbol = self.ticker.get()
                api_key = self.apikey.get()
                
                asset = Fundamentals(service, symbol, api_key)
                asset.get_fundamentals()

if __name__ == '__main__':
    root = Tk()
    my_gui = Viewer(root)
    root.mainloop()