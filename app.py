from flask import Flask, request
import json
from utils import get_all_currency_rates, get_one_currency_rate
import Transaction


app = Flask(__name__)

# Load dummy data
transactions_file = open("./dummy_data/transactions.json", "r")
currency_rates_file = open("./dummy_data/currency_rates.json", "r")

transactions = json.load(transactions_file)
currency_rates = json.load(currency_rates_file)

# Add CAD to USD rate to currency rates
currency_rates = get_all_currency_rates(currency_rates)


transactions = transactions["transactions"]

# Create an array of transactions
transactions_list = []
for transaction in transactions:
    transactions_list.append(
        Transaction.Transaction(
            transaction["sku"], transaction["amount"], transaction["currency"]
        )
    )

print(transactions_list)


# Close files
transactions_file.close()
currency_rates_file.close()


# Home route to check it's working
@app.route("/")
def home():
    return "Hello World"


## Currency routes ##


# Route to get all currency rates
@app.route("/currency_rates")
def get_currency_rates():
    return currency_rates


# Route to get a currency rate by currency node
@app.route("/currency_rate")
def get_currency_rate():
    # Get parameters from URL
    from_currency = request.args.get("from")
    to_currency = request.args.get("to")

    rate = get_one_currency_rate(from_currency, to_currency, currency_rates)
    if rate is None:
        return {"Error": "Curriencies not found"}
    else:
        return {"rate": rate}


## Transactions routes ##


# Return all transactions by currency code
@app.route("/transactions")
def get_transactions():
    # Get parameters from URL
    currency = request.args.get("currency")
    sku = request.args.get("sku")

    # Return list
    new_transactions_list = []
    try:
        for transaction in transactions_list:
            if sku is None or transaction.get_sku() == sku:
                if transaction.get_currency() == currency:
                    new_transactions_list.append(transaction.__dict__)
    except Exception as e:
        print("Error a la ruta /transactions: {}".format(e))
    return new_transactions_list
