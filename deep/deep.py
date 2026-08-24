print("What is the Answer to the Great Question of Life, the Universe, and Everything?")

userSays = input()


if userSays == "42":
    print("Yes")
elif userSays.strip(" ") == "42":
    print("Yes")
elif (userSays.strip().casefold() == "forty-two".strip().casefold() or
    userSays.strip().casefold() == "forty two".strip().casefold()
    ):
    print("Yes")
else:
    print("No")
