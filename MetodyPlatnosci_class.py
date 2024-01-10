
class MetodyPlatnosci:
    def __init__(self,p):
        self.prize=p
    def zaplac(self):
        if self.prize > 0:
            print("Wybierz metodę płatności:\n1.Płatność bankowa\n2.Płatność gotówkom\n")
            w=int(input("Twój wybór ->"))
            if w==1:
                print("Wybrano Płatności bankowe\n-----Przekierowuję na stronę banku------\n")
            elif w==2:
                print("Wybrano Płatność gotówką\n")


    