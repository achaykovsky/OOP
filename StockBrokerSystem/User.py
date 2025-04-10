from OperationType import OperationType


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.enabled = True
        self.permissions = {
            OperationType.BUY: True,
            OperationType.SELL: True,
            OperationType.SHORT: True,
        }

    def disable(self):
        self.enabled = False

    def enable(self):
        self.enabled = True

    def disable_operation(self, operation_type):
        self.permissions[operation_type] = False

    def enable_operation(self, operation_type):
        self.permissions[operation_type] = True