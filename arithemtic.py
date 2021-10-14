result = input('What is the decide of the task? task: 4 * 100 - 54 ')
a = result == 4 * 100 - 54
if a:
    print("""Correct
    Correct answer: 346
    your answer: 346
    """)
else:
    print("""Wrong answer
    Correct answer: 346
    your answer: {}
    """.format(result))
    