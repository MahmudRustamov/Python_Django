"""8-vazifa: Kalit so‘z bilan to‘qnashuvdan qochish
# class_ nomli atributga ega Course klassini yarating (class kalit so‘zidan farqli).
# class_ qiymatini belgilang va uni chop eting.
"""

class Course:
    def __init__(self, class_):
        self.class_ = class_


course = Course("Python")
print(course.class_)
