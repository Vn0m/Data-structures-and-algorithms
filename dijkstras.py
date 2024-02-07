# Initialize the graph as a dictionary
graph = {}

# Define the connections and costs between nodes in the graph
# Here, we represent the graph as a dictionary where each node is a key,
# and its value is another dictionary containing neighboring nodes and their associated costs
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# Define infinity for comparison
infinity = float("inf")

# Initialize the costs dictionary with the cost of reaching each node from the start node
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Initialize the parents dictionary to keep track of the parent node for each node
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Initialize a list to keep track of processed nodes
processed = []

# Define a function to find the node with the lowest cost among the nodes not yet processed
def findLowestCostNode(costs):
    lowestCost = float("inf")
    lowestCostNode = None
    for node in costs:
        cost = costs[node]
        # Check if the cost to reach this node is lower than the current lowest cost
        # and if the node has not been processed yet
        if cost < lowestCost and node not in processed:
            lowestCost = cost
            lowestCostNode = node
    return lowestCostNode

# Find the node with the lowest cost and update costs and parents of neighboring nodes iteratively
node = findLowestCostNode(costs)
while node is not None:
    # Get the cost of reaching the current node
    cost = costs[node]
    # Get the neighboring nodes of the current node
    neighbors = graph[node]
    # Iterate over neighboring nodes and update costs and parents if a shorter path is found
    for n in neighbors.keys():
        # Calculate the new cost to reach the neighbor through the current node
        newCost = cost + neighbors[n]
        # Update the cost and parent if the new cost is lower than the current cost
        if costs[n] > newCost:
            costs[n] = newCost
            parents[n] = node
    # Mark the current node as processed
    processed.append(node)
    # Find the next node with the lowest cost among the nodes not yet processed
    node = findLowestCostNode(costs)
