from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.max_values = lambda: [(i, data[i]) for i in data if data[i] == max(data.values())]
data.min_values = lambda: [(i, data[i]) for i in data if data[i] == min(data.values())]
