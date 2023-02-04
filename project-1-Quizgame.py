q1="""What is your favorite dog
a.lab
b.husky
c.goldie
d.pug"""

q2="""who is your favorite hero
a.dulqueer
b.prabhas
c.srk
d.yash"""

q3="""what is your favorite dish
a.biryani
b.pizza
c.chicken fried rice
d.paneer"""

q4="""what is your favorite watch
a.apple
b.fossil
c.titan
d.fastrack"""

q5="""who is your bestfriend
a.sita
b.hima
c.akhila
d.harini"""

questions={q1:"c",q2:"a",q3:"a",q4:"b",q5:"c"}

name=input("hi what ur name:")
print("hello",name,"welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this ques(yes/no)")
    if flag1=="yes":
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
        print("wow!you got one point")
        score=score+1
        print("your current score is:",score)
    else:
        print("wrong answer,u lost 1 mark")
        score=score-1
        print("your current score is",score)
    flag2=input("Do you want to quit (yes/no)")
    if flag2=="yes":
        break
print("your total score is",score)
              
































        











































