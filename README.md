# Simple Python Calculator

A simple Python calculator that provides basic arithmetic operations (addition and subtraction).

## Features

- Addition operation
- Subtraction operation
- Unit tests with pytest
- Code coverage reporting
- Linting with flake8
- Docker support
- CI/CD pipeline with GitHub Actions

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

```python
from calculator import add, subtract

# Addition
result = add(5, 3)  # Returns 8

# Subtraction
result = subtract(5, 3)  # Returns 2
```

## Testing

Run the tests using pytest:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=.
```

## Linting

Run the linter:
```bash
flake8 .
```

## Docker

Build the Docker image:
```bash
docker build -t calculator .
```

Run the container:
```bash
docker run calculator
```

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:
1. Runs tests and generates coverage reports
2. Performs linting checks
3. Builds and pushes Docker image to DockerHub (on main branch pushes)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request 