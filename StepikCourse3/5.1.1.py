my_list = [i for i in input().split()]
n = int(input())
lists = [[] for i in range(n)]

for i in range(len(my_list)):
    lists[i % n].append(my_list[i])

print(lists)