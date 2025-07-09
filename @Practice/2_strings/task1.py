"""Foydalanuvchi sizga biror bir linkni input qilib kiritadi, siz uni
    rostdan ham link ekanligini tekshirishingiz kerak. Agar uni boshlanishi
    http:// yoki https:// bo'lsa demak u link bo'ladi."""


link = input('Enter the link: ')

if link.startswith('https://') or link.startswith("http://"):
    print('This is a link')
else:
    print("This is not a proper link")