# Contributing to Python DSA MAANG

First off, thank you for considering contributing to this repository! With over 300 problems, it's a massive undertaking, and community help is greatly appreciated.

## Getting Started

1. **Fork the repository** on GitHub.
2. **Clone your fork** locally.
3. Install the dependencies (we use `pytest` for testing and `black`/`flake8` for formatting):
   ```bash
   pip install -r requirements.txt
   ```

## Adding a New Problem Solution

We have scaffolding ready for all 300 problems! To contribute a solution:

1. **Find an empty template**: Pick any `*_template_problem.py` file in the `topics/` directory that hasn't been solved yet.
2. **Rename the file**: Give it a descriptive name (e.g., rename `015_template_problem.py` to `015_3sum.py`).
3. **Fill in the code**:
   - Write the `solve_brute()` and `solve_optimal()` functions.
   - Include the Time and Space complexity proofs in the top docstring.
4. **Write Tests**: Add your test cases to the `@pytest.mark.parametrize` blocks at the bottom of the file.

### Using the CLI Generator
If you want to add a brand new problem that isn't already scaffolded, use our CLI tool!
```bash
python utils/generate_dsa.py create --topic arrays --difficulty easy --num 301 --name "New Problem Name"
```

## Testing Your Code

Before submitting a Pull Request, ensure your code passes all tests and linting.

```bash
# Run tests
pytest

# Format your code
black .

# Check for linting errors
flake8 .
```

## Pull Request Process

1. Create a new branch: `git checkout -b feature/solve-015`.
2. Commit your changes.
3. Push to your fork and submit a Pull Request.
4. The CI/CD pipeline will automatically run your tests. If it passes, a maintainer will review and merge it!
