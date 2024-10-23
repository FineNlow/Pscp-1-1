"""Music"""
def spotify():
    """Music"""
    artist = {}
    for _ in range(int(input())):
        name, song = input().split("-")
        # ไม่มีชื่อก็สร้าง list เพลงเข้าไปใน artist
        if name not in artist:
            artist[name] = []
        # เพิ่มเพลงไปใน list ของ name artist(ชื่อศิลปิน)
        artist[name].append(song)
    for name, song in artist.items():
        print(name)
        print(*song, sep="\n")
spotify()
