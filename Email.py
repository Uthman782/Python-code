email = input("Enter your Email: ")
if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@') == 1):
            if (email[-3] == '.') ^ (email[-4] == '.') ^ (email[-5] == '.'):
                if not(email.count(' ') >= 1):
                    print("PASS___---1")
                else:
                    print("Email is wrong.5")
            else:
                print("Email is Wrong.4")
        else:
            print("Email is Wrong.3")
    else:
        print("Email is Wrong.2")
else:
    print("Email is Wrong.1")
