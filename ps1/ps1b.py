from calendar import month
from logging import INFO, Logger
import logging


def calculate_time():
    portion_down_payment = 0.25
    r = 0.04
    annual_salary = int(
        input("Enter your starting annual salary: ").strip())
    portion_saved = float(
        input("Enter the percent of your salary to save, as a decimal: ").strip())
    total_cost = int(
        input("Enter the cost of your dream home: "). strip())
    semi_annual_raise = float(
        input("Enter the semiannual raise, as a decimal: ").strip())
    current_savings = 0
    months = 0
    estimate_savings_time(portion_down_payment, r, annual_salary, portion_saved, total_cost, semi_annual_raise, current_savings, months)
    return 'Number of months: %d' % months

def estimate_savings_time(portion_down_payment, r, annual_salary, portion_saved, total_cost, semi_annual_raise, current_savings, months):
    while (total_cost * portion_down_payment > current_savings):
        if (months - 1) % 6 == 0 and (months - 1) != 0:
            annual_salary += annual_salary * semi_annual_raise
        monthly_savings = (annual_salary / 12) * portion_saved
        current_savings += monthly_savings + current_savings * (r / 12)
        months += 1


print(calculate_time())
