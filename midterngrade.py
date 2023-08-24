# zzz
# zzz
# zzz



def calscore(quiz: float,midterm: float,final: float):
    return float(quiz) * 0.15 + float(midterm) * 0.35 + float(final) * 0.5

def calgrade(termScore: float):
    if termScore >= 90: return 'A'
    elif termScore >= 80: return 'B'
    elif termScore >= 70: return 'C'
    elif termScore >= 60: return 'D'
    else: return 'F'

while True:
    name = input("enter name: ")
    quiz = input("enter quiz score: ")
    midterm = input("enter midterm score: ")
    final = input("enter final score:")

    termScore = calscore(quiz,midterm,final)
    grade = calgrade(termScore)

    print("name: " ,name,"\n term score:",termScore,"\n grade:",grade)

    nextname = input("continue? (y/n):")

    if nextname != 'y' and nextname != 'y' :
        break