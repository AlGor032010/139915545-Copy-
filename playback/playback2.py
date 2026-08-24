userInput = str(input("[Hey...how's...it...goin'...?]  "))

wordCount = len(userInput.split())

def reply1():
   print('[Oh...? Tell...me...more...about...it...]')

def reply2():
    print('[Woah...! Slow...Down...!]')

if wordCount == 1 or wordCount > 1 and "..." in userInput:
    reply1()
elif wordCount > 1 and " " in userInput:
    reply2()
    print("Sorry. " + userInput.replace(" ", "..."))
