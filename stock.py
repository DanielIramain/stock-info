import requests

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
                print(data)
        except Exception as e:
            print(f'Error transforming data: {e}')