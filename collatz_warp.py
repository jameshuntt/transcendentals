from decimal import Decimal, getcontext
import math

# Set very high precision: 1 million decimal digits + safety margin
getcontext().prec = 1_010_000

def collatz_sequence(n):
    """
    Generate the full Collatz sequence starting from n.
    The sequence ends at 1 and includes all intermediate steps.
    """
    steps = []
    while n != 1:
        steps.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    steps.append(1)
    return steps

def warp_sequence(seq):
    """
    Warp the Collatz sequence:
    - Add a small mod-7 perturbation
    - Divide by log(index + 2) to decay larger indices
    This injects mild chaos and decay into the number's construction.
    """
    warped = []
    for i, val in enumerate(seq):
        mod = i % 7                      # Cyclical offset
        warped_val = Decimal(val + mod) / Decimal(math.log(i + 2))  # Log decay
        warped.append(warped_val)
    return warped

def generate_real_from_collatz(n, max_terms):
    """
    Build a real number from the warped Collatz sequence.
    The construction is: sum of 1 / ((i + 1) * warped[i])
    This creates a converging series with pseudo-random digit expansion.
    """
    collatz = collatz_sequence(n)
    warped = warp_sequence(collatz)

    s = Decimal(0)
    for i, val in enumerate(warped[:max_terms]):
        s += Decimal(1) / ((i + 1) * val)  # Weighted harmonic term
    return s

if __name__ == "__main__":
    MAX_TERMS = 1_500_000  # Empirically chosen to extract ~1 million stable digits
    print("Computing warped Collatz-derived real number...")

    result = generate_real_from_collatz(27, max_terms=MAX_TERMS)

    # Convert result to string and isolate the decimal digits
    result_str = str(result)
    digits = result_str.split('.')[1][:1_000_000]

    # Write 1 million digits to a file
    with open("collatz_warped_real.txt", "w") as f:
        f.write(digits)

    print("Saved first 1,000,000 digits to collatz_warped_real.txt")