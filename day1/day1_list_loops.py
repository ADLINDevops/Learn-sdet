#Lists
tests=["login_valid","login_invalid","dropdown_select","table_sort"]
print("Testcase=",tests)
#for Loop
for test in tests:
    print(f"Testcase {test}...>Passed")

#range
for day in range(1,11):
    status="🚀" if day<8 else "🔥"
    print(f"day:{status}progress")

#list methods
tests.append("file_upload")
print("updated testcases",tests)
print("Total testcase:",len(tests))