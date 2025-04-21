class Classmthod:

    wheel =0
    @classmethod
    def tyre(cls):
        cls.wheel=1


class Define_Stattic:

    type=1
    @staticmethod
    def trump():
        Define_Stattic.type+=1

Define_Stattic.trump()
print(Define_Stattic.type)

