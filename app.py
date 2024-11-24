def arithmetic_sequence(first_term, common_diff, num_terms):
    sequence = []
    for i in range(num_terms):
        sequence.append(first_term + i * common_diff)
    return sequence

def geometric_sequence(first_term, common_ratio, num_terms):
    sequence = []
    for i in range(num_terms):
        sequence.append(first_term * (common_ratio ** i))
    return sequence

def main():
    sequence_type = input("Enter 'A' for Arithmetic sequence or 'G' for Geometric sequence: ").strip().upper()

    first_term = float(input("Enter the first term: "))
    num_terms = int(input("Enter the number of terms: "))

    if sequence_type == 'A':
        common_diff = float(input("Enter the common difference: "))
        sequence = arithmetic_sequence(first_term, common_diff, num_terms)
        sequence_sum = sum(sequence)
        print("Arithmetic sequence:", sequence)
        print("Sum of the sequence:", sequence_sum)
    elif sequence_type == 'G':
        common_ratio = float(input("Enter the common ratio: "))
        sequence = geometric_sequence(first_term, common_ratio, num_terms)
        sequence_product = 1
        for num in sequence:
            sequence_product *= num
        print("Geometric Sequence:", sequence)
        print("Product of the sequence:", sequence_product)
    else:
        print("Invalid input. Please enter 'A' or 'G'.")

if __name__ == "__main__":
    main()