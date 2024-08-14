# exercices-leetcode

This repository contains my solutions to various LeetCode exercises. The exercises are classified by difficulty level into three main categories:

- **Easy**
- **Medium**
- **Hard**

Each exercise is organized into its own folder under the corresponding difficulty level, containing the solution code, test cases, and a README file describing the solution.

## Project Structure

Each exercise will have the following sub-structure:

```plaintext
│   ├── solution.py       # The Python code implementing the solution
│   ├── test.py           # The test cases to validate the solution
│   └── README.md         # A description of the problem, solution, and complexity analysis
```

## Setting Up the Project

To work with this repository, follow these instructions:

### 1. Create a Virtual Environment

It is recommended to use a virtual environment to keep dependencies isolated. You can create a virtual environment using the following commands:

```bash
python3 -m venv venv
```

This will create a virtual environment named `venv` in your project directory.

### 2. Activate the Virtual Environment

Activate the virtual environment using the command specific to your operating system:

- **For Windows:**

    ```bash
    .\venv\Scripts\activate
    ```

- **For macOS/Linux:**

    ```bash
    source venv/bin/activate
    ```

### 3. Install Requirements

Once the virtual environment is activated, install the dependencies listed in `requirements.txt`:

```bash
pip3 install -r requirements.txt
```

This will install all the necessary packages, including `pytest` for running tests.

### 4. Run the Tests

To validate your solutions, you can run the test cases using `pytest`. Navigate to the directory containing the test file and run:

```bash
pytest test.py
```

This command will search for all `test.py` files in the project and run the tests.

## Explore the Solutions

Feel free to explore the solutions, analyze the code, and run the tests. 

Suggestions are always welcome!