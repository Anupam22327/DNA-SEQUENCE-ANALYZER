# DNA Sequence Analysis Tool

def validate_sequence(sequence):
    """Check whether the DNA sequence contains only A, T, G, C."""
    
    valid_bases = {"A", "T", "G", "C"}
    
    return all(base in valid_bases for base in sequence)


def analyze_sequence(sequence):
    """Analyze the DNA sequence."""

    length = len(sequence)

    # Count nucleotides
    A = sequence.count("A")
    T = sequence.count("T") 
    G = sequence.count("G")
    C = sequence.count("C")

    # Calculate percentages
    gc_content = ((G + C) / length) * 100
    at_content = ((A + T) / length) * 100

    # Reverse complement
    complement = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }

    reverse_complement = "".join(
        complement[base] for base in reversed(sequence)
    )

    # Transcription: DNA → RNA
    rna = sequence.replace("T", "U")

    # Display results
    print("\n========== DNA SEQUENCE ANALYSIS ==========")

    print(f"Sequence       : {sequence}")
    print(f"Length         : {length} bp")

    print("\nNucleotide Count")
    print(f"Adenine (A)    : {A}")
    print(f"Thymine (T)    : {T}")
    print(f"Guanine (G)    : {G}")
    print(f"Cytosine (C)   : {C}")

    print("\nComposition")
    print(f"GC Content      : {gc_content:.2f}%")
    print(f"AT Content      : {at_content:.2f}%")

    print("\nReverse Complement")
    print(reverse_complement)

    print("\nTranscription")
    print(rna)

    print("============================================")


# Main program

sequence = input("Enter your DNA sequence: ")

# Remove spaces and convert to uppercase
sequence = sequence.replace(" ", "").upper()

if len(sequence) == 0:
    print("Error: Sequence cannot be empty.")

elif validate_sequence(sequence):
    analyze_sequence(sequence)

else:
    print("Invalid DNA sequence!")
    print("Only A, T, G and C are allowed.")
    