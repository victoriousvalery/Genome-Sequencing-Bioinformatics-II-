""" CODE CHALLENGE: Solve the String Composition Problem.
     Input: An integer k and a string Text.
     Output: Composition_k(Text) (the k-mers can be provided in any order). """

with open('string_comp_in.txt') as f:
    k = f.readline()
    text = f.read()
k = int(k)
k_mers = []

for i in range(len(text)-k+1):  # just iterate taking a slice, len(text)-k+1 steps are required
    k_mers.append(text[i:i+k])

with open('string_comp_out.txt', 'w') as out:
    for item in k_mers:
        out.write(''.join(map(str, item)))
        out.write('\n')