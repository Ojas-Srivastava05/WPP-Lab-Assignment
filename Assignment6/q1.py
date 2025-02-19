class PasswordManager:
    def __init__(self):
        self.old_passwords = []
        n = int(input("Enter the number of passwords that you have: "))
        for _ in range(n):
            self.old_passwords.append(input("Enter the password: "))

    def get_password(self):
   
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self):
       
        new_password = input("Enter the password that you want to set: ")

        if new_password in self.old_passwords:
            print("The entered password was an old password")
            return False  

        self.old_passwords.append(new_password)
        print("The password has been successfully changed")
        return True  

    def is_correct(self, password):
        
        return password == self.get_password()



pm = PasswordManager()
print("Most recent password:", pm.get_password())
pm.set_password()
password_attempt = input("Enter password to verify: ")
print("Password correct?", pm.is_correct(password_attempt))