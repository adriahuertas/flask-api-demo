from flask import Flask
import json

app = Flask(__name__)

# Load dummy data
transactions_file = open("./dummy_data/transactions.json", "r")
currency_rates_file = open("./dummy_data/currency_rates.json", "r")

transactions = json.load(transactions_file)
currency_rates = json.load(currency_rates_file)

# Close files
transactions_file.close()
currency_rates_file.close()


# Home route to check it's working
@app.route("/")
def home():
    return "Hello World"
