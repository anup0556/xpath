# nara-automation-testing

This project is an automation testing framework for the website [https://naravirtual.in](https://naravirtual.in) using Selenium.

## Project Structure

```
nara-automation-testing
├── src
│   ├── tests
│   │   └── nara_test.py
│   └── utils
│       └── __init__.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd nara-automation-testing
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the automation tests, execute the following command:

```
python -m src.tests.nara_test
```

## Contributing

Feel free to submit issues or pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.