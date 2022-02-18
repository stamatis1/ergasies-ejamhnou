total_words = ''
with open("Tale of two cities.txt") as fileobj:
   for line in fileobj:
        for ch in line:
            ordValue = bin(ord(ch))[2:]
           
            if ord(ch) < 2:
                ordValue = "000000" + ordValue
            elif ord(ch) < 4:
                ordValue = "00000" + ordValue
            elif ord(ch) < 8:
                ordValue = "0000" + ordValue
            elif ord(ch) < 16:
                ordValue = "000" + ordValue
            elif ord(ch) < 32:
                ordValue = "00" + ordValue
            elif ord(ch) < 64:
                ordValue = "0" + ordValue   
            total_words = total_words + ordValue



max_continious_zeros = 0
max_continious_ones = 0
continious_zeros = 0
continious_ones = 0


for letter in total_words:
    if letter == '0':
        continious_ones = 0
        continious_zeros = continious_zeros + 1
        if continious_zeros > max_continious_zeros:
            max_continious_zeros = continious_zeros
    elif letter == '1':
        continious_zeros = 0
        continious_ones = continious_ones + 1
        if continious_ones > max_continious_ones:
            max_continious_ones = continious_ones


print(max_continious_zeros)
print(max_continious_ones)
