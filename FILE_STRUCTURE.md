# Refactored Mortgage Calculator - File Structure

## Quick Start

1. **Extract all files** to a directory
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Run the app**: `streamlit run main.py`
4. **Run tests**: `pytest`

## File Structure

```
mortgage_calculator/
├── mortgage_calculator/           # Main package directory
│   ├── __init__.py               # Package initialization and exports
│   ├── config.py                 # Configuration constants and settings
│   ├── models.py                 # Data models (dataclasses)
│   ├── calculations.py           # Core business logic for calculations
│   ├── utils.py                  # Utility functions and helpers
│   ├── ui_components.py          # Streamlit UI components
│   └── tests/                    # Unit tests
│       ├── __init__.py           # Test package init
│       └── test_calculator.py    # Comprehensive test suite
│
├── main.py                       # Application entry point
├── requirements.txt              # Python dependencies
├── setup.py                      # Package installation setup
├── .gitignore                    # Git ignore rules
├── README.md                     # Main documentation
├── DEVELOPMENT.md                # Developer guide
└── REFACTORING_SUMMARY.md        # Summary of improvements
```

## File Descriptions

### Core Application Files

#### `main.py`
- **Purpose**: Application entry point
- **What it does**: 
  - Configures Streamlit page settings
  - Orchestrates UI rendering and calculations
  - Handles errors and logging
  - Ties all components together
- **Run with**: `streamlit run main.py`

#### `mortgage_calculator/__init__.py`
- **Purpose**: Package initialization
- **What it does**:
  - Defines package exports
  - Makes key classes available for import
  - Sets package version

### Business Logic

#### `mortgage_calculator/config.py`
- **Purpose**: Centralized configuration
- **Contains**:
  - Default values for inputs
  - Validation constraints (min/max values)
  - Display settings (currency symbol, decimal places)
  - Application constants (months per year, etc.)
- **Why**: Keeps magic numbers in one place, easy to modify

#### `mortgage_calculator/models.py`
- **Purpose**: Data structures
- **Contains**:
  - `MortgageInputs`: User input parameters
  - `MortgageResults`: Calculation results
  - `PaymentScheduleEntry`: Single payment entry
  - `PaymentSchedule`: Complete payment schedule
- **Why**: Type-safe, immutable data structures with validation

#### `mortgage_calculator/calculations.py`
- **Purpose**: Core calculation engine
- **Contains**:
  - `MortgageCalculator` class
  - Methods for calculating payments
  - Payment schedule generation
- **Why**: Pure business logic, easy to test independently

#### `mortgage_calculator/utils.py`
- **Purpose**: Helper functions
- **Contains**:
  - Currency formatting functions
  - Input validation
  - DataFrame operations
  - LTV ratio calculation
- **Why**: Reusable utilities, DRY principle

### User Interface

#### `mortgage_calculator/ui_components.py`
- **Purpose**: Streamlit UI components
- **Contains**:
  - `MortgageUI` class
  - Methods for rendering each section
  - Input collection
  - Results display
  - Error/warning messages
- **Why**: Separates UI from business logic, easier to modify interface

### Testing

#### `mortgage_calculator/tests/test_calculator.py`
- **Purpose**: Comprehensive test suite
- **Contains**:
  - Tests for data models
  - Tests for calculations
  - Tests for utility functions
  - Edge case testing
- **Run with**: `pytest`
- **Why**: Ensures code reliability and correctness

### Documentation

#### `README.md`
- **Purpose**: Main project documentation
- **For**: All users
- **Contains**:
  - Project overview
  - Installation instructions
  - Usage guide
  - Feature list
  - Basic architecture

#### `DEVELOPMENT.md`
- **Purpose**: Developer documentation
- **For**: Developers contributing to the project
- **Contains**:
  - Development setup
  - Code standards
  - Testing guidelines
  - Debugging tips
  - Deployment instructions

