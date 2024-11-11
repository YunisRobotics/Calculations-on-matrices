
# Matrix Operations Program

A Python program for performing basic operations on two matrices, such as addition, subtraction, and multiplication. The program supports both random matrix generation and manual input of matrix values.

## Features

- **Matrix Creation**: Initialize matrices with custom dimensions, either with random values or by entering values manually.
- **Operations**: Supports addition, subtraction, and multiplication of matrices when dimensions allow.
- **Compatibility Check**: Automatically checks if the matrices are compatible for each operation.

## Getting Started

### Requirements

- Python 3.x
- Basic Python knowledge
- Git installed

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YunisRobotics/Calculations-on-matrices.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Matrix-Operations
   ```

3. Run the program:
   ```bash
   python Matrix_Operations.py
   ```

### Usage Guide

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

Contributions are welcome! Please give feedback to my project or fork the repository and submit a pull request for review.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/YunisRobotics/Calculations-on-matrices/blob/main/LICENSE) file for more details.
