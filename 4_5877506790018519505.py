############# Here's the Python code to accomplish each of the tasks step by step:

## 1. Encryption:

def encrypt(M, e, n):
    """Encrypt plaintext M using RSA encryption."""
    return pow(M, e, n)


# Given values
M = 10172213
e = 13
n = 25399259

# Step 1: Encryption
C = encrypt(M, e, n)
print("Step 1: Encryption")
print("Ciphertext C:", C)


## 2. Decryption:

def decrypt(C, d, n):
    """Decrypt ciphertext C using RSA decryption."""
    return pow(C, d, n)


# Given value of d (private exponent)
d = 93791797

# Step 2: Decryption
M_decrypted = decrypt(C, d, n)
print("\nStep 2: Decryption")
print("Decrypted plaintext M:", M_decrypted)


## 3. **Decode "C" using the given coding table:

def decode_C(C, coding_table):
    """Decode ciphertext C using the given coding table."""
    C_str = str(C)
    decoded_text = ""
    for i in range(0, len(C_str), 2):
        code = int(C_str[i:i + 2])
        if code in coding_table:
            decoded_text += coding_table[code]
        else:
            decoded_text += "<placeholder>"  # Placeholder for missing characters in coding table
    return decoded_text


# Given coding table
coding_table = {
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J',
    20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W',
    33: 'X', 34: 'Y', 35: 'Z'
}

# Step 3: Decode C using the given coding table
decoded_text = decode_C(C, coding_table)
print("\nStep 3: Decoded text from C:")
print(decoded_text)


## 4. Write a program to convert exponents into binary:

def convert_to_binary(n):
    """Convert integer n to binary."""
    return bin(n)[2:]


# Given exponents e and d
e = 13
d = 93791797

# Step 4: Convert exponents e and d to binary
e_binary = convert_to_binary(e)
d_binary = convert_to_binary(d)
print("\nStep 4: Binary representation of exponents:")
print("Exponent e (binary):", e_binary)
print("Exponent d (binary):", d_binary)


## 5. Find bits representing the exponent "b" and the number of bits "k":

def find_exponent_bits(b):
    """Find bits representing the exponent 'b' and the number of bits 'k'."""
    bb = []  # Initialize array to store binary bits
    i = 0
    k = 0

    while b > 0:
        k = i
        bb.append(b % 2)  # Remainder when dividing by 2
        b = b // 2  # Integer division
        i += 1

    return bb[::-1], k  # Reverse the array to have the least significant bit first


# Given value of b
b = 10172213

# Step 5: Find bits representing the exponent "b" and the number of bits "k"
b_bits, k = find_exponent_bits(b)
print("\nStep 5: Bits representing the exponent 'b' and the number of bits 'k':")
print("Binary bits of exponent b:", b_bits)
print("Number of bits k:", k)

# Given values
e = 13
d = 93791797
n = 25399259

# Plaintext to be encrypted
M = 10172213

# Step 6: Encryption using the public key {e, n}
C = encrypt(M, e, n)
print("Step 1: Encryption")
print("Ciphertext C:", C)

# Step 2: Decryption using the private key {d, n}
M_decrypted = decrypt(C, d, n)
print("\nStep 2: Decryption")
print("Decrypted plaintext M:", M_decrypted)
