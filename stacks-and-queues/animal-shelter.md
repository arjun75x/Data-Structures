# Animal Shelter

An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis.People must adopt either the oldest \(based on arrival time\) of all animals in the shelter, or they can select whether they would prefer a dog or a cat and receive the oldest animal of that type. They cannot select which animal they would like. Create the data structures to maintain this system and implement operations such as enqueue,dequeueAny, dequeueDog, dequeueCat. You may use the built in LinkedList data structure.

```python
class AnimalShelter():
    class Dog():
        def __init__(self, name):
            self.name = name
    class Cat():
        def __init__(self, name):
            self.name = name

    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()
        self.queue = Queue()

    def enqueue(self, animal):
        self.queue.enqueue(animal)
        if (type(animal) is AnimalShelter.Dog):
            self.dog_queue.enqueue(animal)
        else:
            self.cat_queue.enqueue(animal)

    def dequeueAny(self):
        temp = self.queue.dequeue
        if (type(temp) is AnimalShelter.Dog):
            self.dog_queue.dequeue()
        else:
            self.cat_queue.dequeue()
        return temp
    
    def dequeueDog(self):
        out = self.dog_queue.dequeue()
        temp = self.queue.dequeue()
        if (type(temp) is AnimalShelter.Dog):
            return out
        else:
            new_queue = Queue()
            new_queue.enqueue(temp)
            while (not self.queue.isEmpty()):
                temp = self.queue.dequeue
                if (type(temp) is AnimalShelter.Dog):
                    break
                else:
                    new_queue.enqueue(temp)
            while (not self.queue.isEmpty()):
                new_queue.enqueue(self.queue.dequeue())
            self.queue = new_queue
        return out
    
    def dequeueCat(self):
        out = self.cat_queue.dequeue()
        temp = self.queue.dequeue()
        if (type(temp) is AnimalShelter.Cat):
            return out
        else:
            new_queue = Queue()
            new_queue.enqueue(temp)
            while (not self.queue.isEmpty()):
                temp = self.queue.dequeue
                if (type(temp) is AnimalShelter.Cat):
                    break
                else:
                    new_queue.enqueue(temp)
            while (not self.queue.isEmpty()):
                new_queue.enqueue(self.queue.dequeue())
            self.queue = new_queue
        return out
```

