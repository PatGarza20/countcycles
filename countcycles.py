# By Patricio Garza | https://github.com/PatGarza20

#Global Variables
cycles = 0
longer = []
longest = []
layers = 0

class Node:
    def __init__(self, number, connections, visited):
        self.number = number
        self.connections = connections
        self.visited = visited
    
    def getNumber(self):
        return self.number
    
    def getConnections(self):
        return self.connections
    
    def setConnections(self, new):
        self.connections = new

    def isVisited(self):
        return self.visited
    
    def setVisited(self, visit):
        self.visited = visit

# Converts string of neighbors to list of nodes.
def findConnections(node, nodes):
    neighbors = node.getConnections()
    finalList = []
    
    # e.g for 1 0 0, nodes[0] is appended to finalList.
    for iter in range(len(neighbors)):
        if neighbors[iter] == "1":
            finalList.append(nodes[iter])
    
    node.setConnections(finalList)

# Sets all nodes to not visited.
def noneVisited(nodes):
    for iter in range(len(nodes)):
        nodes[iter].setVisited(False)

# Outputs number of cycles and longest cycle in graph.
def countCycles(node, parent):
    global cycles
    global longest
    global longer

    node.setVisited(True)
    neighbors = node.getConnections()
    
    # Recursively iterates through each node's neighbors.
    # Longer keeps track of how many nodes are visited before a
    # cycle is tripped (neighbor has been visited before and is not node's parent).
    # Longest == Longer if Longer > Longest, Longer is trimmed to actual start of cycle before checking.
    for iter in range(len(neighbors)):
        if neighbors[iter].isVisited() == False:
            longer.append(node.getNumber())
            countCycles(neighbors[iter], node)

        elif parent.getNumber() != neighbors[iter].getNumber():
            cycles += 1
            longer.append(node.getNumber())
            
            # This check prevents errors when longer is empty.
            if neighbors[iter].getNumber() in longer:
                num = longer.index(neighbors[iter].getNumber())
                temp = longer[num:]
                if len(temp) > len(longest):
                    longest = temp
            longer = []

# Outputs number of layers in graph.
def countLayers(node):
    global layers
    
    # Queue is used to iterate through the tree with BFS.
    node.setVisited(True)
    queue = []
    queue.append(node)

    # QueueTwo is used to keep track of which nodes have appeared in Queue.
    queueTwo = []
    num = 0

    while queue:
        # If there's any nodes in the Queue that have been seen,
        # Queue2 will know and increase num to avoid counting a new layer.
        for iter in range(len(queue)):
            if queueTwo.count(queue[iter]) > 0:
                num += 1

        # Otherwise if everything in the Queue is new,
        # QueueTwo appends the Queue's contents to itself and layers += 1.
        if num == 0:
            for iter in range(len(queue)):
                queueTwo.append(queue[iter])
            layers += 1
        num = 0

        # Iterates through neighbors and appends the unvisited.
        neighbors = queue[0].getConnections()
        queue.pop(0)
        
        for iter in range(len(neighbors)):
            if neighbors[iter].isVisited() == False:
                neighbors[iter].setVisited(True)
                queue.append(neighbors[iter])


def main():
    # Reads data from the given file
    # splitlines() turns raw data into a list of strings.
    # e.g 0 1 1 becomes ['0 1 1']
    with open('input2.txt', 'r') as file:
        data = file.read()
        actualData = data.splitlines()
        
    # split() removes whitespace in strings.
    # e.g '0 1 1' becomes ['0','1','1']
    for iter in range(len(actualData)):
        actualData[iter] = actualData[iter].split()

    # Creates list of nodes using the Node class.
    nodes = []
    for iter in range(len(actualData)):
        nodes.append(Node(str(iter+1), actualData[iter], False))
    
    # findConnections() uses prior string list of connections
    # then converts it to an object list of the actual nodes.
    # e.g ['0','1','1'] is converted to object list [Node 2, Node 3]
    for iter in range(len(nodes)):
        findConnections(nodes[iter], nodes)

    # Objective 1: Count total cycles in graph.
    noneVisited(nodes)
    global cycles

    countCycles(nodes[0], nodes[0])
    print("Number of cycles:", int(cycles/2))

    # Objective 2: Output longest cycle in graph.   
    global longest

    print("Longest Cycle:", len(longest), "nodes |", longest)

    # Objective 3: Count total layers in graph.
    noneVisited(nodes)
    global layers

    countLayers(nodes[0])
    print("Number of layers in the graph:", layers - 1)

main()