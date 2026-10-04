"""Run a personal expense and subscription tracking report."""

from data_processor import load_transactions, summarize_spending, find_recurring_payments
from data_visualizer import plot_monthly_spending


def main():
    """Load transactions, print useful summaries, and save a chart."""
    transactions = load_transactions("transactions.csv")
    monthly_summary = summarize_spending(transactions)
    recurring_payments = find_recurring_payments(transactions)

    print("Monthly spending by category:")
    print(monthly_summary.to_string(index=False))

    print("\nPossible recurring payments (seen in at least two months):")
    if recurring_payments.empty:
        print("No recurring payments found.")
    else:
        print(recurring_payments.to_string(index=False))

    plot_monthly_spending(monthly_summary, "monthly_spending.png")
    print("\nChart saved to monthly_spending.png")


if __name__ == "__main__":
    main()
