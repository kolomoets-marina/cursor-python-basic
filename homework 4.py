#1. Створіть клас Vehicle з атрибутами екземпляра max_speed і mileage та методами increase_speed, break_speed, mileage_info
#2. Створіть дочірній клас Bus, який успадкує всі змінні та методи класу Vehicle і матиме власний метод seating_capacity
#3. Визначте, від якого класу успадковується клас Bus (перевірте issubclass)
#4. Створіть екземпляр Bus під назвою school_bus і визначте, чи є school_bus об'єктом класу Vehicle/Bus

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage,

    def increase_speed(self, current)
        print(f'Speed was increased by {current} km')

    def break_speed(self):
        print('Your speed is break')

    def mileage_info(self):
        print('You drove {self.mileage} miles')

class Bus(Vehicle):

    def seating_capacity(self, capacity):
        print(f'Seating capacity is {capacity}')

print(issubclass(Bus, Vehicle))

school_bus = Bus('80','9000')

print(isinstance(school_bus, Vehicle))
print(isinstance(school_bus, Bus))

#5. Створіть новий клас School з атрибутами екземпляра get_school_id і number_of_students та методами school_address, main_subject

class School:
    def __init__(self, get_school_id,number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_adress(self,adress):
        print(f'You chose school adress is {adress}')

    def main_subject(self,subject):
        print(f'You chose main subject is {subject}')

#6*. Створіть новий клас SchoolBus, який успадкує всі методи від School і Bus і матиме власний - bus_school_color

class SchoolBus(Vehicle, School):
    def bus_school_collor(self, color):
        print(f'Bus school color is {color}')

#7. Поліморфізм: Створіть два класи: Bear, Wolf. Обидва вони повинні мати метод eat. Створіть два екземпляри: від Ведмідь і від Вовк,
#створіть із нього кортеж і використовуючи спільну змінну, викличте метод eat.

class Bear:
    def __init__(self, name, color, weight, fav_meal):
        self.name = name
        self.color = color
        self.weight = weight
        self.fav_meal = fav_meal

    def eat(self):
        print(f'{self.name} eats {self.fav_meal}')


class Wolf:
    def __init__(self, name, color, weight, fav_meal):
        self.name = name
        self.color = color
        self.weight = weight
        self.fav_meal = fav_meal

    def eat(self):
        print(f'{self.name} eats {self.fav_meal}')

baly = Bear('Baly', 'brown', 56, 'honey')
balto = Wolf('Balto', 'grey', 21, 'meat')

for animal in (baly, balto):
    animal.eat()

#Магічні методи:
#Додатково: 8*. Створіть клас City з атрибутами екземпляра name i population, сторіть новий екземпляр цього класу, лише коли population > 1500,
#інакше повертається повідомлення: "Your city is too small". Підказка: використовуєте для цього завдання магічні методи

class City:
    def __new__(cls, name, population):
        if population <= 1500:
            print('Your city is too small')
        else:
            return object.__new__(cls)

    def __init__(self, name,population):
        self.name = name
        self.population = population

Kharkiv = City('Kharkiv', 1500000)
Shevchenkove = City('Shevchenkove', 1000)
Kupiansk = City('Kupiansk', 1500)


