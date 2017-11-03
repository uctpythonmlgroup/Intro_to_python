class Animal(object):
    def __init__(self,animal_name,animal_age,animal_gender,animal_food):
        super(Animal, self).__init__()
        self.animal_name=animal_name
        self.animal_age=animal_age
        self.animal_food=animal_food
        self.animal_gender=animal_gender


    def run(self,distance):
        print('{0} just rand {1} meters'.format(self.animal_name,distance))

    def swim(self,pool_name,time=2):
        print('I just swam at {} pool for {} hours'.format(pool_name,time))

    def talk(self,words):
        print(words)

#Inheritence


class dog(Animal):
    def __init__(self,dog_type,animal_name,animal_age,animal_gender,animal_food):
        self.dog_type=dog_type
        super(dog, self).__init__(animal_name,animal_age,animal_gender,animal_food)

    def bark(self,num):
        for k in range(0,num):
            print('Woof',end=' ')

    def talk(self,words):
        print('I am a dog')
        print('{} says'.format(self.animal_name+words))

#create a instance of class
Bobby=dog('German','Bobby',17,'Male','Dog Mor')
print(Bobby.run(12))


new_animal=Animal('Judy',12,'Female','Guavas')
new_animal.run('100km')

