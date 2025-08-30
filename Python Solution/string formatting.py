# number = 22
# desi=str(number)
# print(desi)
# octal = oct(number)[2:]
# print(octal)
# hexa = hex(number)[2:]
# print(hexa.upper())
# binary = bin(number)[2:]
# print(binary)
# width = len(bin(number)[2:])
# print(width)
# print(desi.rjust(width), octal.rjust(width), hexa.rjust(width), binary.rjust(width))


def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1,number + 1):
        desi = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(desi.rjust(width), octal.rjust(width), hexa.rjust(width), binary.rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
