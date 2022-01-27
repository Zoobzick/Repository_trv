import time
class Traficlight:

    __color = ("RED", "YELLOW", "GREEN")


    def running(self):
        while True:
            self.__color = "RED"
            print(self.__color)
            time.sleep(7)
            self.color = "Yellow"
            print(self.color)
            time.sleep(2)
            self.color = "Green"
            print(self.color)
            time.sleep(5)




svetofor = Traficlight
svetofor.running(svetofor)