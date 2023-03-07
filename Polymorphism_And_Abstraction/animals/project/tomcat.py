from project.cat import Cat


class Tomcat(Cat):
    GENDER = "Male"

    def __init__(self, name, age):
        super().__init__(name, age, self.GENDER)

    def make_sound(self):
        return "Hiss"
