import re
#conditions for passwords->
#min 8 char, lower and upper case , digits and special characters
def check_passwd_strength(passwd):
    if len(passwd)<8:
        return "Weak: password must contain atleast 8 characters"
    if not any(char.isdigit() for char in passwd):
        return "Weak: password must contain a digit"
    if not any(char.islower() for char in passwd):
        return "Weak: password must contain a loser case character"
    if not any(char.isupper() for char in passwd):
        return "Weak: password must contain a upper case character"
    if not re.search(r'[!@#$%^&*(){<>?}]',passwd):
        return "Medium: password can also contain a special character"
    return "Strong: password meets all the requirements"
    
def common_passwds(passwd):
    common_pass=["Admin", "Password", "abc123","root","abcd1234","newpassword"]
    # for p in common_pass:
    #     if p.lower()==passwd.lower():
    #         return "Weak: very common password" ------>This is same for the below code in simple language.
    if any(char.lower()==passwd for char in common_pass):
        return "Weak: very common password"
    return check_passwd_strength(passwd)

def passwd_checker():
    while True:
        print("Enter the password to  check strength or enter \"exit\" to exit:")
        passwd=input()
        if passwd.lower()=="exit":
            print("Thank you for using the tool")
            break
        result=common_passwds(passwd)
        print(result)
if __name__=="__main__":
    passwd_checker()

