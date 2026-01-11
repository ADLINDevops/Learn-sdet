#TEST Result storage
test_results={
    "Login_valid":{"Status":"PASS","time":2,"Priority":"P1"},
    "Login_invalid":{"Status":"Fail","time":1.8,"Priority":"P1"},
    "dropdown_select":{"Status":"PASS","time":3.2,"Priority":"P2"},
    "table_sort":{"Status":"SKIP","time":0,"Priority":"P3"}
}
print("Test Report")
print("-"*40)
passed=0
total_time=0

for test, details in test_results.items():
    #items() methos used when more than 2 arguments
    status=details["Status"]
    time_taken=details["time"]
    if status=="PASS":
        passed+=1
        total_time+=time_taken
    print(f"{test:15}|{status:4}|{time_taken:5.1f}")
print(f"SUMMARY: {passed}/4 passed, {total_time:.1f}s total")
