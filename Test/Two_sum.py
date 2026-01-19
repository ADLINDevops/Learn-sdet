def two_sum(nums,target):
    """
    Hashmap stores {num: Index}
    Single pass    
    """
    seed={} #Hashmap:number->index
    #one pass through array
    for i,num in enumerate(nums):
        #what to find?
        complement=target-num
        #Have we seen it before?
        if complement in seed:
            return [seed[complement],i]
        #Remember this number for future
        seed[num]=i
    return [] #No Solution
#time COmplexity-O(n)- single pass through Array
#space complexity-worst- O(n), save entire array in hashmap

print(two_sum([2,7,11,15],9))
print(two_sum([3,3],9))
print(two_sum([0,9,2,-9],-9))