score = 0
bonus_score = 0
overall_score = 0

answer = input ("what does the aileron do on a plane, A) Roll the plane left to right, or B) pitch it up and down")
if answer == "A" : 
    print("correct")
    score += 1

answer = input ("what is a air foil, A) a piece of foil filled with air,or B) a certain shape the generates lift when air runs over it")
if answer == "B" : 
    print("correct")
    score += 1
    
    
answer = input ("what is the body of a plane called, A) a plane body, or B) a fusilage")
if answer == "B": 
    print("correct")
    score += 1



answer = input ("what are flaps on a plane, A) they fold down generating lift and slowing the plane down,or B) they allow the plane to turn and yaw")
if answer == "A":
    print ("correct") 
    bonus_score += 1



answer = input ("how do the control surfaces effect the plane, A) do they allow the plane to roll, pitch,and yaw,or B) are they the controls that the pilot holds to control the aircraft")
if answer == "B":
    print ("correct") 
    bonus_score += 1


 # end of quiz:
if score > 2:
    print ("you know your planes")

if bonus_score > 1 and score > 2:
    overall_score = score + bonus_score
    print ("im impressed on you knowledge")

if score < 3: 
    print ("you suck at planes")

print ("you overall score is",overall_score,"out of 5")

