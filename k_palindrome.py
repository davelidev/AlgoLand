# http://www.careercup.com/question?id=6287528252407808
# A k-palindrome is a string which transforms into a palindrome on removing at most k characters. 
# 
# Given a string S, and an interger K, print "YES" if S is a k-palindrome; otherwise print "NO". 
# Constraints: 
# S has at most 20,000 characters. 
# 0<=k<=30 
# 
# Sample Test Case#1: 
# Input - abxa 1 
# Output - YES 
# Sample Test Case#2: 
# Input - abdxa 1 
# Output - No

def solution(word, k):
    if k < 0:
        return False
    elif len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return solution(word[1:], k - 1) or solution(word[:-1], k - 1)
    else:
        return solution(word[1:-1], k)
