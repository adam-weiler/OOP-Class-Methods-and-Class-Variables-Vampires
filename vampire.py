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
        return f'{self.name} has sated their appetite by drinking blood..\n'

    #sunrise()
        # for all vampires in coven
            #if out_of_coffin or no drank blood today
                # Remove from coffin



    @classmethod
    def sunset(cls):
        print('The sun is setting.. the vampires are all waking up...\n')
        for vampire in cls.coven:
            vampire.drank_blood_today = False
            vampire.in_coffin = False

            # print(f'{vampire.name} - {vampire.in_coffin} - {vampire.drank_blood_today}')


    @classmethod
    def sunrise(cls):
        print('The sun is rising.. sunlight is deadly to vampires...\n')
        for vampire in cls.coven:
            if vampire.in_coffin and vampire.drank_blood_today:
                print(f'{vampire.name} is safe and can rest until tomorrow night.')
            else:
                cls.coven.remove(vampire)
                if vampire.drank_blood_today == False:
                    print(f'{vampire.name} has starved to death!')
                elif vampire.in_coffin == False:
                    print(f'{vampire.name} has burnt to death!')
                else:
                    print(f'{vampire.name} has been staked by a slayer!') #This probably won't run.
                # print(f'{vampire.name} - {vampire.in_coffin} - {vampire.drank_blood_today}')
        pass


    def go_home(self):
        self.in_coffin = True
        return f'{self.name} is returning to their coffin..\n'

# print(Vampire)

dracula = Vampire.create('Dracula', 122)
# print(f'{dracula.name} - {dracula.age} - {dracula.in_coffin} - {dracula.drank_blood_today}')

nosferatu = Vampire.create('Nosferatu', 97)

blade = Vampire.create('Blade', 90)

barnabas = Vampire.create('Barnabas Collins', 175)

von_count = Vampire.create('Count von Count', 1832652)



Vampire.sunset()

print(dracula.drink_blood())
print(dracula.go_home())


print(von_count.drink_blood())

print(nosferatu.go_home())
print(barnabas.go_home())

Vampire.sunrise()


print(Vampire.coven)