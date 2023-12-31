# Get all currency rates. This function return the original data plus
# the CAD to USD rate
def get_all_currency_rates(currency_rates):
    # Get original currencies
    currencies = currency_rates["currency_rates"]

    # Find CAD to EUR rate and EUR to USD rate
    for currency in currencies:
        if currency["from"] == "CAD" and currency["to"] == "EUR":
            cad2eur = float(currency["rate"])
        elif currency["from"] == "EUR" and currency["to"] == "USD":
            eur2usd = float(currency["rate"])

    # Add CAD to USD rate
    cad2usd = cad2eur * eur2usd

    # Utilitzem un format de tres decimals com la resta de valors de la llista
    # i afegim també el valor contrari
    currencies.append(
        {"from": "CAD", "to": "USD", "rate": str("{:.3f}".format(cad2usd))}
    )
    currencies.append(
        {"from": "USD", "to": "CAD", "rate": str("{:.3f}".format(1 / cad2usd))}
    )

    return currencies


# Get currency rate if exists, returns None otherwise
def get_one_currency_rate(from_currency, to_currency, currency_list):
    # Find the currencies
    for currency in currency_list:
        if currency["from"] == from_currency and currency["to"] == to_currency:
            rate = currency["rate"]
    # We might have to check if the currencies are inverted in a real case,
    # but with our dummy data we don't have to
    return rate
