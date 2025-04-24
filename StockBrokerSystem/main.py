import time

from OperationType import OperationType
from StockBrokerSystem import StockBrokerSystem

if __name__ == '__main__':
    system = StockBrokerSystem()

    # Add some stocks
    system.add_stock("AAPL", "Apple Inc.", 150.00)
    system.add_stock("GOOGL", "Alphabet Inc.", 2800.00)

    # Add a regular user
    system.add_user("user1")

    # Add an admin user
    admin = system.add_user("admin1", is_admin=True)

    # Admin controls
    admin.enable_operation(OperationType.BUY)
    admin.disable_operation(OperationType.SELL)
    admin.enable_user("user1")
    admin.disable_user("user1")
    admin.enable_operation_for_user("user1", OperationType.SHORT)
    admin.disable_operation_for_user("user1", OperationType.BUY)

    # Adding and performing operations
    system.add_operation("user1", OperationType.BUY, "AAPL", 10)
    system.perform_all_operations()
