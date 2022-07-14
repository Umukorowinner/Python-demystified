name = input('What is your name? ');
print("Hey, welcome " + name)

answer = input('Are you ready to play the game? ');
if answer.lower() != 'yes':
    quit()

print("okay, let's play")
score = 0

answer = input('Who is the president of United state of America? ');
if answer.lower() != 'joe biden':
    print("incorrect!")
else:
    print("correct!, you rock.")
    score += 1

answer = input('Who is the president of United Kingdom? ');
if answer.lower() != 'boris johnson':
    print("incorrect!")
else:
    print("correct!, you rock.")
    score += 1
print("your total score is " + str(score))

percentage = (score / 2) * 100

print("your average percentage is: " + str(percentage) + "%")