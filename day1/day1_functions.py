def run_test(test_name, expected_result="Pass"):
    #single testcase
    print(f"{test_name} is {expected_result}")

def calculate_automation_ROI(manual_hours,auto_hours,hourly_rate=1000):
    saved_hours=manual_hours-auto_hours
    money_saved=saved_hours*hourly_rate
    return money_saved
print("\nTest Execution")
run_test("Login_valid")
run_test("Login_invalid","Fail")
savings=calculate_automation_ROI(manual_hours=100,auto_hours=5)
print(f"Rupees {savings:,} saved!")
run_test("dropdown_Select")