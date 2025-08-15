class InvalidNameError (Exception):
    pass
class InvalidEmailError (Exception):
    pass
class OverpaymentError (Exception):
    pass

def check_name():
    name=input("Enter name")
    isdigit=False
    for ch in name:
        if ch.isdigit():
            isdigit=True
    if isdigit or not (len(name)>=3):
        raise InvalidNameError("Must be at least 3 characters long")
    return name
def check_email():
    email=input("Enter email")
    if "@" not in email or not email.endswith(".com"):
        raise InvalidEmailError("Must contain '@' and end with '.com'")
    return email
def check_price_and_payment():
    price=int(input("Enter price"))
    if not price>0:
        raise ValueError("Must be a positive number")
    payment=int(input("Enter payment"))
    if not payment>0 or not payment<=price:
        raise OverpaymentError("Payment cannot exceed course price!")
    return price, payment
    
def check_age():
    age=int(input("Enter age"))
    if not age>16:
        raise ValueError("Age must be 16 or older!")
    return age

try:
    name = check_name()
    email = check_email()
    age = check_age()
    price, payment = check_price_and_payment()

    print("\n✅ Registration Successful!")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Age: {age}")
    print(f"Course Price: ₹{price}")
    print(f"Payment Made: ₹{payment}")
    print(f"Remaining Balance: ₹{price - payment}")

except InvalidNameError as e:
    print(f"❌ Error: {e}")
except InvalidEmailError as e:
    print(f"❌ Error: {e}")
except ValueError as e:
    print(f"❌ Error: {e}")
except ValueError as e:
    print(f"❌ Error: {e}")
except OverpaymentError as e:
    print(f"❌ Error: {e}")
finally:
    print("✅ Registration Successful!")