questions = [
    ["Who invented the light bulb?", "Edison", "Newton", "Einstein", "Tesla", 1],
    ["Largest planet in our Solar System?", "Earth", "Jupiter", "Mars", "Saturn", 2],
    ["National animal of India?", "Tiger", "Lion", "Elephant", "Peacock", 1],
    ["Fastest land animal?", "Cheetah", "Horse", "Kangaroo", "Leopard", 1],
    ["Which gas do plants absorb?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Helium", 3],
    ["Currency of Japan?", "Won", "Dollar", "Yen", "Ringgit", 3],
    ["Which ocean is the largest?", "Indian", "Pacific", "Atlantic", "Arctic", 2],
    ["How many continents are there?", "5", "6", "7", "8", 3],
    ["First man to step on the Moon?", "Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Rakesh Sharma", 1],
    ["Which is the programming language for AI?", "Python", "HTML", "CSS", "SQL", 1]
]
Prizes = [0,1000,5000,10000,50000,120000,360000,650000,1250000,2500000,10000000]
i=0
for q in questions:
    print("Question: ",q[0]) 
    print("Options: ",q[1]) 
    print("Options: ",q[2]) 
    print("Options: ",q[3]) 
    print("Options: ",q[4]) 

    a = int(input("choose one option from 1-4: "))
    if a == q[5]:
        print("you answered the question correctly")
        i +=1
        print("Reward for correctly answering this question is: ",Prizes[i])
    else:
        print("Your answer in wrong the correct options was: ",q[5])
        print("You won: ",Prizes[i])
        break

    

else:
    print("Congrats you are our new corerpati")
