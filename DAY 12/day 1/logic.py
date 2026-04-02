likes = 0
comments = []

def addlike():
    global likes
    likes += 1
    return likes

def addcomments(text):
    comments.append(text)
    return comments

import logic

print(logic.likes)
print(logic.comments)

print(logic.addlike())
print(logic.addlike())
print(logic.addlike())

print(logic.addcomments("good"))