"""GraderMachine"""
def gradermachine(x,y):
    """GraderMachine"""
    z = ""
    total = 0
    if y > x:
        for i in range(x, y+1):
            if not i%2:
                z += str(i) + " "
                total += i
        print(f"pass : {z}")
        print(f"Sum : {total}")
    else:
        for i in range(x, y-1, -1):
            if not i%2:
                z += str(i) + " "
                total += i
        print(f"pass : {z}")
        print(f"Sum : {total}")
gradermachine(int(input()), int(input()))
