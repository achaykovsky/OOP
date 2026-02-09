from Jira.Ticket import Ticket


# Time Complexity: O(n)
# Space Complexity: O(n)
class TicketList:
    def __init__(self):
        self.head = None

    def insert_ticket(self, ticket_id: int, n: int):
        new_ticket = Ticket(ticket_id, n)

        # Case 1: Insert at the head
        if not self.head or n == 1:
            new_ticket.next = self.head
            self.head = new_ticket
        else:
            prev = None  # Pointer to the previous ticket
            current = self.head

            # Case 2: Traverse to the correct insertion point
            while current and current.priority < n:
                prev = current
                current = current.next

            # Insert the new ticket
            prev.next = new_ticket
            new_ticket.next = current

        # Shift priorities of subsequent tickets
        current = new_ticket.next
        while current:
            current.priority += 1
            current = current.next

    def to_list(self):
        """Converts the linked list to a list of dictionaries for easy visualization."""
        result = []
        current = self.head
        while current:
            result.append({"id": current.id, "priority": current.priority})
            current = current.next
        return result
