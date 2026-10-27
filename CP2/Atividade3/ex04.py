v = [45, -89, 32, -12, 33]

for i in range(len(v)):
    for j in range(i + 1, len(v)):
        if v[i] > v[j]:
            v[i], v[j] = v[j], v[i]

print(v)
