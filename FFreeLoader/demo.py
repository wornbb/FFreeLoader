import yahoo_client
import json

configuration = yahoo_client.Configuration()
configuration.api_key['X-API-KEY'] = 'anEGPki60w9uSjIkjNNtl2ZGFGsNF5GKakfMA7L0'
api_instance = yahoo_client.APIApi(yahoo_client.ApiClient(configuration))
symbols='AAPL,MSFT' # no space between symbols
api_instance.quotes(symbols)
data = json.loads(api_instance.api_client.last_response.data.decode())

a = "stop"