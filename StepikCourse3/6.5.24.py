from collections import defaultdict

messages = eval(f"[{input().split(' = ')[1:][0].strip('[]')}]")
senders = eval(f"[{input().split(' = ')[1:][0].strip('[]')}]")

cock = list(zip(senders, messages))

def_dict = defaultdict(int)

for key in senders:
    for msg in cock:
        msg = msg[1].split()
        if key == msg[0]:
            def_dict[key] = len(msg)


print(senders)
print(cock)
print(def_dict)