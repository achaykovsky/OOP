import uuid


class Stock:
    def __init__(self, symbol, company_name, current_price):
        self.stock_id = uuid.uuid4().hex  # Unique identifier for the stock
        self.symbol = symbol
        self.company_name = company_name
        self.current_price = current_price

    def update_price(self, new_price):
        self.current_price = new_price
        print(f"Price of {self.symbol} updated to {self.current_price}")
