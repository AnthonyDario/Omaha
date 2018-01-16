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

