def calculate_time():
    portion_down_payment = 0.25
    r = 0.04
    annual_salary = int(input("Enter your annual salary: ").strip())
    portion_to_be_saved = float(
        input("Enter the percent of your salary to save, as a decimal: ").strip())
    total_cost = int(
        input("Enter the cost of your dream home: ").strip())
    current_savings = 0
    principal = (annual_salary / 12) * portion_to_be_saved
    months = 0
    while ((total_cost * portion_down_payment) > current_savings):
        current_savings += principal + (current_savings * (r / 12))
        months += 1
    return months


print(calculate_time())
