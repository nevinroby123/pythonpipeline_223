# Personal Expense and Subscription Tracker

This tool helps you understand where your money goes and notice recurring payments. It reads transactions exported as a CSV, totals expenses by month and category, flags descriptions that appear in multiple months, and saves a spending chart.

## Setup

Install Python, then install the required packages:

```bash
pip install -r requirements.txt
```

## Prepare your transactions

Use `transactions.csv` as a template. It must have these columns: `date`, `description`, `amount`, and `category`.

- Use dates such as `2026-01-15`.
- Enter expenses as positive amounts.
- Enter income and refunds as negative amounts so they are excluded from expense totals.
- Keep merchant descriptions consistent across months to help identify repeat payments.

Replace the sample rows with transactions from your own CSV export. Remove account numbers or other personal details before sharing the file.

## Run

```bash
python main.py
```

The program prints monthly category totals and possible recurring payments. It saves `monthly_spending.png` in the project directory.

## How recurring payments are flagged

A payment description is listed when it appears as an expense in at least two different months. This is a simple clue for review, not a guarantee that a payment is a subscription. Descriptions that vary between transactions may not be grouped together.
