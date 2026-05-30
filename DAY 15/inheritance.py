class Instagram :
    def reel (self) :
        print("you can  post the reel")

class Instagram2(Instagram):
    def story(self) :
        print("you can upload a story")

class Instagram3(Instagram2):
    def note (self) :
        print("you can upload a thoughts")

class meta:
    def ai(self):
        print("you can use Ai")

class crossplatform:
    def intigrating(self):
        print("you can integrate with whtasapp and facebook")

class Instagram4(meta,crossplatform,Instagram3):
    def repost(self):
        print("you can repost the content")

print("chaitu - Instagram--------------")
chaitu = Instagram()
chaitu.reel()

print("nag - Instagram2 ------------")
nag = Instagram2()
nag.reel
nag.story()

print("samba - Instagram3 -----------")
samba = Instagram3()
samba.reel()
samba.story()
samba.note()

print('kohli - Instagram4_------------')
kohli = Instagram4()
kohli.reel()
kohli.story()
kohli.note()
kohli.ai()
kohli.intigrating()
kohli.repost()
