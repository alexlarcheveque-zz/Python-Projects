#get user email address

email = input("What is your email address?: ").strip()

#slice out user name

user_name = email[:email.index("@")]

#slice out domain name

domain_name = email[email.index("@") + 1 : ]

#format message

output = "Your username is {} and your domain name is {}"
string = output.format(user_name, domain_name)

#display output message
print(string)
