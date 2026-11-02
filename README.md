# MTN USSD Data Purchase (Python)

A simple Python program that simulates buying mobile data on the MTN network using a USSD code. It runs in the terminal and uses `while` loops, `if / elif / else` statements, and user input.

## How It Works

1. The user dials the USSD code `*312#`.
2. The user chooses a plan category: Daily, Weekly or Monthly.
3. The user chooses a data plan.
4. The user confirms the purchase.
5. The user enters their PIN.
6. If the PIN is correct and the airtime balance is enough, the program shows:
   `You have successfully purchased ##MB of data.`
7. The user can choose to buy another plan or exit.

## Data Plans

| Category | Option | Data  | Price  |
|----------|--------|-------|--------|
| Daily    | 1      | 100MB | N100   |
| Daily    | 2      | 200MB | N200   |
| Weekly   | 1      | 750MB | N500   |
| Weekly   | 2      | 1.5GB | N1000  |
| Monthly  | 1      | 3GB   | N1500  |
| Monthly  | 2      | 6GB   | N2500  |

## Details

- Starting airtime balance: N2000
- USSD code: `*312#`
- Default PIN: `1234`
- The user has 3 attempts to enter the correct PIN.

## Concepts Used

- `input()` and `print()`
- `while` loops (input validation and repeating the purchase)
- `if / elif / else` statements
- Variables and f-strings

## How to Run

1. Install Python 3.
2. Download or clone this repository:
   ```
   git clone https://github.com/Fathom18-bot/USSD--PYTHON.git
   ```
3. Open the project in PyCharm (or any editor).
4. Run the file:
   ```
   python ussd.py
   ```

## Sample Run

```
Dial USSD code: *312#

--- MTN Data Plans ---
1. Daily Plans
2. Weekly Plans
3. Monthly Plans
Reply with option: 2

--- Weekly Plans ---
1. 750MB - N500
2. 1.5GB - N1000
Reply with option: 1

You are about to buy 750MB for N500
1. Confirm
2. Cancel
Reply with option: 1
Enter your PIN: 1234

You have successfully purchased 750MB of data.
Your new balance is N1500

Buy another plan? 1. Yes  2. No: 2
Thank you for using MTN.
```

## Fabunmi Joel Ayomikun
