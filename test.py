from vampire import Vampire

dracula = Vampire.create('Dracula', 122) #Alive
nosferatu = Vampire.create('Nosferatu', 97)
blade = Vampire.create('Blade', 90) #Alive
barnabas = Vampire.create('Barnabas Collins', 175)
von_count = Vampire.create('Count von Count', 1832652)  #Alive
print()

# Vampire.list_all_vampires()
print()

Vampire.sunset()

print(dracula.drink_blood())
print(dracula.go_home())

print(nosferatu.go_home())

print(barnabas.go_home())

print(von_count.drink_blood())

Vampire.sunrise()
print()

Vampire.list_all_vampires()