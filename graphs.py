from collections import deque

# graph as a stack because of key value pairs
graph = {}

# 1st degree connections
graph["Juan"] = ["Alice", "Bob", "Claire"]

# 2nd degree connections
graph["Alice"] = ["Peggy"]
graph["Bob"] = ["Peggy", "Carlos"]
graph["Claire"] = ["Thom", "Jonny"]
# 3rd degree connections
graph["Peggy"] = []
graph["Carlos"] = []
graph["Thom"] = []
graph["Joony"] = []

# if the person's last letter ends with m we will treat him as the seller
def personIsSeller(name):
    return name[-1] == 'm'


def breadthFirstSearch(name):
    # create a queue
    searchQueue = deque()
    # add all the 1st degree connections
    searchQueue += graph["Juan"]
    # keep track of searched people
    searched = []
    # while the que is not empty we'll get the first person in the queue (FIFO)
    while searchQueue:
        person = searchQueue.popleft()
        # if it hasn't been searched we check if its the seller and return true
        if not person in searched:
            if personIsSeller(person):
                print(person + " is a mango seller!")
                return True
            # else we add its connections to the queue and append their name in searched array
            else:
                searchQueue += graph[person]
                searched.append(person)
    # if we reach this point there wasn't any seller
    return False

breadthFirstSearch("Juan")
