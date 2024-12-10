#linear search
l = ["latha","kavitha","arun"]
sk= input("Enter the key")

for x in l:
    if x== sk:
        print("the candidate found")
        break
else:
    print("the key you are trying to find does not exist")