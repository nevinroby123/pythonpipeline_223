"""Create a chart of monthly spending by category."""

import matplotlib.pyplot as plt


def plot_monthly_spending(summary, output_path):
    """Save a stacked bar chart using totals grouped by month and category."""
    if summary.empty:
        print("No expenses to plot.")
        return

    chart_data = summary.pivot(index="month", columns="category", values="total_spent").fillna(0)
    chart_data.plot(kind="bar", stacked=True, figsize=(10, 6))
    plt.title("Monthly Spending by Category")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.xticks(rotation=45, ha="right")
    plt.legend(title="Category", bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
