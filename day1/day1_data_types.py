#Numbers
selenium_tests=50
manual_tests=1000
total_test=selenium_tests+manual_tests
automation_ratio=selenium_tests/total_test*100
print("Testing metrics: ")
print(f"Manual test {manual_tests:,}")
print(f"selenium test {selenium_tests}")
print(f"total test {total_test:,}")
print(f"automation ratio {automation_ratio:.1f}%")

#strings
website="the-internet.herokuapp.com"
login_page=website+"/login"
print(f"Target site={login_page}")

#Type conversion
day_to_master="90"
day_int=int(day_to_master)
print(f"Days to SDET Mastery: {day_int}")