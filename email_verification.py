email = input("Enter the email_id : ")
s,j,d = 0,0,0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and email.count('@') == 1:
            if (email[-3] == '.') ^ (email[-4] == '.'):
                for i in email:
                    if i.isdigit():
                        continue
                    elif i == i.isspace():
                        s = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i == '.' or i == '_' or i == '@':
                        continue
                    else:
                        d = 1
                if s == 1 or j == 1 or d == 1:
                    print("Wrong password5")
                else:
                    print("Right password")
            else:
                print("Wrong password4")
        else:
            print("Wrong password3")
    else:
        print("Wrong password2")
else:
    print("Wrong password1") 