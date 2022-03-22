import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class CurencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Impossible to convert {quote} in {quote}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Currency is not found "{quote}"')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Currency is not found "{base}"')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Amount must be a number, not "{amount}"')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base



