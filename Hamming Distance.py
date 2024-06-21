import math

# def to_binary(num):
#     # Yes, it is slow but it is mine
#     num_of_bits = math.log2(num) // 1 + 1
#
#     binary = []
#     for i in range(1, int(num_of_bits)+1):
#         mod = num % 2**(i)
#
#         if mod != 0:
#             num -= 2**(i-1)
#
#             binary.insert(0, 1)
#         else: binary.insert(0, 0)
#
#     return binary
#
# def to_binary(num):
#     return str(bin(num))[2::]
#
# def hammingDistance(num1, num2):
#     binary1 = to_binary(max(num1, num2))
#     binary2 = to_binary(min(num1, num2))
#
#     if len(binary1) > len(binary2):
#         for i in range(len(binary1) - len(binary2)):
#             binary2.insert(0, 0)
#
#     Hamming_Distance = 0
#     for i, element in enumerate(binary1):
#         if element != binary2[i]:
#             Hamming_Distance += 1
#
#     return Hamming_Distance


def hammingDistance(num1, num2):
    binary1 = str(bin(max(num1, num2)))[2:]
    binary2 = str(bin(min(num1, num2)))[2:]


    if len(binary1) > len(binary2):
        i = len(binary1) - len(binary2)
        binary2 = "0" * i + binary2


    Hamming_Distance = 0
    for i, element in enumerate(binary1):
        if element != binary2[i]:
            Hamming_Distance += 1

    return Hamming_Distance


print(hammingDistance(1, 4))