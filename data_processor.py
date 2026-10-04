"""Load, clean, and summarize personal transaction data."""

import pandas as pd


REQUIRED_COLUMNS = {"date", "description", "amount", "category"}


def load_transactions(file_path):
    """Read transactions, validate columns, and clean incomplete rows."""
    transactions = pd.read_csv(file_path)
    missing_columns = REQUIRED_COLUMNS - set(transactions.columns.str.lower())
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"CSV is missing required columns: {missing}")

    # Normalize header names so CSVs with capitalized headers also work.
    transactions.columns = transactions.columns.str.lower().str.strip()
    transactions = transactions.dropna(subset=["date", "description", "amount", "category"]).copy()
    transactions["date"] = pd.to_datetime(transactions["date"], errors="coerce")
    transactions["amount"] = pd.to_numeric(transactions["amount"], errors="coerce")
    transactions = transactions.dropna(subset=["date", "amount"])

    # Expenses are positive; income and refunds are negative.
    transactions["month"] = transactions["date"].dt.to_period("M").astype(str)
    transactions["description"] = transactions["description"].astype(str).str.strip()
    transactions["category"] = transactions["category"].astype(str).str.strip()
    return transactions


def summarize_spending(transactions):
    """Return total expenses by month and category, excluding income/refunds."""
    expenses = transactions[transactions["amount"] > 0]
    summary = (
        expenses.groupby(["month", "category"], as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_spent"})
        .sort_values(["month", "total_spent"], ascending=[True, False])
    )
    return summary


def find_recurring_payments(transactions):
    """Find descriptions with expenses in two or more different months."""
    expenses = transactions[transactions["amount"] > 0].copy()
    recurring = (
        expenses.groupby("description")
        .agg(months_seen=("month", "nunique"), average_amount=("amount", "mean"))
        .reset_index()
    )
    recurring = recurring[recurring["months_seen"] >= 2]
    recurring["average_amount"] = recurring["average_amount"].round(2)
    return recurring.sort_values("average_amount", ascending=False).reset_index(drop=True)
