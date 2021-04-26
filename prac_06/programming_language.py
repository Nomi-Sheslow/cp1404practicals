class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{language.name}, {language.typing} Typing, Reflection={language.reflection}, First appeared in " \
               "{language.year}".format(language=self)

    def is_dynamic(self):
        return self.typing == "Dynamic"
