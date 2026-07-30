# Question 8

# Write a function create_password(password).

# -   The outer function stores the original password.
# -   The inner function receives another password.
# -   If both passwords are the same, print Access Granted; otherwise
#     print Access Denied.
# -   Return the inner function.

def create_password(password):
    def another(password2):
        if password == password2:
            print("Acess Granted")
        else:
            print("Acess Denied")
    return another
c = create_password(145673)
c(145673)