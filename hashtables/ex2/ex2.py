#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    
    # A dictionary of form {Departure : Destination}

    flights = {ticket.source : ticket.destination for ticket in tickets}

    # Append the Departure of all the trip to a route list.

    route = [flights['NONE']]

    for _ in range(length-1):

        # Look into the dictionary for the last key departure and add
        # its destination, and so on.

        route.append(flights[route[-1]])

    return route


if __name__ == "__main__":
    
    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")

    tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5,
                ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

    print(reconstruct_trip(tickets, 10))