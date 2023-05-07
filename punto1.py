import numpy as np

v = np.zeros(30, dtype=int)
for i in range (5000):
        candi = np.random.randint(0,30)
        v[candi] = v[candi] +1
        
voticosordenados = np.sort(v)[::-1]

for i, voticos in enumerate(voticosordenados):
    print(f"Candidato {i+1}: {voticos} votos")