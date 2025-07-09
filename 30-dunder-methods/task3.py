"""3. __call__ — SMS yuboruvchi obyekt
Vazifa: SMS yuboradigan obyekt yaratilsin."""


class SendSMS:
    def __init__(self, text):
        self.text = text


    def __call__(self, *args, **kwds):
        return self.text
    
    def __str__(self):
        return self.text


sms = SendSMS("Wassup")

print(sms)