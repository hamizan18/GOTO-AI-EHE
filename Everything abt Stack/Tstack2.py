text = '([{}])'

for char in text:
    if char in "([{":
        print(char, "-> pembuka")
    elif char in ")]}":
        print(char, "-> penutup")