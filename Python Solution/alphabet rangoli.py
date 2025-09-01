# size = 3
# alphabet = [chr(i) for i in range(97,123)]
# alphabet = alphabet[:size]
# print(alphabet)
# indices = list(range(size))
# print(indices)
# index = indices[:-1] + indices[::-1]
# print(index)



def print_rangoli(size):
    alphabet = [chr(i) for i in range(97,123)]
    alphabet = alphabet[:size]
    indices = list(range(size))
    index = indices[:-1] + indices[::-1]
    # your code goes here
    for i in index:
        start_index = i + 1
        original = alphabet[-start_index:]
        reverse = original[::-1]
        row = reverse + original[1:]
        row = "-".join(row)
        width = size*4 - 3
        row = row.center(width,"-")
        print(row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)