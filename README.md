# Linear Algebra Toolkit

## Introduction

Linear Algebra Toolkit is a Python-based project that performs basic vector and matrix operations. It also helps users solve systems of linear equations.

This project is developed using Python and NumPy. It provides a simple menu-based interface where users can select an operation, enter values, and view the results.

## Features

### 1. Vector Operations
- Vector Addition
- Vector Subtraction
- Vector Dot Product
- Vector Magnitude
- Vector Normalization

### 2. Matrix Operations
- Matrix Addition
- Matrix Subtraction
- Matrix Multiplication
- Matrix Transpose
- Matrix Determinant
- Matrix Inverse

### 3. Linear Equations
- Solve systems of linear equations using matrices.

### 4. Input Validation
- Checks invalid numeric inputs.
- Checks vector and matrix dimensions.
- Prevents operations on incompatible inputs.
- Handles zero-vector normalization.
- Checks singular matrices before inverse and equation operations.

### 5. Save Results
The project saves operation results in text files inside the `output` folder.

## Technologies Used

- Python
- NumPy
- Unit Testing (unittest)

## Project Structure

```text
Linear-Algebra-Toolkit/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── output/
│   ├── vector_results.txt
│   ├── matrix_results.txt
│   └── equation_solution.txt
│
└── tests/
    └── test_analysis.py
```

## Installation

**Step 1: Clone the repository**

```bash
git clone https://github.com/JS-JUNAIDSALEEM/Linear-Algebra-Toolkit.git
```

**Step 2: Open the project folder**

```bash
cd Linear-Algebra-Toolkit
```

**Step 3: Install the required library**

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command in the terminal:

```bash
python main.py
```

The project will display a menu:

```text
1. Vector Operations
2. Matrix Operations
3. Solve Linear Equations
4. Exit
```

Select an option and enter the required values to perform an operation.

## Running Unit Tests

This project includes unit tests to check the main functions and their results.

The test file is located inside the `tests` folder.

Run the following command from the project root:

```bash
py -m unittest discover -s tests -v
```

The test file currently contains **24 test cases** covering:

- Vector operations
- Matrix operations
- Linear equation solving
- Invalid inputs
- Dimension checking
- Singular matrix handling

*Note: Test results should be verified by running the command locally.*

## Output

The project saves results in the `output` folder.

- `vector_results.txt` – Stores vector operation results.
- `matrix_results.txt` – Stores matrix operation results.
- `equation_solution.txt` – Stores solutions of linear equations.

## Learning Objectives

Through this project, I practiced:

- Working with Python functions.
- Using NumPy for mathematical operations.
- Understanding vectors and matrices.
- Applying input validation.
- Handling errors and invalid inputs.
- Saving results in text files.
- Writing unit tests using Python unittest.

## Author

### Junaid Saleem

- **GitHub:** [JS-JUNAIDSALEEM](https://github.com/JS-JUNAIDSALEEM)
- **LinkedIn:** [Junaid Saleem](https://www.linkedin.com/in/junaid-saleem-developer/)
