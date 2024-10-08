"""REal"""
# แปลง string เป็น bits
def con():
    """input on off"""
    bits = ""
    for _ in range(7):
        a = input()
        if a == "on":
            bits += "1"
        else:
            bits += "0"
    return bits

# แปลง bits เป็นเลข
def trans(bits):
    """"bits trans"""
    led_map = (
        ("1111110", "0"),
        ("0110000", "1"),
        ("1101101", "2"),
        ("1111001", "3"),
        ("0110011", "4"),
        ("1011011", "5"),
        ("1011111", "6"),
        ("1110000", "7"),
        ("1111111", "8"),
        ("1111011", "9")
    )
    for pattern, digit in led_map:
        if bits == pattern:
            return digit
    return "ERROR"

# เพิ่มจุดหลังเลข
def adddot():
    """check on/off"""
    a = input()
    return "." if a == "on" else ""

# ตอบ
def main():
    """check segment"""
    ans = ""
    for _ in range(3):
        bitss = con()
        ans += trans(bitss) + adddot()
    if "ERROR" in ans or ans.count(".") > 1:
        print("Error")
    else:
        print(f"{float(ans):.2f}")
main()
