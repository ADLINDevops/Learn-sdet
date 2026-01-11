#validation
def validate_test(Test_type,Severity,Priority=3):
    score=Priority
    if(Severity=="p1"):
        score+=10
    elif(Severity=="p2"):
        score+=5
    if(Test_type=="Login"):
        score+=15
    elif(Test_type=="payment"):
        score+=20
    print(f"{Test_type}(P{Priority},{Severity})->score:{score}")
#Testcase
print("TESTCASE Prioritization")
tests=[("Login","p1",1),("payment","p2",3),("Login","p2",2)]#tuple
for test in tests:
    validate_test(*test)#converts tuple to conditional argument
