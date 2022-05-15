#
# Ford and Fulkerson Algorithm implemented in Python.
#

class Edge(object):
    def __init__(self, source, sink, capacity):
        self.source = source
        self. sink = sink
        self.capacity = capacity

    def __repr__(self):
        return "%s -> %s : %d" % (self.source, self.sink, self.capacity)


class Flow(object):

    def __init__(self):
        self.edges = {}
        self.adjacents = {}

    def add_edges(self, source, sink, capacity):
        if source == sink:
            raise ValueError("Source can not be the Sink.")
        edge = Edge(source, sink, capacity)
        redge = Edge(source, sink, capacity)
        self.edges[edge] = 0
        self.edges[redge] = 0

        if source not in self.adjacents:
            self.adjacents[source] = []
        if sink not in self.adjacents:
            self.adjacents[sink] = []

        self.adjacents[source].append(edge)
        self.adjacents[sink].append(redge)

    def valid_path(self, source, sink, path):
        """ Returns the list of the edges from source to sink """

        if source == sink:
            return path
        for edge in self.adjacents[source]:
            if edge not in path:
                if edge.capacity - self.edges[edge] > 0:
                    return self.valid_path(edge.sink, sink, path + [edge])

        # In case there is no more possible path:
        return None

    def max_flow(self, source, sink):
        """" Update the flow for edges and returns the max_flow """

        path = self.valid_path(source, sink, [])

        while (path):
            # get the maximum possible flow that can be taken from this path:
            max_flow = min([edge.capacity for edge in path])
            for edge in path:
                self.edges[edge] += max_flow
            path = self.valid_path(source, sink, [])

        # Compute all the flows from the neighbors of source:
        return sum([self.edges[edge] for edge in self.adjacents[source]])


t = Flow()
n = int(input("Enter the number of vertices: "))
for i in range(n):
    for j in range(n):
        if i != j:
            flow = int(
                input(f"Enter the flow between vertex {i} and vertex {j}: "))
            source = str(i)
            sink = str(j)
            t.add_edges(source, sink, flow)
# t.add_edges('s', 'o', 3)
# t.add_edges('s', 'p', 3)
# t.add_edges('o', 'p', 2)
# t.add_edges('o', 'q', 3)
# t.add_edges('p', 'r', 2)
# t.add_edges('q', 'r', 4)
# t.add_edges('r', 't', 3)
# t.add_edges('q', 't', 2)

print(0, t.max_flow('0', '5'))

# 6
# 16
# 13
# 0
# 0
# 0
# 0
# 10
# 12
# 0
# 0
# 0
# 4
# 0
# 14
# 0
# 0
# 0
# 9
# 0
# 20
# 0
# 0
# 0
# 7
# 4
# 0
# 0
# 0
# 0
# 0
