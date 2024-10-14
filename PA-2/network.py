from collections import defaultdict
import time

class Network:
    
    # Constructor using defaultdict.
    def __init__(self):

	    self.graph = defaultdict(list)
  

	
	# Function to add an edge to graph.
    def addEdge(self, u, v):
	    self.graph[u].append(v)
    
    ########################################################################
    # BFS function
    #
    # @param s: source node
    # @param t: target node
    #######################################################################
    def BFS(self, s, t):
        start = time.monotonic_ns()
        visited = [False] * (max(self.graph) + 1)
 
        queue = []
 
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            s = queue.pop(0)
            print(s, end=" ")
            
            # If target node, stop time and return.
            if s == t:
                end = time.monotonic_ns()
                print("\n\n--- %s ns ---" % (end - start))
                print("--- %.6f ms ---\n" % ((end - start) / 1000000))
                return
 
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    
    ########################################################################
    # DFSHelper function
    #
    # @param s: source node
    # @param t: target node
    # @param visited: set of visited nodes
    #######################################################################
    def DFSHelper(self, v, t, visited):
        if t in visited:
            return
        # Mark the current node as visited + print
        visited.add(v)
        print(v, end=' ')
        
        # Explore adjacent vertices.
        for neighbor in self.graph[v]:
            if neighbor == t:
                visited.add(t)
                print(neighbor, end=' ')
                return 
            elif neighbor not in visited:
                self.DFSHelper(neighbor, t, visited)
 
    
    ########################################################################
    # DFS Function
    #
    # @param s: source node
    # @param t: target node
    #######################################################################
    def DFS(self, v, t):
        start = time.monotonic_ns()
        
        # visited vertices as a set.
        visited = set()
 
        # Call the recursive helper function.
        self.DFSHelper(v, t, visited)
        
        end = time.monotonic_ns()
        print("\n\n--- %s ns ---" % (end - start))
        print("--- %.6f ms ---\n" % ((end - start) / 1000000))
        
    ########################################################################
    # ReadFile function
    #
    # @param : filename is the name of the file to be read.
    #######################################################################  
    def ReadFile(self, filename):
        f = open(filename, 'r')
        for line in f:
            # split the line into a list of strings.
            fname = line.rstrip().split(',')

            # seperate the vertices, convert to integers.
            fname[0] = int((fname[0].split('N_')).pop(-1))
            fname[1] = int((fname[1].split('N_')).pop(-1))
            
            #add edges to graph.
            self.addEdge(fname[0], fname[1])



if __name__ == '__main__':
 
    g = Network()
    
    
    g.ReadFile("Test_Case_Assignment2.txt")
    for i in range(1, 25):
        print("*** FROM N_0 TO N_%s ***\n" % i)
        print("DFS:\n")
        g.DFS(0, i)
        print("BFS:\n")
        g.BFS(0,i)
    

    
    
        
        
    
