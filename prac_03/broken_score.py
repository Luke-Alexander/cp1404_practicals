score = float(input("Enter score: "))


def get_result(score):
    if score < 0 or score > 100:
        return("Invalid score")
    elif score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")


print(get_result(score))
