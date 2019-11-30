#Eddie Carpio
#11/19/2019
#project
class person():

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def description(self):
        author = (f'{self.first+self.last+self.age}')
        return author
