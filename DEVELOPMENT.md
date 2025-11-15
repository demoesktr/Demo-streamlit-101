# Development Guide

This guide provides detailed information for developers working on the Mortgage Calculator project.

## Development Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Setting Up Development Environment

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd mortgage-calculator
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   # Install in editable mode with dev dependencies
   pip install -e ".[dev]"
   
   # Or install from requirements.txt
   pip install -r requirements.txt
   ```

## Code Standards

### Style Guide

This project follows PEP 8 style guidelines with the following tools:

#### Black (Code Formatter)

```bash
# Format all files
black .

# Check without making changes
black --check .
```

Configuration (in `pyproject.toml` if added):
```toml
[tool.black]
line-length = 88
target-version = ['py38']
```

#### isort (Import Sorting)

```bash
# Sort imports
isort .

# Check without making changes
isort --check-only .
```

Configuration:
```toml
[tool.isort]
profile = "black"
line_length = 88
```

#### Flake8 (Linting)

```bash
# Lint the codebase
flake8 mortgage_calculator/

# Lint with specific configuration
flake8 --max-line-length=88 --extend-ignore=E203 mortgage_calculator/
```

#### Mypy (Type Checking)

```bash
# Type check the codebase
mypy mortgage_calculator/

# Strict mode
mypy --strict mortgage_calculator/
```

### Pre-commit Hooks (Optional)

Install pre-commit hooks to automatically check code before commits:

```bash
pip install pre-commit
pre-commit install
```

Create `.pre-commit-config.yaml`:
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
      - id: black
  
  - repo: https://github.com/pycqa/isort
    rev: 5.12.0
    hooks:
      - id: isort
  
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
        args: [--max-line-length=88]
  
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.5.0
    hooks:
      - id: mypy
```

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest mortgage_calculator/tests/test_calculator.py

# Run specific test
pytest mortgage_calculator/tests/test_calculator.py::TestMortgageCalculator::test_basic_calculation

# Run tests in parallel (install pytest-xdist)
pytest -n auto
```

### Coverage Reports

```bash
# Generate coverage report
pytest --cov=mortgage_calculator

# Generate HTML coverage report
pytest --cov=mortgage_calculator --cov-report=html

# View the report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### Writing Tests

Follow these guidelines when writing tests:

1. **Use descriptive test names**: `test_<functionality>_<scenario>`
2. **Follow AAA pattern**: Arrange, Act, Assert
3. **One assertion per test** (when possible)
4. **Use fixtures** for common setup
5. **Test edge cases** and error conditions

Example:
```python
def test_calculate_mortgage_with_zero_interest(self):
    """Test mortgage calculation with 0% interest rate."""
    # Arrange
    inputs = MortgageInputs(
        home_value=300000,
        deposit=50000,
        interest_rate=0.0,
        loan_term_years=25,
    )
    
    # Act
    calculator = MortgageCalculator()
    results = calculator.calculate_mortgage(inputs)
    
    # Assert
    expected_monthly = 250000 / (25 * 12)
    assert math.isclose(results.monthly_payment, expected_monthly)
```

## Architecture

### Module Organization

```
mortgage_calculator/
├── __init__.py           # Package exports
├── config.py             # Constants and configuration
├── models.py             # Data models (dataclasses)
├── calculations.py       # Business logic
├── utils.py              # Helper functions
├── ui_components.py      # Streamlit UI
└── tests/                # Unit tests
```

### Design Principles

1. **Separation of Concerns**
   - UI logic in `ui_components.py`
   - Business logic in `calculations.py`
   - Data structures in `models.py`

2. **Immutability**
   - Use frozen dataclasses for data models
   - Avoid mutable default arguments

3. **Type Safety**
   - Type hints on all functions
   - Use dataclasses for structured data

4. **Error Handling**
   - Validate inputs early
   - Raise appropriate exceptions
   - Provide meaningful error messages

5. **Single Responsibility**
   - Each module has one clear purpose
   - Each class/function does one thing well

### Adding New Features

1. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Write the code**:
   - Update models if needed
   - Implement business logic
   - Add UI components
   - Update configuration

3. **Write tests**:
   - Unit tests for business logic
   - Integration tests if needed
   - Aim for >80% coverage

4. **Update documentation**:
   - Add docstrings
   - Update README if needed
   - Add to CHANGELOG

5. **Run quality checks**:
   ```bash
   black .
   isort .
   flake8 mortgage_calculator/
   mypy mortgage_calculator/
   pytest
   ```

6. **Commit and push**:
   ```bash
   git add .
   git commit -m "Add feature: description"
   git push origin feature/your-feature-name
   ```

## Debugging

### Streamlit Debugging

```bash
# Run in debug mode
streamlit run main.py --logger.level=debug

# Clear cache
streamlit cache clear
```

### Python Debugging

Use built-in debugger:
```python
import pdb; pdb.set_trace()
```

Or use IDE debuggers (VS Code, PyCharm, etc.)

### Logging

Add logging to troubleshoot issues:
```python
import logging

logger = logging.getLogger(__name__)
logger.info("Calculating mortgage for inputs: %s", inputs)
logger.error("Error occurred: %s", error, exc_info=True)
```

## Performance

### Profiling

Profile the application:
```bash
python -m cProfile -o output.prof main.py
```

Analyze results:
```python
import pstats
p = pstats.Stats('output.prof')
p.sort_stats('cumulative')
p.print_stats(10)
```

### Optimization Tips

1. Use vectorized operations with pandas/numpy
2. Cache expensive calculations
3. Use generators for large datasets
4. Profile before optimizing

## Deployment

### Docker (Optional)

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
```

Build and run:
```bash
docker build -t mortgage-calculator .
docker run -p 8501:8501 mortgage-calculator
```

### Cloud Deployment

#### Streamlit Cloud

1. Push to GitHub
2. Connect repository to Streamlit Cloud
3. Deploy with one click

#### Heroku

Create `Procfile`:
```
web: sh setup.sh && streamlit run main.py
```

Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

## Troubleshooting

### Common Issues

1. **Import errors**: Ensure virtual environment is activated
2. **Module not found**: Check package installation
3. **Test failures**: Check test environment setup
4. **Type errors**: Run mypy to identify issues

### Getting Help

1. Check documentation
2. Review existing issues
3. Run tests to verify behavior
4. Check logs for error details

## Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [PEP 8 Style Guide](https://pep8.org/)

## Continuous Integration

Example GitHub Actions workflow (`.github/workflows/ci.yml`):

```yaml
name: CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run linting
      run: |
        flake8 mortgage_calculator/
        black --check .
        isort --check-only .
        mypy mortgage_calculator/
    
    - name: Run tests
      run: |
        pytest --cov=mortgage_calculator
```

## License

This project is released under the MIT License.
