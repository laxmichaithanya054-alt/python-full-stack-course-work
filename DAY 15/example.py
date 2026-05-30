class Whatsaapv0 :
    def status(self):
        print("you can upload image the videos")

class Whatsaapv1(Whatsaapv0):
    def status(self):
        super().status()
        print("you can like,react and reply")

class Whatsaapv2(Whatsaapv1):
    def status(self):
        super().status()
        print("you can share the status")

chaitu = Whatsaapv2()
chaitu.status()