from binance.client import Client
from binance_key import Binancekey1, BinanceDemoKey
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor



# Actual keys for trading on Binance
api_key = Binancekey1['api_key']
api_secret = Binancekey1['api_secret']

# Demo Keys for trading on Binance
# api_key = BinanceDemoKey['api_key']
# api_secret = BinanceDemoKey['api_secret']

client = Client(api_key, api_secret)
# client.API_URL = 'https://testnet.binance.vision/api'  # Uncomment this while running real time version


btc_price = {'error':False}

def btc_trade_history(msg):
    if msg['e'] != 'error':
        print(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
    else:
        btc_price['error'] = True

bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket('BTCEUR', btc_trade_history)
bsm.start()
bsm.stop_socket(conn_key)
reactor.stop()