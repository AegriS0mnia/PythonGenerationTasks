func = input()
ends = list(map(int, input().split()))
func_values = []
arguments = [i for i in range(ends[0], ends[1] + 1)]

for x in arguments:
    func_values.append(eval(func))

print(f'Минимальное значение функции {func} на отрезке [{ends[0]}; {ends[1]}] равно {min(func_values)}')
print(f'Максимальное значение функции {func} на отрезке [{ends[0]}; {ends[1]}] равно {max(func_values)}')
