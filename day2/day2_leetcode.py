
def contain_duplcate(nums):
    seed={}
    for i,num in enumerate(nums):
        if(num in seed):
            return True
        seed[num]=i
        
    return False
    

nums=[
    [1,2,3,4],
    [1,2,1,3],
    [1,1,1,2]
]
for num in nums:
    result=contain_duplcate(num)
    print(f"Input:{num} Result: {result}")