class Ticket:
    def __init__(self, ticket_id: int, priority: int):
        self.id = ticket_id
        self.priority = priority
        self.next = None