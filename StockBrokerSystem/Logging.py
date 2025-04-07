class Logging:
    def __init__(self):
        self.operations_log = {}  # Dictionary to store operation logs by ID

    def log_operation(self, operation):
        self.operations_log[operation.operation_id] = operation
        print(f"Logged operation: {operation.operation_id}")

    def get_operations_log_by_time(self, start_time):
        return {op_id: op for op_id, op in self.operations_log.items() if op.timestamp >= start_time}

    def get_operations_log_by_user(self, user_id):
        return {op_id: op for op_id, op in self.operations_log.items() if op.user.user_id == user_id}

    def get_operations_log_by_time_and_user(self, start_time, user_id):
        return {op_id: op for op_id, op in self.operations_log.items() if
                op.timestamp >= start_time and op.user.user_id == user_id}