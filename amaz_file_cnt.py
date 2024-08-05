
def count_file(file):
    cnt = 0
    try:
        with open(file, "r") as file:
            for line in file:
                cnt += line.lower().count("apple")
    except FileNotFoundError:
        print("File not found")
        cnt = -1
    except Exception as e:
        print("Error: ", e)
        cnt = -1
    return cnt


cnt = count_file("apple.txt")
print("The word 'apple' appears", cnt, "times in the file")