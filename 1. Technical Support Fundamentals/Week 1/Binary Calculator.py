# Input
print(" ")
input_num = int(input('Enter the Number (Max=128): '))

def binary_calculator(num):
    # Convert input number into binary
    binary = bin(num)[2:]

    # Add leading zeros if necessary
    binary = binary.zfill(8)

    # Count number of each binary digit
    count_128 = binary.count('1', 0, 1)
    count_64 = binary.count('1', 1, 2)
    count_32 = binary.count('1', 2, 3)
    count_16 = binary.count('1', 3, 4)
    count_8 = binary.count('1', 4, 5)
    count_4 = binary.count('1', 5, 6)
    count_2 = binary.count('1', 6, 7)
    count_1 = binary.count('1', 7, 8)

    # Print results
    print(" ")
    print(f"Binary: {binary}")
    print(" ")
    print(f"128s: {count_128}")
    print(f"64s: {count_64}")
    print(f"32s: {count_32}")
    print(f"16s: {count_16}")
    print(f"8s: {count_8}")
    print(f"4s: {count_4}")
    print(f"2s: {count_2}")
    print(f"1s: {count_1}")
    print(" ")


# Test the function
binary_calculator(input_num)
