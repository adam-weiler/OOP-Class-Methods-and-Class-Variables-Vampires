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



    #drink_blood()
        # drank_blood_today = true

    #sunrise()
        # for all vampires in coven
            #if out_of_coffin or no drank blood today
                # Remove from coffin

    #sunset()
        #for all vampires in coven
            #drank_blood_today is false
            #in_coffin is false


    #go_home
        #in_coffin to true
    pass

print(Vampire)

dracula = Vampire.create('Dracula', 122)