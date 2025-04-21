from datetime import datetime
import time

from Admin import Admin
from Logging import Logging
from Operation import Operation
from OperationType import OperationType
from Stock import Stock
from User import User


class StockBrokerSystem:
    def __init__(self):
        self.operations = {}  # Use a dictionary to store operations by their ID
        self.users = {}
        self.stocks = {}  # Dictionary to store stocks by their symbol
        self.global_permissions = {
            OperationType.BUY: True,
            OperationType.SELL: True,
            OperationType.SHORT: True,
        }
        self.logger = Logging()  # Instance of the Logging class

    def add_user(self, user_id, is_admin=False):
        if is_admin:
            self.users[user_id] = Admin(user_id, self)
        else:
            self.users[user_id] = User(user_id)
        return self.users[user_id]

    def add_stock(self, symbol, company_name, current_price):
        if symbol in self.stocks:
            print(f"Stock with symbol {symbol} already exists")
            return
        stock = Stock(symbol, company_name, current_price)
        self.stocks[symbol] = stock
        print(f"Added stock: {symbol} - {company_name} at price {current_price}")
        return stock

    def get_stock(self, symbol):
        return self.stocks.get(symbol, None)

    def add_operation(self, user_id, operation_type, symbol, quantity):
        user = self.users.get(user_id)
        if not user:
            print(f"User {user_id} does not exist")
            return
        stock = self.stocks.get(symbol)
        if not stock:
            print(f"Stock {symbol} does not exist")
            return
        if user.enabled and self.global_permissions.get(operation_type, False) and user.permissions.get(operation_type,
                                                                                                        False):
            operation = Operation(operation_type, user, stock, quantity)
            self.operations[operation.operation_id] = operation
            self.logger.log_operation(operation)  # Log the operation
            print(f"Operation added: {operation.__dict__}")
        else:
            print(f"Operation {operation_type.value} is not allowed for user {user_id}")

    def delete_operation(self, operation_id):
        if operation_id in self.operations:
            del self.operations[operation_id]
            print(f"Operation with id {operation_id} deleted")
        else:
            print(f"Operation with id {operation_id} not found")

    def perform_operation(self, operation_id):
        operation = self.operations.get(operation_id)
        if operation:
            operation.perform()
        else:
            print(f"Operation with id {operation_id} not found")

    def perform_all_operations(self):
        for operation in self.operations.values():
            operation.perform()

    def schedule_operation(self, user_id, operation_type, symbol, quantity, timestamp):
        user = self.users.get(user_id)
        if not user:
            print(f"User {user_id} does not exist")
            return
        if timestamp > datetime.now().timestamp():
            time.sleep(timestamp - time.time())
            self.add_operation(user_id, operation_type, symbol, quantity)
            self.perform_operation(next(reversed(self.operations)))
        else:
            print("Scheduled time must be in the future")
