'''
This is a library to interface with the Robinhood API via Python
'''

import requests

class RobinhoodAPI:

    base_url = 'https://api.robinhood.com'

    def get_quote(self, symbol):
        ''' Gets a quote for a symbol 
        '''
        r = requests.get('{0}/quotes/{1}/'.format(self.base_url, symbol))
        if r.status_code == requests.codes.ok:
            return r.text
        else:
            raise ValueError('Symbol {0} not found'.format(symbol))

    def get_quotes(self, symbols):
        ''' Gets quotes for a list of symbols
        '''
        symbol_string = ','.join(symbols)
        r = requests.get('{0}/quotes/?symbols={1}'.format(self.base_url, symbol_string))
        if r.status_code == requests.codes.ok:
            return r.text
        else:
            raise ValueError('No symbols found'.format(symbol))

    def get_historical_quotes(self, symbol, interval, span):
        ''' gets the historical quotes for a symbol using the given interval and span

        '''
        url = '{0}/quotes/historical/{1}/?interval={2}&span={3}' \
              .format(self.base_url, symbol, interval, span)
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            return r.text
        else:
            raise ValueError(r.text)

'''
    GET /quotes/historicals/$symbol/[?interval=$i&span=$s&bounds=$b] interval=week|day|10minute|5minute|null(all) span=day|week|year|5year|all bounds=extended|regular|trading
    '''
