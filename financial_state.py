def main():
    salary=float(input("Please enter your salary for this Month :"))
    month=input("Enter the month :")
    financial_data = {
        'savings': 0.0,
        'rent': 0.0,
        'electricity': 0.0
    }
    financial_data['savings'] = float(input("Enter the amount allocated to savings: $"))
    financial_data['rent'] = float(input("Enter the amount allocated to rent: $"))
    financial_data['electricity'] = float(input("Enter the amount allocated to electricity: $"))
    total_expenses = financial_data['savings'] + financial_data['rent'] + financial_data['electricity']
    remainder = salary - total_expenses
    yearly_rent = financial_data['rent'] * 12
    yearly_electricity = financial_data['electricity'] * 12
    salary_squared = salary*salary
    additional_savings = 50
    savings_divided = additional_savings / financial_data['savings'] if financial_data['savings'] != 0 else 0
    print(f"\n---- Financial Summary for {month} ----")
    print(f"Salary: ${salary}")
    print(f"Savings: ${financial_data['savings']:.2f}")
    print(f"Rent: ${financial_data['rent']:.2f}")
    print(f"Electricity: ${financial_data['electricity']:.2f}")
    print(f"Total allocated to savings, rent, and electricity: ${total_expenses:.2f}")
    print(f"Remaining salary after these expenses: ${remainder:.2f}")
    print(f"Yearly rent: ${yearly_rent:.2f}")
    print(f"Yearly electricity costs: ${yearly_electricity:.2f}")
    print(f"Salary squared (for fun!): ${salary_squared:.2f}")
    print(f"Additional savings ($50): ${additional_savings:.2f}")
    print(f"Additional savings divided by savings: {savings_divided:.2f}")
main()