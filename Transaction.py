import json


class Transaction:
    def __init__(self, sku, amount, currency):
        self.sku = sku
        self.amount = amount
        self.currency = currency

    def __str__(self):
        # Return json format
        return json.dumps(self.__dict__)

    # Redefine repr to be the same as str
    __repr__ = __str__

    # Get currency
    def get_currency(self):
        return self.currency

    # Get sku
    def get_sku(self):
        return self.sku
