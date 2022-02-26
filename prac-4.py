# Date:-27/1/2022
# Author Sapnil Patel
# Github link:- https://github.com/sapnil1482/Python_Ass.git

n = int(input())
arr = (int, input().split())


arrlist = []

for t in arr:
    arrlist.append(t)
num=arrlist[1]

test_list = [int(i) for i in num]
test_sorted= (sorted(test_list, reverse=True))
List = []
for i in test_sorted:
    if i != max(test_sorted):
        List.append(i)

print(max(List))

