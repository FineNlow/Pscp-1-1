"""Mickey"""
def main(num):
    """Mickey run!!!!"""
    nhu = [int(input()) for _ in range(num)]
    homie = [int(input()) for _ in range(num)]
    # เรียงจากน้อยไปมาก
    nhu.sort()
    homie.sort()
    # เวลาสูงสุดที่หนูใช้
    nhu_time = 0
    for i in range(num):
        # หาระยะ
        time = abs(nhu[i] - homie[i])
        nhu_time = max(nhu_time, time)
    print(nhu_time)
main(int(input()))
