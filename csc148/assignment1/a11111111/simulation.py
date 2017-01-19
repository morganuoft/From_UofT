"""Assignment 1 - Grocery Store Simulation (Task 3)

This file should contain all of the classes necessary to model the different
kinds of events in the simulation.
"""
# Feel free to add extra imports here for your own modules.
# Just don't import any external libraries!
from container import PriorityQueue
from store import GroceryStore
import event


class GroceryStoreSimulation:
    """A Grocery Store simulation.

    This is the class which is responsible for setting up and running a
    simulation.
    The API is given to you: your main task is to implement the two methods
    according to their docstrings.

    Of course, you may add whatever private attributes and methods you want.
    But because you should not change the interface, you may not add any public
    attributes or methods.

    This is the entry point into your program, and in particular is used for
    autotesting purposes. This makes it ESSENTIAL that you do not change the
    interface in any way!
    """
    # === Private Attributes ===
    # @type _events: PriorityQueue[Event]
    #     A sequence of events arranged in priority determined by the event
    #     sorting order.
    # @type _store: GroceryStore
    #     The grocery store associated with the simulation.
    def __init__(self, store_file):
        """Initialize a GroceryStoreSimulation from a file.

        @type store_file: str
            A file containing the configuration of the grocery store.
        @rtype: None
        """
        self._events = PriorityQueue()
        self._store = GroceryStore(store_file)

    def run(self, event_file):
        """Run the simulation on the events stored in <event_file>.

        Return a dictionary containing statistics of the simulation,
        according to the specifications in the assignment handout.

        @type self: GroceryStoreSimulation
        @type event_file: str
            A filename referring to a raw list of events.
            Precondition: the event file is a valid list of events.
        @rtype: dict[str, object]
        """
        # Initialize statistics
        stats = {
            'num_customers': 0,
            'total_time': 0,
            'max_wait': -1
        }
        max_wait_dic = {}
        max_wait_list = []
        initial_events = event.create_event_list(event_file)

        # initial_events is a PriorityQueue of [item.timestamp, item]
        while not initial_events.is_empty():
            todo = initial_events.remove()
            # 'todo' is the element of initial event.
            from event import FinishCheck, Arrive
            # if isinstance()
            if isinstance(todo[1], FinishCheck):
                stats['num_customers'] = stats['num_customers'] + 1
                stats['total_time'] = todo[0]
                max_wait_dic[todo[1].costumer.name] = todo[0] - max_wait_dic[todo[1].costumer.name]
            if isinstance(todo[1], Arrive):
                if not todo[1].costumer.name in max_wait_dic:
                    max_wait_dic[todo[1].costumer.name] = todo[0]
            spawn = todo[1].do(self._store)
            # spawn is the [[item.timestamp, item],[item.timestamp, item]]...by do() methods.
            if isinstance(spawn,list):
                for i in spawn:
                    initial_events.add(i)
                # add [item.timestamp, item] to PriorityQueue.
            # self._store is now the name of the GroceryStore.
        for i in max_wait_dic:
            max_wait_list.append(max_wait_dic[i])
        max_wait_list.sort()
        stats['max_wait'] = max_wait_list.pop()
        # Begin to calculate max_wait.


        # TODO: Process all of the events, collecting statistics along the way.

        return stats


# We have provided a bit of code to help test your work.
if __name__ == '__main__':
    sim = GroceryStoreSimulation('config.json')
    final_stats = sim.run('events.txt')
    print(final_stats)