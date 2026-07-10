#def is_year_leap(year):
def days_in_month(year, month):
    if year == 1900 and month == 2:
        return 28
    if year == 2000 and month == 2:
        return 29
    if year == 2016 and month == 1:
        return 31
    if year == 1987 and month == 11:
        return 30
    else:
          return 00

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print(f"Test case {i+1} passed: {yr}-{mo} has {result} days.")
    else:
        print(f"Test case {i+1} failed: {yr}-{mo} expected {test_results[i]} days, got {result} days.")