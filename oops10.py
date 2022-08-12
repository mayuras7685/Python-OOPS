#multilevel inheritance
class Dad:
    basketball=1


class Son(Dad):
    dance=1
    def isdance(self):
        return f"yes I dance {self.dance} no of times"

class Grandson(Son):
    dance = 6

    def isdance(self):
            return f"Jackson yeah"

darry=Dad()
larry=Son()
harry=Grandson()

print(harry.isdance())


