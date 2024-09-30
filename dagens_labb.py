# Labben blev lite större än jag tänkte mig. 

import datetime
from string import punctuation, ascii_uppercase, digits

SPECIAL_CHAR = set(punctuation)
UPPERCASE = set(ascii_uppercase)
DIGITS = set(digits)

class User:
    def __init__(self, user_id, user_name, user_email, password, last_active = None, level = 0, created = None, is_active=False, is_logged_in = False) -> None:
        self._user_id = user_id
        self._user_name = user_name
        self._user_email = user_email
        self._created = created if created else datetime.datetime.now()
        self._last_active = last_active
        self._password = password
        self._level = level,
        self._is_active = is_active, 
        self._is_logged_in = is_logged_in

    def get_user_id(self):
        return self._user_id
    
    def get_user_name(self):
        return self._user_name
    
    def get_user_email(self):
        return self._user_email

    def get_last_active(self):
        return self._last_active
    
    def get_level(self):
        return self._level

    def get_created(self):
        return self._created
    
    def get_is_active(self):
        return self._is_active

    def get_is_logged_in(self):
        return self._is_logged_in
    
    def set_user_name(self, new_name, password):
        if not self.authenticate(password): return

        if len(new_name) >= 2:
            self._user_name = new_name
        else:
            print("Username must be at least 2 characters!")


    def set_user_email(self, new_email, password):
        if not self.authenticate(password): return

        if "@" not in new_email or '.' not in new_email:
            print("Not valid email")
            return
        
        prefix, sufix = new_email.split('@')
        if prefix:
            domain, top_domain = sufix.split('.')
            if domain and top_domain:
                self._user_email = new_email
                return

        print("Not valid email") 

    def authenticate(self, password):
        if password == self._password: return True
        
        print("Invalid authentication!")
        return False
    
    def set_password(self, new_password, old_password):

        if not self.authenticate(old_password) :return
        if not self.get_is_logged_in(): 
            print("Must be logged in to change password!")
            return
        
        if not len(new_password) >= 8:
            print("New password must be at least 8 characters long")
            return
        
        special_char = False
        number_char = False
        uppercase_char = False
        for char in new_password:
            if char in DIGITS:
                number_char = True
            elif char in UPPERCASE:
                uppercase_char = True
            elif char in  SPECIAL_CHAR:
                special_char = True

        
        if special_char and number_char and uppercase_char:
            self._password = new_password
        else:
            print("Invalid new password!!")

    def log_in(self, password):
        if self.authenticate(password):
            self._is_logged_in = True
            self._update_activity()
            return True
        return False
    
    def log_out(self):
        if not self._is_logged_in:
            self._is_logged_in = False
            self._update_activity()
            return True
        return False       


    def _update_activity(self):
        self._last_active = datetime.datetime.now()





user = User(1,'Kalle88','kalle88@gmail.com', 'abc123A!')
print(user.get_last_active())
user.set_user_name("Kalle33", "abc123A!df")
print(user.get_user_name())
user.set_password("qwer1234A!", "abc123A!")
user.log_in("qwer1234A!")
print(user.get_last_active())