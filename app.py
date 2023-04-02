import requests
import json
import datetime


def get_stock_info(symbol):
    # Enter your Alpha Vantage API key here
    api_key = "B92DFS3VV30O8Q36"

    # Build the URL for retrieving the stock quote
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"

    try:
        # Send the request and get the response
        response = requests.get(url)

        # Convert the response to JSON format
        data = response.json()

        # Get the current date and time
        current_time = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")

        # Get the stock information from the response
        stock_name = data["Global Quote"]["01. symbol"]
        stock_price = float(data["Global Quote"]["05. price"])
        stock_change = float(data["Global Quote"]["09. change"])
        stock_change_percent = float(data["Global Quote"]["10. change percent"][:-1])

        # Build the URL for retrieving the company name
        url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={symbol}&apikey={api_key}"

        # Send the request and get the response
        response = requests.get(url)

        # Convert the response to JSON format
        data = response.json()

        # Get the company name from the response
        company_name = data["bestMatches"][0]["2. name"]

        # Format the output string
        output = f"Output: \n"
        output += f"{current_time}\n"
        output += f"{company_name} ({stock_name})\n"
        output += f"{stock_price:.2f} {'+' if stock_change > 0 else ''}{stock_change:.2f} ({'+' if stock_change_percent > 0 else ''}{stock_change_percent:.2f}%)\n"

        # Print the output
        print(output)

    except (KeyError, IndexError):
        print("Invalid symbol. Please try again.")

    except requests.exceptions.RequestException:
        print("Unable to connect to the server. Please check your internet connection and try again.")


# Get the stock symbol from the user
symbol = input("Please enter a symbol: ").upper()

# Call the get_stock_info function
get_stock_info(symbol)
