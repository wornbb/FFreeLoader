from lib2to3.pygram import Symbols
from symtable import Symbol
import yahoo_client
configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'YOUR_API_KEY'
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
symbols='AAPL'
api_instance.quotes(symbols)