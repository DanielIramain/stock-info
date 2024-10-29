import requests
from tkinter.filedialog import asksaveasfile 

import pandas as pd

class Information():
    ''' Manage the data request '''
    def __init__(self, service:str, symbol:str, apikey:int) -> None:
        self.__service = service
        self.__symbol = self.validate_symbol(symbol)
        self.__apikey = self.validate_apikey(apikey)

    @property
    def service(self):
        return self.__service

    @property
    def symbol(self):
        return self.__symbol

    @property
    def apikey(self):
        return self.__apikey

    @symbol.setter
    def symbol(self, new_symbol):
        self.__symbol = self.validate_symbol(new_symbol)

    @apikey.setter
    def apikey(self, new_apikey):
        self.__apikey = self.validate_apikey(new_apikey)

    def validate_symbol(self, symbol: str) -> str:
        try:
            new_symbol = str(symbol)

            return new_symbol
        except ValueError:
            print('The symbol must be valid')

            return new_symbol
    
    def validate_apikey(self, apikey: int) -> int:
        try:
            new_apikey = int(apikey)

            return new_apikey
        except ValueError:
            print('The apikey must be an int value')

            return None

    def sheets_to_excel(self, data: pd.DataFrame):
        try:
            with asksaveasfile(mode='w', defaultextension='.xlsx') as file:
                data[0].to_excel(file.name, sheet_name='Annual') 
                data[1].to_excel(file.name, sheet_name='Quarterly')
        except AttributeError:
            print('User canceled')

    def request_information(self, url:str):
        try:
            request = requests.get(url)
            data = request.json()
            self.transform_data(data)
        except Exception as e:
            print(f'Error at getting fundamentals: {e}')
    
    def get_data(self):
        try:
            url = f'https://www.alphavantage.co/query?function={self.service}&symbol={self.symbol}&apikey={self.apikey}'
            self.request_information(url)
        except Exception as e:
            print(f'Error in request: {e}')

class Fundamentals(Information):
    ''' Get the fundamental information of a company '''
    def __init__(self, service, symbol, apikey) -> None:
        super().__init__(service, symbol, apikey)

    def transform_data(self, data: dict):
        '''
        Transforms data depending on the service in the solicitude
        '''
        try:
            if self.service == 'overview':
                df = pd.DataFrame.from_dict(data, orient='index')

                with asksaveasfile(mode='w', defaultextension='.xlsx') as file:
                    df.to_excel(file.name)
            elif self.service in ['dividends', 'splits']:
                df = pd.DataFrame(data['data'])
                
                with asksaveasfile(mode='w', defaultextension='.xlsx') as file:
                    df.to_excel(file.name)
            elif self.service in ['income_statement', 'balance_sheet', 'cash_flow']:  
                df_annual = pd.DataFrame(data['annualReports'])
                df_quarterly = pd.DataFrame(data['quarterlyReports'])
                
                self.sheets_to_excel([df_annual, df_quarterly])
            elif self.service == 'earnings':
                df_annual = pd.DataFrame(data['annualEarnings'])
                df_quarterly = pd.DataFrame(data['quarterlyEarnings'])
                
                self.sheets_to_excel([df_annual, df_quarterly])
            elif self.service == 'etf_profile':
                df = pd.DataFrame.from_dict(data, orient='index')

                with asksaveasfile(mode='w', defaultextension='.xlsx') as file:
                    df.to_excel(file.name)
        except Exception as e:
            print(f'Error transforming data: {e}')

class TimeSeries(Information):
    '''
    Get time series of the company
    '''
    def __init__(self, service: str, symbol: str, apikey: int, interval: str) -> None:
        super().__init__(service, symbol, apikey)
        self.__interval = self.validate_interval(interval)

    @property
    def interval(self):
        return self.__interval
    
    @interval.setter
    def interval(self, new_interval):
        self.__interval = self.validate_interval(new_interval)

    def validate_interval(self, interval):
        try:
            if type(interval) != str:
                print('Interval must be a str')

                return None
            else:
                return interval
        except ValueError:
            print('Invalid interval')

            return None

    def get_data_per_interval(self):
        try:
            url = f'https://www.alphavantage.co/query?function={self.service}&symbol={self.symbol}&interval={self.interval}&apikey={self.apikey}'
            self.request_information(url)
        except Exception as e:
            print(f'Error in request: {e}')
    
    def transform_data(self, data: dict):
        '''
        Transforms data depending on the service in the solicitude
        '''
        try:
            services = ['time_series_intraday', 
                    'time_series_daily', 
                    'time_series_daily_adjusted',
                    'time_series_weekly',
                    'time_series_weekly_adjusted',
                    'time_series_monthly',
                    'time_series_monthly_adjusted',
                    'global_quote']
            
            if self.service in services[0:7]:
                data_keys = list(data.keys())
                df = pd.DataFrame.from_dict(data[data_keys[1]], orient='index')

                with asksaveasfile(mode='w', defaultextension='.xlsx') as file:
                    df.to_excel(file.name)
            elif self.service == 'global_quote':
                df = pd.DataFrame(data)

                with asksaveasfile(mode='w', defaultextension='.xlsx') as file:
                    df.to_excel(file.name)
        except Exception as e:
            print(f'Error transforming time series data: {e}')