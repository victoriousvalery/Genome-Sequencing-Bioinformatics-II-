"""DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.
     Input: A collection of k-mers Patterns.
     Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns)."""
# Some parts of the code may seem irrational, but these are requirements. 
import collections
with open('debruijn_kmers_in.txt') as input_data:
    kmers = input_data.read().strip()
kmer_list = []
for elem in kmers.split('\n'):
    length_of_kmer = len(elem)
    kmer_list.append(elem)

unique_kmers = set()
for elem in kmer_list:
    unique_kmers.add(elem[0:length_of_kmer-1])
    unique_kmers.add(elem[1:length_of_kmer])
unique_kmers = list(unique_kmers)
unique_kmers.sort()
graph = {node:[] for node in unique_kmers}
for elem in kmer_list:
    s = elem[0:length_of_kmer-1]
    t = elem[1:length_of_kmer]
    graph[s].append(t)

graph = collections.OrderedDict(sorted(graph.items()))

elements = list(graph.items())
with open('debruijn_kmers_out.txt', 'w') as o:
    for k, item in enumerate(graph):
        if graph[item]:
            o.write(elements[k][0])
            o.write(" -> ")
            s = len(graph[item])
            count = 0
            for elem in graph[item]:
                count += 1
                if count < s:
                    o.write(elem + ",")
                else:
                    o.write(elem)
            o.write('\n')