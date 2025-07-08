def stock_portfolio_tracker():
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 2800, "MSFT": 320, "AMZN": 3500}
    portfolio = {}

    print("\nStock Portfolio Tracker")
    print("Enter 'done' when finished.")

    while True:
        stock = input("Enter stock symbol: ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("Stock not found. Available: ", ", ".join(stock_prices.keys()))
            continue
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("Please enter a valid number.")

    if not portfolio:
        print("No stocks added.")
        return

    total_investment = sum(stock_prices[stock] * qty for stock, qty in portfolio.items())
    print("\nYour Portfolio:")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares at ${stock_prices[stock]} each => ${stock_prices[stock] * qty}")
    print(f"\nTotal Investment: ${total_investment}")

if __name__ == "__main__":
    stock_portfolio_tracker()