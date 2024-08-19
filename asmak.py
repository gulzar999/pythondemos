class user:
    def __init__ (self, user_id, username):
        
        self.id=user_id
        self.username=username
        self.followers=20
        self.following=98

    def follow(self,user):
        user.followers  +=1
        self.following  +=1
        
user_1 = user("564","asma")
user_2 =user("345","puspha")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

class question:
    def __init__(self,q_answer,q_question):
      self.q_answer=q_answer
      self.q_answer=q_question

new_q=question("asma","true")
print(new_q.q_answer)

print("asma\nasma\nasma\nasma")
input("what is your name")

        
