class Test:

    name = "Ashutosh"

    def main(self):
        name = "Someone"

    def someFunOne(self):
        name = "Divya"
        print(self.name, name)


t = Test()
t.name = "Kanchan"
t.someFunOne()
