# DNA base pairing: a <-> t, c <-> g

# Define base pair mapping
pair = {
    'a': 't',
    't': 'a',
    'c': 'g',
    'g': 'c'
}

def get_valid_sequence():
    """Prompt the user until a valid DNA sequence (a, t, g, c) is provided."""
    while True:
        raw = input("Enter a DNA sequence (letters a, t, g, c): ")
        seq = raw.strip().replace(" ", "")
        if not seq:
            print("Empty input. Please enter at least one base (a, t, g, c).")
            continue
        invalid = sorted(set(ch for ch in seq if ch.lower() not in pair))
        if invalid:
            print(f"Invalid characters found: {', '.join(invalid)}. Please use only a, t, g, c.")
            continue
        return seq

def complement_sequence(seq: str) -> str:
    """Return the complementary DNA sequence for the input sequence."""
    # Preserve original letter case: map using lowercase lookup, then
    # convert to uppercase if the original character was uppercase.
    out = []
    for ch in seq:
        base = ch.lower()
        comp = pair[base]
        out.append(comp.upper() if ch.isupper() else comp)
    return ''.join(out)

def main():
    while True:
        seq = get_valid_sequence()
        comp = complement_sequence(seq)
        print(f"Original sequence: {seq}")
        print(f"Complementary sequence: {comp}")

        # Ask the user whether they want to enter another sequence
        while True:
            again = input("Would you like to enter another sequence? (y/n): ").strip().lower()
            if again in ('y', 'yes'):
                break  # outer loop continues
            if again in ('n', 'no', 'q', 'quit'):
                print("Goodbye.")
                return
            print("Please answer 'y' or 'n'.")

if __name__ == '__main__':
    main()

# Notes:
# - Accepts sequences of any length composed of a, t, g, c (spaces ignored).
# - Re-prompts on invalid characters so the user can correct mistakes.