#### `REFACTORING_SUMMARY.md`
- **Purpose**: Refactoring overview
- **For**: Understanding improvements
- **Contains**:
  - Before/after comparison
  - Key improvements
  - Code quality metrics
  - Best practices applied

### Configuration

#### `requirements.txt`
- **Purpose**: Python dependencies
- **Contains**:
  - Core dependencies (streamlit, pandas, matplotlib)
  - Development dependencies (pytest, black, etc.)
- **Use**: `pip install -r requirements.txt`

#### `setup.py`
- **Purpose**: Package installation configuration
- **Use**: `pip install -e .` for editable install
- **Enables**: Installing as a proper Python package

#### `.gitignore`
- **Purpose**: Git ignore rules
- **Contains**:
  - Python cache files
  - Virtual environments
  - IDE files
  - Test coverage reports
- **Why**: Keeps repository clean

## Module Dependencies

```
main.py
  └─> mortgage_calculator/
        ├─> calculations.py
        │     └─> models.py
        │           └─> config.py
        ├─> ui_components.py
        │     ├─> models.py
        │     ├─> utils.py
        │     └─> config.py
        └─> utils.py
              ├─> models.py
              └─> config.py
```

## How Components Work Together

1. **User Opens App**
   - `main.py` launches Streamlit
   - Page configuration is set

2. **UI Renders**
   - `MortgageUI` renders input section
   - User enters home value, deposit, interest rate, loan term

3. **Input Collection**
   - `ui_components.py` collects inputs
   - Creates `MortgageInputs` object (validated by `models.py`)

4. **Validation**
   - `utils.validate_inputs()` checks for errors
   - If invalid, error displayed via `ui.show_error()`

5. **Calculation**
   - `MortgageCalculator.calculate_all()` is called
   - Returns `MortgageResults` and `PaymentSchedule`

6. **Display Results**
   - `ui.render_summary_metrics()` shows key numbers
   - `ui.render_additional_info()` shows extra details
   - `ui.render_payment_schedule()` shows chart and table

7. **Error Handling**
   - Any errors caught in `main.py`
   - Logged and displayed to user

## Key Design Patterns

### 1. Separation of Concerns
- UI code separate from business logic
- Easy to change either independently

### 2. Data Classes
- Immutable, type-safe data structures
- Validation built-in

### 3. Static Methods
- Calculator methods don't need instance state
- Easy to test and use

### 4. Factory Pattern
- `calculate_all()` creates both results and schedule
- Single call for common use case

### 5. Dependency Injection
- UI components receive data, don't create it
- Better testability

## Usage Examples

### As a Package

```python
from mortgage_calculator import MortgageCalculator, MortgageInputs

# Create inputs
inputs = MortgageInputs(
    home_value=500000,
    deposit=100000,
    interest_rate=5.5,
    loan_term_years=30
)

# Calculate
calculator = MortgageCalculator()
results, schedule = calculator.calculate_all(inputs)

# Use results
print(f"Monthly payment: ${results.monthly_payment:,.2f}")
```

### Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=mortgage_calculator

# Specific test
pytest mortgage_calculator/tests/test_calculator.py::TestMortgageCalculator::test_basic_calculation -v
```

### Code Quality

```bash
# Format code
black .

# Sort imports
isort .

# Lint
flake8 mortgage_calculator/

# Type check
mypy mortgage_calculator/
```

## Next Steps

1. **Install and run** the application
2. **Read README.md** for user documentation
3. **Read DEVELOPMENT.md** if contributing
4. **Run tests** to verify everything works
5. **Explore the code** to understand the structure

## Support

- Check README.md for usage questions
- Check DEVELOPMENT.md for development questions
- Review test files for examples
- All code is documented with docstrings

## Version

Current version: 1.0.0

This is a production-ready release with:
- ✅ Full test coverage
- ✅ Type safety
- ✅ Error handling
- ✅ Documentation
- ✅ Best practices
