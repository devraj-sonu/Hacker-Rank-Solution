size = 3
alphabet = [chr(i) for i in range(64,123)]
print(alphabet)
indices = list(range(size))
print(indices)
index = indices[:-1] + indices[::-1]
print(index)