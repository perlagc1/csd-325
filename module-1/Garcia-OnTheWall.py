def countdown(bottles):
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        bottles -= 1
    print("1 bottle of beer on the wall, 1 bottle of beer.")

countdown(5)
print("\nGo buy more beer!")
