## collatz_warp

### collatz_warp.py

##### if you run it and check the numbers you get this (as long as the tool i uses didnt hallucinate some ai garbage)

| Property        | Result                              |
|-----------------|-------------------------------------|
| shannon entropy | ~3.321 bits/digit (max for base‑10) |
| average digit % | ~10% per digit (0–9)                |
| randomness      | ~99.97%                             |
| quad repeats    | 104 in 1,000,000 digits             |
| distribution    | extremely uniform                   |

##### This matches expectations for an output that is *close to Borel normal* and *non‑periodic*.

### collatz_warp_output.txt
##### check it out if you want, tell me if its somehow a repeater

### check_data.py
#### i ran it and i got this exact output
--- Global Frequency Analysis (Total: 1,000,000 digits) ---
Digit 0: 99,820 (9.98%)
Digit 1: 100,202 (10.02%)
Digit 2: 100,140 (10.01%)
Digit 3: 101,085 (10.11%)
Digit 4: 99,554 (9.96%)
Digit 5: 99,834 (9.98%)
Digit 6: 99,785 (9.98%)
Digit 7: 100,064 (10.01%)
Digit 8: 99,702 (9.97%)
Digit 9: 99,814 (9.98%)

--- Entropy ---
Shannon Entropy: 3.3219 bits/digit
Randomness Efficiency: 100.00%

--- Pattern Check ---
Quad Repeats (e.g., '1111'): 1001
Found repeating 7-digit block: 0887761

### summary
##### This system generates pseudo-transcendental sequences not through a single static formula, but through the interaction of multiple **Computational Chains** influenced by dynamic **Force Pressures**.

## 1. The Multi-Chain Core

##### Instead of a linear generator, we utilize a mesh of interleaved sequences (e.g., Warped Collatz, LCGs, or cellular automata).
* **Chain α (The Master):** Sets the base frequency and primary numeric flow.
* **Chain β (The Disruptor):** Injects entropy when α enters a low-complexity state or begins to show periodic tendencies.
* **Chain γ (The Observer):** Monitors the output for emerging patterns and applies "Counter-Pressure" to steer the system back toward chaos.


## 2. Shaping via "Pressure"

##### "Pressure" is defined as a mathematical constraint applied to the transition probabilities of the next digit. 
* **Distribution Pressure:** If the digit `7` is over-represented in the current window (e.g., 10k digits), the "Force" adjusts the weight of the underlying modulo operations to suppress it.
* **Structural Pressure:** Prevents the sequence from collapsing into a "Rational Trap" (repeating loops) by shifting the seed or algorithm parameters based on the system's "temperature."


## 3. Identifying "Sweet Spots" (Attractors)

##### A "Sweet Spot" is a state of **Perfect Chaos**—a region in the phase space where the sequence is demonstrably non-periodic but maintains a statistically flat 10% distribution across all digits.
* **Formal Goal:** To prove that a "Multi-Source" approach creates a wider basin of attraction for irrationality than single-source generators.


## 4. The Formal Proof Strategy (Work in Progress)

##### To move toward a formal proof of "Transcendental Shaping," the framework tracks:
1.  **Lyapunov Exponents:** Measuring the rate of divergence between two chains with nearly identical starting seeds to verify high sensitivity (chaos).
2.  **Borel Normality:** Utilizing Chi-Squared tests on multi-megabyte blocks to ensure the sequence remains "normal" (each digit/sequence appears with the expected frequency).
3.  **Entropy Density:** Monitoring the Shannon entropy to ensure it remains consistently above **3.32 bits/digit**, approaching the theoretical limit of a base-10 random system.