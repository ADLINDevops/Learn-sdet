def longest_substring(s):
    """ Sliding window technique
    Time COmplexity:O(n)
    Space complexity:O(min(n,m))"""
    if not s:
        return 0
    start=0
    longest_sub=0
    seen={}# key:char, value:index
    #Traverse string with end pointer
    for end,char in enumerate(s):
        if char in seen and seen[char]>=start:
            start=seen[char]+1
            #if character in dict, then increment start value
        seen[char]=end# if character not in dict, add it

        current_length=end-start+1#length of the window
        longest_sub=max(longest_sub,current_length)#update max length of substring
    return longest_sub

print(longest_substring("abcabcab"))