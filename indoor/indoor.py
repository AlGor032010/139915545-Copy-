#This program asks the user to use their indoor voice or thanks them for doing so
sent = str(input("hello! how may i help you today? "))

lowC = sent.lower()

for char in sent:
    if char.isupper():
        print("shhhhhh! please use your indoor voice")
        print(lowC)
    else:
        print("very well. thank you for using your indoor voice.")
    break
