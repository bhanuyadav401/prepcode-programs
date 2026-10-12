username_input = "user123"
password_input = "secure_pass"
correct_username = "user123"
correct_password = "secure_pass"
login_success = (username_input == correct_username) and (password_input == correct_password)
print("login successful:", login_success)