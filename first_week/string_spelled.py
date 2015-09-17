"""String Spelled by a Genome Path Problem. Reconstruct a string from its genome path.
     Input: A sequence of k-mers Pattern_1, … ,Pattern_n such that the last k - 1 symbols of Patterni are
                equal to the first k-1 symbols of Pattern_i+1 for 1 ≤ i ≤ n-1.
     Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni  (for 1 ≤ i ≤ n)"""

with open('string_spelled_in.txt') as f:
    k_mers = f.read()

k_mers_parsed = []

for i in k_mers.split('\n'):
    k_mers_parsed.append(i)
genome = k_mers_parsed[0]
for i in range(1,len(k_mers_parsed)):
    genome = genome + k_mers_parsed[i][-1]
#print(genome)

with open('string_spelled_out.txt', 'w') as out:
    out.write(genome)


