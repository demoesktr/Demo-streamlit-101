# Mortgage Repayments Calculator

A production-ready, modular mortgage calculator application built with Streamlit. This application calculates monthly mortgage payments, total interest, and generates detailed payment schedules.

## Features

- 🏠 **Interactive UI**: User-friendly Streamlit interface
- 📊 **Detailed Analytics**: Comprehensive payment schedules with visualizations
- 🔒 **Type Safety**: Full type hints throughout the codebase
- ✅ **Input Validation**: Robust validation of all user inputs
- 🧪 **Well-Tested**: Comprehensive unit test coverage
- 📦 **Modular Design**: Clean separation of concerns for maintainability
- 🚀 **Production-Ready**: Error handling, logging, and best practices

## Project Structure

```
mortgage_calculator/
├── mortgage_calculator/          # Main package
│   ├── __init__.py              # Package initialization
│   ├── config.py                # Configuration and constants
│   ├── models.py                # Data models (dataclasses)
│   ├── calculations.py          # Core business logic
│   ├── utils.py                 # Utility functions
│   ├── ui_components.py         # Streamlit UI components
│   └── tests/                   # Unit tests
│       ├── __init__.py
│       └── test_calculator.py
├── main.py                      # Application entry point
├── requirements.txt             # Project dependencies
└── README.md                    # This file
```

## Installation

1. **Clone the repository** (or download the files)

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

```bash
streamlit run main.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Using the Calculator

1. **Enter Home Value**: Total value of the property
2. **Enter Deposit**: Initial down payment amount
3. **Enter Interest Rate**: Annual interest rate as a percentage
4. **Enter Loan Term**: Duration of the loan in years

The calculator will automatically:
- Calculate monthly repayments
- Show total repayments and interest
- Display loan-to-value (LTV) ratio
- Generate a complete payment schedule
- Visualize the remaining balance over time

## Running Tests

Execute the test suite:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=mortgage_calculator --cov-report=html

# Run specific test file
pytest mortgage_calculator/tests/test_calculator.py -v
```

## Development

### Code Quality Tools

The project uses several tools to maintain code quality:

- **Black**: Code formatting
  ```bash
  black .
  ```

- **isort**: Import sorting
  ```bash
  isort .
  ```

- **Flake8**: Linting
  ```bash
  flake8 mortgage_calculator/
  ```

- **Mypy**: Type checking
  ```bash
  mypy mortgage_calculator/
  ```

### Code Organization

The codebase follows these principles:

1. **Separation of Concerns**: UI, business logic, and data models are separate
2. **Type Safety**: All functions have type hints
3. **Immutability**: Data models use frozen dataclasses
4. **Error Handling**: Comprehensive error handling with informative messages
5. **Documentation**: All modules, classes, and functions are documented
6. **Testing**: High test coverage for business logic

## Architecture

### Models (`models.py`)

Defines immutable data structures using dataclasses:
- `MortgageInputs`: User input parameters
- `MortgageResults`: Calculated results
- `PaymentScheduleEntry`: Single payment entry
- `PaymentSchedule`: Complete payment schedule

### Calculations (`calculations.py`)

Core business logic:
- `MortgageCalculator`: Main calculator class
  - `calculate_mortgage()`: Calculates monthly payments and totals
  - `generate_payment_schedule()`: Creates detailed payment schedule
  - `calculate_all()`: Convenience method for both calculations

### UI Components (`ui_components.py`)

Streamlit-specific UI code:
- `MortgageUI`: Encapsulates all UI rendering
  - `render_input_section()`: Collects user inputs
  - `render_summary_metrics()`: Displays key metrics
  - `render_payment_schedule()`: Shows schedule and chart
  - `render_additional_info()`: Displays supplementary information

### Utils (`utils.py`)

Helper functions:
- Currency formatting
- Input validation
- DataFrame operations
- LTV ratio calculation

### Config (`config.py`)

Application constants:
- Default values
- Validation constraints
- Display settings

## API Reference

### MortgageCalculator

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

print(f"Monthly payment: ${results.monthly_payment:,.2f}")
print(f"Total interest: ${results.total_interest:,.2f}")
```

## Formula

The calculator uses the standard mortgage payment formula:

```
M = P * [r(1+r)^n] / [(1+r)^n - 1]
```

Where:
- M = Monthly payment
- P = Principal (loan amount)
- r = Monthly interest rate (annual rate / 12)
- n = Number of payments (years × 12)

## Error Handling

The application handles various error scenarios:

- **Validation Errors**: Invalid input values
- **Calculation Errors**: Division by zero, overflow
- **Unexpected Errors**: Logged with full stack trace

## Logging

The application includes comprehensive logging:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

Logs include:
- Input validation results
- Calculation events
- Error details with stack traces

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `pytest`
5. Run linting: `flake8`, `black`, `mypy`
6. Submit a pull request

## License

This project is available for use under standard open-source terms.

## Version History

### Version 1.0.0
- Initial production release
- Modular architecture
- Comprehensive test coverage
- Full type hints
- Streamlit UI
- Error handling and logging

## Support

For issues, questions, or contributions, please refer to the project's issue tracker.

## Acknowledgments

Built with:
- [Streamlit](https://streamlit.io/) - Web framework
- [Pandas](https://pandas.pydata.org/) - Data manipulation
- [Matplotlib](https://matplotlib.org/) - Visualization
- [Pytest](https://pytest.org/) - Testing framework
