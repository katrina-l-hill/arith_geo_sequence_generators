from app import arithmetic_sequence, geometric_sequence

# Normal test cases

def test_arithmetic_sequence():
    # Test Case 1: Arithmetic Sequence with Positive Numbers
    first_term = 1
    common_diff = 2
    num_terms = 5
    expected_sequence = [1, 3, 5, 7, 9]
    expected_sum = 25
    sequence = arithmetic_sequence(first_term, common_diff, num_terms)
    assert sequence == expected_sequence, f"Expected {expected_sequence}, but got {sequence}"
    assert sum(sequence) == expected_sum, f"Expected sum {expected_sum}, but got {sum(sequence)}"

def test_geometric_sequence():
    # Test Case 2: Geometric Sequence with Positive Numbers
    first_term = 2
    common_ratio = 3
    num_terms = 4
    expected_sequence = [2, 6, 18, 54]
    expected_product = 2 * 6 * 18 * 54
    sequence = geometric_sequence(first_term, common_ratio, num_terms)
    assert sequence == expected_sequence, f"Expected {expected_sequence}, but got {sequence}"
    product = 1
    for num in sequence:
        product *= num
    assert product == expected_product, f"Expected product {expected_product}, but got {product}"

def test_arithmetic_sequence_negative_diff():
    # Test Case 3: Arithmetic Sequence with Negative Common Difference
    first_term = 10
    common_diff = -2
    num_terms = 6
    expected_sequence = [10, 8, 6, 4, 2, 0]
    expected_sum = 30
    sequence = arithmetic_sequence(first_term, common_diff, num_terms)
    assert sequence == expected_sequence, f"Expected {expected_sequence}, but got {sequence}"
    assert sum(sequence) == expected_sum, f"Expected sum {expected_sum}, but got {sum(sequence)}"

# Edge test cases

def test_single_term_arithmetic_sequence():
    # Edge Case 1: Single Term Arithmetic Sequence
    first_term = 5
    common_diff = 3
    num_terms = 1
    expected_sequence = [5]
    expected_sum = 5
    sequence = arithmetic_sequence(first_term, common_diff, num_terms)
    assert sequence == expected_sequence, f"Expected {expected_sequence}, but got {sequence}"
    assert sum(sequence) == expected_sum, f"Expected sum {expected_sum}, but got {sum(sequence)}"

def test_single_term_geometric_sequence():
    # Edge Case 2: Single Term Geometric Sequence
    first_term = 7
    common_ratio = 2
    num_terms = 1
    expected_sequence = [7]
    expected_product = 7
    sequence = geometric_sequence(first_term, common_ratio, num_terms)
    assert sequence == expected_sequence, f"Expected {expected_sequence}, but got {sequence}"
    product = 1
    for num in sequence:
        product *= num
    assert product == expected_product, f"Expected product {expected_product}, but got {product}"

def test_geometric_sequence_ratio_one():
    # Edge Case 3: Geometric Sequence with Common Ratio of 1
    first_term = 4
    common_ratio = 1
    num_terms = 5
    expected_sequence = [4, 4, 4, 4, 4]
    expected_product = 4 ** 5
    sequence = geometric_sequence(first_term, common_ratio, num_terms)
    assert sequence == expected_sequence, f"Expected {expected_sequence}, but got {sequence}"
    product = 1
    for num in sequence:
        product *= num
    assert product == expected_product, f"Expected product {expected_product}, but got {product}"