from flask import Flask, request
import json
from utils import get_all_currency_rates, get_one_currency_rate

app = Flask(__name__)

# Load dummy data
transactions_file = open("./dummy_data/transactions.json", "r")
currency_rates_file = open("./dummy_data/currency_rates.json", "r")

transactions = json.load(transactions_file)
currency_rates = json.load(currency_rates_file)

# Add CAD to USD rate to currency rates
currency_rates = get_all_currency_rates(currency_rates)

# Close files
transactions_file.close()
currency_rates_file.close()


# Home route to check it's working
@app.route("/")
def home():
    return "Hello World"


# Route to get all currency rates
@app.route("/currency_rates")
def get_currency_rates():
    # Get original currencies
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
        return rate
