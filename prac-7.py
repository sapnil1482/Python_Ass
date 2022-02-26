# ID:-20CE103
# Author Sapnil Patel
# Github link:- https://github.com/sapnil1482/Python_Ass.git
# AIM:-You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 

T = int(input())
for i in range(T):
    n = input()
    l = len(n)
    if l % 2 == 0:
        b, c = n[:l//2], n[l//2:]
    else:
        b, c = n[:l//2], n[l//2+1:]
    if sorted(b) == sorted(c):
        print("YES")
    else:
        print("NO")