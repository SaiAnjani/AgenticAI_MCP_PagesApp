# Calculator with Email Functionality

This project implements a calculator that can perform various mathematical operations and send the results via email.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Advanced mathematical functions (power, square root, cube root, factorial, etc.)
- Results can be saved to a Pages document (on macOS)
- Results can be sent via email

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Configure the `.env` file with your credentials:
   ```
   # Gemini API Key
   GEMINI_API_KEY=your_gemini_api_key_here

   # Gmail Credentials
   GMAIL_USERNAME=your_gmail_address@gmail.com
   GMAIL_APP_PASSWORD=your_gmail_app_password_here
   ```

   **Note:** For Gmail, you need to use an App Password, not your regular password. To create an App Password:
   1. Go to your Google Account settings
   2. Navigate to Security > 2-Step Verification
   3. At the bottom, select "App passwords"
   4. Generate a new app password for this application

## Usage

1. Run the calculator:
   ```
   python talk2mcp.py
   ```

2. Enter your mathematical query when prompted.

3. The system will process your query and display the results.

4. After the calculation is complete, you'll be asked if you want to send the results via email.

5. If you choose to send the email, enter the recipient's email address.

## Available Mathematical Operations

- Addition: `add(a, b)`
- Subtraction: `subtract(a, b)`
- Multiplication: `multiply(a, b)`
- Division: `divide(a, b)`
- Power: `power(a, b)`
- Square Root: `sqrt(a)`
- Cube Root: `cbrt(a)`
- Factorial: `factorial(a)`
- Logarithm: `log(a)`
- Remainder: `remainder(a, b)`
- Trigonometric functions: `sin(a)`, `cos(a)`, `tan(a)`
- And more...

## Troubleshooting

- If you encounter issues with Gmail, make sure your App Password is correct and that you've enabled "Less secure app access" or are using 2-Step Verification with App Passwords.
- For Pages functionality, this only works on macOS. 