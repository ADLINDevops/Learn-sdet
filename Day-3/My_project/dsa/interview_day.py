def longest_test_sequence(testcases):
    """Find the longest substring"""
    if not testcases:
        return 0
    new_sequence={}
    start=0
    max_length=0
    for end,testcase in enumerate(testcases):
        if testcase in new_sequence and new_sequence[testcase]>=start:
            start=new_sequence[testcase]+1
       # print(f"value is {start}")
        new_sequence[testcase]=end
        max_length=max(max_length,end-start+1)
        print(new_sequence)
    return len(new_sequence)

print(longest_test_sequence(["test_login","test_PII","test_cart","test_cart","test_out","test_PII"]))
