from Library.User import User


class Admin(User):
    def __init__(self, user_id, system):
        super().__init__(user_id)
        self.system = system

    def enable_operation(self, operation_type):
        self.system.global_permissions[operation_type] = True
        print(f"Operation {operation_type.value} enabled for all users")

    def disable_operation(self, operation_type):
        self.system.global_permissions[operation_type] = False
        print(f"Operation {operation_type.value} disabled for all users")

    def enable_user(self, user_id):
        user = self.system.users.get(user_id)
        if user:
            user.enable()
            print(f"User {user_id} enabled")
        else:
            print(f"User {user_id} does not exist")

    def disable_user(self, user_id):
        user = self.system.users.get(user_id)
        if user:
            user.disable()
            print(f"User {user_id} disabled")
        else:
            print(f"User {user_id} does not exist")

    def enable_operation_for_user(self, user_id, operation_type):
        user = self.system.users.get(user_id)
        if user:
            user.enable_operation(operation_type)
            print(f"Operation {operation_type.value} enabled for user {user_id}")
        else:
            print(f"User {user_id} does not exist")

    def disable_operation_for_user(self, user_id, operation_type):
        user = self.system.users.get(user_id)
        if user:
            user.disable_operation(operation_type)
            print(f"Operation {operation_type.value} disabled for user {user_id}")
        else:
            print(f"User {user_id} does not exist")
