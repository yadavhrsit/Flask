class person:
    age = 0
    name = ""
    phone = ""

    def __init__(self, age, name, phone):
        self.age = age
        self.name = name
        self.phone = phone

    def hobby(self):
        print(self.name, " is Playing football")


# constructor


classobj = person(30, "Virat Kohli", "123456789")
classobj.hobby()
