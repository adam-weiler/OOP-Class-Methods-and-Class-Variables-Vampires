class Vampire():
    coven = []

    #These are instance methods.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.in_coffin = True
        self.drank_blood_today = True






    @classmethod
    def create(cls, name, age):
        new_vampire = Vampire(name, age)
        cls.coven.append(new_vampire)
        return new_vampire




    def drink_blood(self):
        self.drank_blood_today = True
        return f'{self.name} has sated their appetite by drinking blood..'

    #sunrise()
        # for all vampires in coven
            #if out_of_coffin or no drank blood today
                # Remove from coffin

    @classmethod
    def sunset(cls):
        for vampire in cls.coven:
            vampire.drank_blood_today = False
            vampire.in_coffin = False

            # print(f'{vampire.name} - {vampire.in_coffin} - {vampire.drank_blood_today}')



    def go_home(self):
        self.in_coffin = True
        return f'{self.name} is returning to their coffin..'

print(Vampire)

dracula = Vampire.create('Dracula', 122)
print(f'{dracula.name} - {dracula.age} - {dracula.in_coffin} - {dracula.drank_blood_today}')

nosferatu = Vampire.create('Nosferatu', 97)

blade = Vampire.create('Blade', 90)

blade = Vampire.create('Blade', 90)

von_count = Vampire.create('Count von Count', 1832652)



print(dracula.drink_blood())

print(dracula.go_home())

Vampire.sunset()

