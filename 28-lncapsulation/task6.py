"""# 6-vazifa: Faqat yozish (write-only) xossasi
# PasswordManager klassini yarating va unda private __password atributini belgilang.
# Faqat setter yozing, getterda AttributeError chiqarilsin."""

class PasswordManager:
    def __init__(self, password):
        self.__password = password


    @property
    def password(self):
        raise AttributeError

    @password.setter
    def password(self, new_password):
        self.__password = new_password


p =   PasswordManager("BMWM5F90")
p.password = "Newuser"
print(p.password)