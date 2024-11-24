# Creating Arithmetic and Geometric Sequence Generators

## Author: Katrina Hill

### Description
This Python program generates either an arithmetic sequence or a geometric sequence based on user input. It calculates the terms of the sequence and provides additional results, such as the sum of an arithmetic sequence or the product of a geometric sequence.

### Features
- Arithmetic Sequence: Generate a sequence with a constant difference between consecutive terms.
- Geometric Sequence: Generate a sequence where each term is multiplied by a constant ratio.
- Additional Calculations:
    - Sum of the arithmetic sequence.
    - Product of the geometric sequence.

### Files
- `app.py`: The main program that performs the sequence generation.
- `tests.py`: The test file to check the funtionality of the application.

### Requiurements
- Python 3.x installed on your machine.

### How to Run
1. **Clone the repository** (or download the files):
   - git clone https://github.com/katrina-l-hill/arith_geo_sequence_generators
   - cd into the repository directory
2. **Run the Main program**:
   - run python `app.py` to run the program
   - the first prompt will be to enter 'A' for Arithmetic sequence or 'G' for Geometric sequence
     - press enter after entering the letter
   - the second prompt will be to enter the first term
     - press enter after entering the number
   - the third prompt will be to enter the number of terms
     - press enter after entering the number
   - the fourth prompt will be to either enter the common difference (Arithmetic) or enter the common ratio (Geometric)
     - press enter after entering the number
3. **Run the tests**:
   - run `python -m pytest tests.py` to run the tests