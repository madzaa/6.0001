
def binary_search():
    lo = 0
    hi = 10000
    num_guesses = 0
    target = 250000

    while lo <= hi:
        middle = (lo+hi) / 2
        num_guesses += 1
        if estimate_savings_time(middle, target) == target:
            return middle
        elif estimate_savings_time(middle, target) < target:
            lo = middle + 1
        else:
            hi = middle - 1
    return estimate_savings_time(middle, target), middle/10000, num_guesses


def estimate_savings_time(savings_rate, down_payment):
    r = 0.04
    semi_annual_raise = 0.07
    current_savings = 0
    months = 0
    annual_salary = 150000

    while (down_payment > current_savings):
        if (months - 1) % 6 == 0 and (months - 1) != 0:
            annual_salary += annual_salary * semi_annual_raise
        monthly_savings = (annual_salary / 12) * (savings_rate/10000)
        current_savings += monthly_savings + current_savings * (r / 12)
        months += 1
        if months >= 36 or current_savings >= down_payment:
            break
    return current_savings


sum, middle, num_guesses = binary_search()
print("Sum:", sum)
print("Middle:", middle)
print("Number of guesses:", num_guesses)
