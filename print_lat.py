# Assuming n is the number of bits in the S-box input/output
n = 4  # Example value, adjust according to your specific S-box

# Initialize the LAT with zeros
LAT = [[0 for _ in range(2**n)] for _ in range(2**n)]

# Example S-box (replace this with your actual S-box)
S=[0xc, 0x6, 0x9, 0x0 ,0x1, 0xa, 0x2, 0xb, 0x3, 0x8, 0x5, 0xd, 0x4, 0xe, 0x7, 0xf]

# Function to calculate the parity (XOR of all bits)
def parity(bits):
    result = 0
    while bits:
        result ^= bits & 1
        bits >>= 1
    return result

# Populate the LAT
for alpha in range(2**n):
    for beta in range(2**n):
        for x in range(2**n):
            u = alpha * x
            v = beta * S[x]
            if parity(u) == parity(v):
                LAT[alpha][beta] += 1
        LAT[alpha][beta] -= 2**(n-1)

# Print the LAT (optional)
for row in LAT:
    print(row)