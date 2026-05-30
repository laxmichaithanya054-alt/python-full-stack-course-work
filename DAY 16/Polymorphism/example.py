class Hotstar :
    def __init__(self,username):
        print(f"Hi {username}!\n welcome to Hotstar !!!")
    def promo(self):
        print("you can watch the promos")
    def login(self):
        print("you can login to your account")
    def search(self):
        print("you can search for your favourite movies and shows")
    def profile(self):
        print("you can create your profile")
    def videocontrollers(self):
        print("you can control the video playback")
    
    def movie(self):
        print("you can't watch movies and shows")
    def download(self):
        print("you can't download the content")
    def quality(self):
        print("you can watch the content in limit  quality")
    def ads(self):
        print("you have to watch ads")
class HotstarPremium(Hotstar):
    def __init__(self, username):
        print(f"Hi {username}!\n welcome to Hotstar Premium !!!")

    def movie(self):
        print("you can watch movies and shows")
    def download(self):
        print("you can download the content")
    def quality(self):
        print("you can watch the content upto high  quality")
    def ads(self):
        print("ads will not be shown")

chaitu = Hotstar('chaitu')


chaitu.promo()
chaitu.login()
chaitu.search()
chaitu.profile()
chaitu.videocontrollers()
chaitu.movie()
chaitu.download()
chaitu.quality()
chaitu.ads()

kohli = HotstarPremium('kohli')
kohli.promo()
kohli.login()
kohli.search()
kohli.profile()
kohli.videocontrollers()
kohli.movie()
kohli.download()
kohli.quality()
kohli.ads()