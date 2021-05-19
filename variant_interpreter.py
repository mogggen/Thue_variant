def run(path):
    f = open(path, 'r')
    h = f.readlines()
    init = h.pop().strip("\n")

    if init.isalnum():
        while h:
            i = h.pop(0).strip("\n")
            if i == "::=":
                break
            if ":::" in i:
                left = i.split(":::")[0]
                right = input()
            else:
                left, right = i.split("::=")
                if right[:1] == '~':
                    right = right[1:]
                    for left in init:
                        print(right, end="")
            init = init.replace(left, right)
    f.close()


run("input.txt")
