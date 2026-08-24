greeting = input("Greeting: ")

if (greeting.strip().casefold() == "hello".strip().casefold() or
    greeting.casefold().startswith("hello".casefold())
    ):
    print("$0")
elif (greeting.casefold().startswith("h".casefold()) and
      greeting.casefold() != "hello".casefold()
      ):
    print("$20")
else:
    print("$100")
