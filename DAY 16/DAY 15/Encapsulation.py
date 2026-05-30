class instagram :
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self.__posts = []
    def get_password(self):
        return self.__password
    def set_password(self,new_password):
        self.__password = new_password
    @property
    def posts(self):
        return self.__posts
    @posts.setter
    def myposts(self,postname):
        self.__posts.append(postname)

chaithanya = instagram("chaithanya","chaitu@123")

print("Before updating :",chaithanya.username)
chaithanya.username = "chaitu"
print("After updating :",chaithanya.username)

print("Before updating password :",chaithanya.get_password())
chaithanya.set_password("chaitu@321")
print("After updating password :",chaithanya.get_password())

print("Posts :",chaithanya.posts)
chaithanya.myposts = "sunset.png"
chaithanya.myposts = "beach.png"
print(chaithanya.posts)
