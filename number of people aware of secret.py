#You are given two integers, delay and forget. Each person will share the secret with a new person every day, starting from delay days after discovering the secret.
#task is to find the number of people who know the secret at the end of day n.
def count_people_knowing_secret(days, delay, forget):
    people_knowing_secret = set()

    for day in range(1, days + 1):
        if day >= delay:
            people_knowing_secret.add(day)
        forget_set = set()
        for person in people_knowing_secret:
            if day - person > forget:
                forget_set.add(person)

        people_knowing_secret -= forget_set

    return len(people_knowing_secret)


input_days = int(input())
input_delay = int(input())
input_forget = int(input())
output = count_people_knowing_secret(input_days, input_delay, input_forget)
print(output)

