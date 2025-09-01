def merge_the_tools(string, k):
    # your code goes here
    start = 0
    end = k
    while end <= len(string):
        # do some stuff here
        temp =string[start:end]
        chunk = list(set(list(temp)))
        print(''.join(chunk))
        start += k
        end += k


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)