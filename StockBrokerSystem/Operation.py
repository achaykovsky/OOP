import uuid
from datetime import datetime


class Operation:
    def __init__(self, operation_type, user, stock, quantity):
        self.operation_id = uuid.uuid4().hex
        self.operation_type = operation_type
        self.user = user
        self.stock = stock
        self.quantity = quantity
        self.timestamp = datetime.now().timestamp()

    def perform(self):
        print(
            f"Performing {self.operation_type.value} operation for user {self.user.user_id} on stock {self.stock.symbol} with quantity: {self.quantity}")
