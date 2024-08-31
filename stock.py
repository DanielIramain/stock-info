import requests

import pandas as pd

class Fundamentals():
    def __init__(self, service, symbol, apikey) -> None:
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

    def validate_symbol(self, symbol):
        try:
            new_symbol = str(symbol)

            return new_symbol
        except ValueError:
            print('The symbol must be valid')

            return new_symbol
    
    def validate_apikey(self, apikey):
        try:
            new_apikey = int(apikey)

            return new_apikey
        except ValueError:
            print('The apikey must be an int value')

            return None

    def get_fundamentals(self):
        try:
            url = f'https://www.alphavantage.co/query?function={self.service}&symbol={self.symbol}&apikey={self.apikey}'

            request = requests.get(url)
            data = request.json()

            self.transform_data(data)
        except Exception as e:
            print(f'Error at getting fundamentals: {e}')

    def transform_data(self, data):
        '''
        Transforms data depending on the service in the solicitude
        '''
        try:
            if self.service == 'overview':
                df = pd.DataFrame.from_dict(data, orient='index')
            elif self.service == 'dividends' or self.service == 'splits':
                df = pd.DataFrame(data['data'])
            elif self.service == 'income_statement' or self.service == 'balance_sheet' or self.service == 'cash_flow':
                df_annual = pd.DataFrame(data['annualReports'])
                df_quarterly = pd.DataFrame(data['quarterlyReports'])
                
                df_annual.to_excel('prueba_anual.xlsx')
                df_quarterly.to_excel('prueba_cuatrimestral.xlsx')
            elif self.service == 'earnings':
                df_annual = pd.DataFrame(data['annualEarnings'])
                df_quarterly = pd.DataFrame(data['quarterlyEarnings'])
                
                df_annual.to_excel('prueba_anual.xlsx')
                df_quarterly.to_excel('prueba_cuatrimestral.xlsx')

            df.to_excel('prueba.xlsx')
        except Exception as e:
            print(f'Error transforming data: {e}')