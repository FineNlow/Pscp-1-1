"""PongYa"""
PLAYER = int(input())
print("PONG" if not PLAYER % 3 or str(PLAYER)[-1] == "3" else PLAYER)
