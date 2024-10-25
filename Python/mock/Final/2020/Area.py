"""Area"""
def main():
    """resistor hua kuy"""
    count = 0
    for _ in range(int(input())):
        line = input().replace(" ","")
        for _ in line:
            count += 1
    print(count)
main()
