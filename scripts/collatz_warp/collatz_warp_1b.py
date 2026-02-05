import math
import sys

def collatz_stream(n):
    """Yields the next number in the Collatz sequence indefinitely."""
    curr = n
    yield curr
    while True:
        if curr == 1:
            # When we hit 1, we 're-seed' to keep the chain alive for 1B digits
            # We use a math-based shift to keep it non-periodic
            n = (n + 1) * 31337 % 10**12 
            curr = n
        elif curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
        yield curr

def generate_warped_digits(seed_n, target_count):
    """Generates and writes digits directly to disk."""
    collatz = collatz_stream(seed_n)
    
    print(f"Generating {target_count:,} digits...")
    
    with open("collatz_warped_output_50_billion.txt", "w") as f:
        written = 0
        for i, val in enumerate(collatz):
            # --- YOUR WARP LOGIC ---
            # Instead of a high-precision sum, we use the 'Warp' to 
            # extract specific digits from the chaotic interaction.
            mod_offset = i % 7
            # We use log and sin to extract a 'shuffled' digit from the value
            pressure = math.log(i + 2)
            # This is the 'Sweet Spot' calculation:
            raw_val = (val + mod_offset) / pressure
            
            # Extract the 5th, 6th, and 7th decimal places as our digits
            # This avoids the 'stable digit' problem of converging sums
            digit_str = f"{raw_val:.15f}".split('.')[1][5:8]
            
            f.write(digit_str)
            written += len(digit_str)
            
            # Progress reporting
            if i % 1_000_000 == 0:
                percent = (written / target_count) * 100
                sys.stdout.write(f"\rProgress: {written:,} / {target_count:,} ({percent:.2f}%)")
                sys.stdout.flush()
                f.flush() # Force write to disk to save RAM
            
            if written >= target_count:
                break

    print(f"\nSuccess! File saved as collatz_warped_output_1_billion.txt")

if __name__ == "__main__":
    # 1 Billion digits
    generate_warped_digits(seed_n=27, target_count=50_000_000_000)