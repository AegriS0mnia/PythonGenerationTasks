emails_quantity = int(input())
emails = [input() for i in range(emails_quantity)]
splitted_emails = []
splitted_emails_digitless = []
for i in emails:
    _email = i.split('@')[0]
    if _email[-1].isdigit():
        splitted_emails_digitless.append(_email[:-1])
    else:
        splitted_emails_digitless.append(_email)
    splitted_emails.append(_email)

domain = emails[-1].split('@')[1]
new_users_number = int(input())
result = []

for i in range(new_users_number):
    new_user = input()

    if new_user in splitted_emails:
        new_user_w = f'{new_user}{splitted_emails_digitless.count(new_user)}'
        new_user_email = f'{new_user_w}@{domain}'
        result.append(new_user_email)
        splitted_emails.append(new_user_w)
        splitted_emails_digitless.append(new_user)
    else:
        new_user_email = f'{new_user}@{domain}'
        splitted_emails.append(new_user)
        splitted_emails_digitless.append(new_user)
        result.append(new_user_email)

print(*result, sep='\n')
