
# Matrix Operations Program

A Python program for performing basic operations on two matrices, such as addition, subtraction, and multiplication. The program supports both random matrix generation and manual input of matrix values.

## Features

- **Matrix Creation**: Initialize matrices with custom dimensions, either with random values or by entering values manually.
- **Operations**: Supports addition, subtraction, and multiplication of matrices when dimensions allow.
- **Compatibility Check**: Automatically verifies if the matrices are compatible for each operation.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/matrix-operations.git
   ```

2. Navigate to the project directory:
   ```bash
   cd matrix-operations
   ```

3. Run the program:
   ```bash
   python matrix_operations.py
   ```

### Usage Instructions

1. Upon running, you’ll be prompted to choose a mode for matrix initialization:

   ```
   Welcome to the Matrix Operations
   Choose your option (1 or 2):
   1: Set randomly
   2: Set manually
   ```

2. **Option 1 (Random Mode)**: Generates two 3x3 matrices with random integers (0-9).

3. **Option 2 (Manual Mode)**: Prompts for the number of rows and columns for each matrix (up to 9x9). Then enter values for each element in both matrices.

## Example Usage

#### Sample Output

```plaintext
Welcome to the Matrix Operations
Choose your option (1 or 2):
1: Set randomly
2: Set manually
> 1

Matrix 1:
[1, 4, 7]
[3, 2, 6]
...

Result of Addition:
...
Result of Subtraction:
...
Result of Multiplication:
...
```

## Matrix Operations Summary

- **Addition/Subtraction**: Possible if both matrices have the same dimensions.
- **Multiplication**: Possible if the columns in matrix 1 equal the rows in matrix 2.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

## License

This project is available under the terms outlined in the LICENSE file.
