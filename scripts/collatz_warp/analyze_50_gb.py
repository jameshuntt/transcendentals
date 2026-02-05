import math
from collections import Counter
import os

def analyze_50gb_file(file_path):
    counts = Counter()
    total_size = os.path.getsize(file_path)
    chunk_size = 1024 * 1024 * 100 # 100MB chunks
    
    print(f"--- Analyzing {total_size / 1e9:.2f} GB File ---")
    
    with open(file_path, 'rb') as f: # Read in binary for speed
        processed = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            
            # Count digits in the byte-stream
            counts.update(chunk.decode('ascii'))
            
            processed += len(chunk)
            percent = (processed / total_size) * 100
            print(f"\rProgress: {processed / 1e9:.2f}GB / {total_size / 1e9:.2f}GB ({percent:.2f}%)", end="")

    total_digits = sum(counts.values())
    print(f"\n\n--- Global Frequency Analysis ---")
    for i in range(10):
        d = str(i)
        print(f"Digit {d}: {counts[d]:,} ({(counts[d]/total_digits)*100:.4f}%)")

    entropy = -sum((count/total_digits) * math.log2(count/total_digits) for count in counts.values() if count > 0)
    print(f"\nShannon Entropy: {entropy:.6f}")
    print(f"Efficiency: {(entropy / math.log2(10)) * 100:.4f}%")

# analyze_50gb_file('collatz_warped_output_1_billion.txt')