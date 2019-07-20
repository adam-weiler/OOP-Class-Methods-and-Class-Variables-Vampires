class Vampire():
    coven = []

    #These are instance methods.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.in_coffin = True
        self.drank_blood_today = True

    def __str__(self):
        return f'The vampire {self.name} is {self.age}. In coffin: {self.in_coffin} - Drank blood today: {self.drank_blood_today}'

    def drink_blood(self):
        self.drank_blood_today = True
        return f'{self.name} has sated their appetite by drinking blood..\n'

    def go_home(self):
        self.in_coffin = True
        return f'{self.name} is returning to their coffin..\n'

    #These are class methods.
    @classmethod
    def create(cls, name, age):
        new_vampire = Vampire(name, age)
        cls.coven.append(new_vampire)
        print(f'{name} has joined the coven!')
        return new_vampire

    @classmethod
    def list_all_vampires(cls):
        print('These are the active vampires in the coven..')

        for vampire in cls.coven:
            print(vampire)
        
    @classmethod
    def sunset(cls):
        print('The sun is setting.. all the vampires are waking up...\n')
        for vampire in cls.coven:
            vampire.drank_blood_today = False
            vampire.in_coffin = False

    @classmethod
    def sunrise(cls):
        print('The sun is rising.. sunlight is deadly to vampires...\n')
        for vampire in cls.coven[:]:
            if (vampire.in_coffin == True) and (vampire.drank_blood_today == True):
                print(f'{vampire.name} is safe and can rest until tomorrow night.')
            else:
                cls.coven.remove(vampire)
                if vampire.drank_blood_today == False:
                    print(f'{vampire.name} has starved to death!')
                elif vampire.in_coffin == False:
                    print(f'{vampire.name} has burnt to death!')
                else:
                    print(f'{vampire.name} has been staked by a slayer!') #This is just to close off the else condition. It won't be triggered.