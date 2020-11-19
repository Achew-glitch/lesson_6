from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = ['Red', 'Yellow', 'Green']

    def running(self):
        for light in self.__color:
                print(light)
                sleep(abs(7 - 5))

a = TrafficLight()
a.running()