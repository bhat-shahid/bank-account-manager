def write_poem():
    lines=input("Enter the new line")
    with open("poem.txt", "a") as f:
        data=f.write(lines+ "\n")
        print("Your line is saved!")
    
    with open("poem.txt", "r")as f:
        lines = f.read()
        print(lines)
write_poem()