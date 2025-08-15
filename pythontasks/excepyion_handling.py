class InvalidUsernameError (Exception):
    pass
class WeakPasswordError (Exception):
    pass
def ueser_name_check():
    user_name=input("Enter username:")
    if " " in user_name or (len(user_name))<4:
        raise InvalidUsernameError("Username too short!")
    print("Username Checked")

def password_check():
    password=input("Enter Password:")
    isdigits=False
    isspecial=False
    for dig in password:
        if dig.isdigit():
            isdigits=True
    for sp_chr in password:
        if not sp_chr.isalpha() and not sp_chr.isdigit():
            isspecial=True
    if not isdigits or not isspecial:
        raise WeakPasswordError("Password must include a special character!")
    if len(password) < 6:
        raise WeakPasswordError("Password must be at least 6 characters long!")
    print("password is correct")
try:
    ueser_name_check()
    password_check()
except InvalidUsernameError as e:
    print(f"❌ Error: {e}")
except WeakPasswordError as e:
    print(f"❌ Error: {e}")
finally:
    print("Program finished")