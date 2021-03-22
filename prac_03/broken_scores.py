def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        determine_score_status(score)


def determine_score_status(score):
    if score < 50:
        print("Bad")
    elif 50 <= score < 90:
        print("Passable")
    else:
        print("Excellent")
