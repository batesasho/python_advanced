symbols = ["-", ",", ".", "!", "?"]
new_content = []
with open("text.txt", 'r+') as file:
    content = file.readlines()
    for num in range(len(content)):
        if not content[num]:
            break
        if num % 2 == 0:
            for symbol in symbols:
                content[num] = " ".join(content[num].replace(symbol, "@").split()[::-1])
        else:
            continue
        print(content[num])
