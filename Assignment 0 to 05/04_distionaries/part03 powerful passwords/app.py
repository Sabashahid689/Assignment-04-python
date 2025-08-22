import hashlib # import modula The hashlib module in Python is used for secure hashing. In simpler terms, it provides functions to generate one-way hashes (digests) of data.

##create function to hashing the password
def hash_password(password):
   """Hashes the given password using SHA256 and returns the
   hexadecimal digest."""

   return hashlib.sha256(password.encode()).hexdigest()

##create dictionary to store the email and hashed password
stored_logins = {
    "email@email.com": hash_password("password@1234"),
    "ali@gmail.com" : hash_password("ali@g123")
}

def login(email, password):
  """
  Verifies if the provided email and password match the stored credentials.

  Args:
    email: The user's email address.
    password: The user's password.

  Returns:
    True if the email and password match the stored credentials, False otherwise.
  """
  # Check if the email is in the stored logins dictionary

  if email in stored_logins :

    # If the email is found, compare the hashed password with the stored hashed password
    # If they match, return True, indicating successful login
    # Otherwise, return False, indicating login failure
    return stored_logins[email] == hash_password(password)
  # If the email is not found in the stored logins, return False, indicating login failure
  return False


if __name__ == '__main__':

#get input from user
  email = input("Enter your email")
  password = input("Enter your password")

# check user is valid or not
  if login(email,password):
    print("Login successfully!")
  else:
    print("Invalid email or password")

