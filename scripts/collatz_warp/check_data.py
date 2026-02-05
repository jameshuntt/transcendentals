import math
from collections import Counter

def analyze_sequence(file_path):
    with open(file_path, 'r') as f:
        # Load the sequence and filter to only digits
        data = f.read()
        digits = [d for d in data if d.isdigit()]
    
    total_count = len(digits)
    if total_count == 0:
        return "No digits found in file."

    # 1. Frequency Analysis
    counts = Counter(digits)
    print(f"--- Global Frequency Analysis (Total: {total_count:,} digits) ---")
    for i in range(10):
        digit = str(i)
        count = counts.get(digit, 0)
        percentage = (count / total_count) * 100
        print(f"Digit {digit}: {count:,} ({percentage:.2f}%)")

    # 2. Shannon Entropy Calculation
    # Formula: H = -sum(p * log2(p))
    entropy = 0
    for i in range(10):
        p = counts.get(str(i), 0) / total_count
        if p > 0:
            entropy -= p * math.log2(p)
    
    max_entropy = math.log2(10) # ~3.3219 bits for base-10
    efficiency = (entropy / max_entropy) * 100
    print(f"\n--- Entropy ---")
    print(f"Shannon Entropy: {entropy:.4f} bits/digit")
    print(f"Randomness Efficiency: {efficiency:.2f}%")

    # 3. Pattern Check: Quads (e.g., 5555)
    quads = 0
    for i in range(len(digits) - 3):
        if digits[i] == digits[i+1] == digits[i+2] == digits[i+3]:
            quads += 1
    print(f"\n--- Pattern Check ---")
    print(f"Quad Repeats (e.g., '1111'): {quads}")

    # 4. Longest Repeating Substring (simplified for performance)
    # Checks for the first repeating 7-digit block
    seen_patterns = {}
    longest_repeat = 0
    pattern_length = 7
    for i in range(len(digits) - pattern_length):
        pattern = "".join(digits[i:i+pattern_length])
        if pattern in seen_patterns:
            print(f"Found repeating {pattern_length}-digit block: {pattern}")
            break
        seen_patterns[pattern] = i

# Run the analysis
analyze_sequence('collatz_warp_output.txt')