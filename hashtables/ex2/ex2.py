#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(hashtable,ticket.source, ticket.destination)

    
    
    for ticket in tickets:
      if ticket.source !="NONE":
        pass
      else:
        check = 1
        counter = 0
        current_source = ticket.destination
        
        while check !=0:

          route[counter] = current_source
          if None not in route:
            return route
      
          counter +=1
          a = hash_table_retrieve(hashtable,current_source)
          if a is None:
            route = [None] * length
            check = 0
          else:
            current_source = a      

    return route
