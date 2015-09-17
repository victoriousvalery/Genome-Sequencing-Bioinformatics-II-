"""CODE CHALLENGE: Solve the Overlap Graph Problem (restated below).
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list."""
def suffix(kmer):
    return kmer[1:len(kmer)]

def prefix(kmer):
    return kmer[0:len(kmer)-1]

with open('graph_overlap_in.txt') as f:
    kmers = f.read()

kmers = kmers.split('\n')
graph = {node:[] for node in kmers}
for edge1 in kmers:
    for edge2 in kmers:
        if suffix(edge1) == prefix(edge2):
            graph[edge1].append(edge2)

graph = collections.OrderedDict(sorted(graph.items()))
elements = list(graph.items())

with open('graph_overlap_out.txt', 'w') as o:
    for k, item in enumerate(graph):
        if graph[item]:
            o.write(elements[k][0])
            o.write(" -> ")
            o.write(*graph.get(item))
            o.write('\n')
