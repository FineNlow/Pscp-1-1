"""Ping"""
import math as m
def ping():
    """Ping"""
    #packet
    received = 4
    lost = 0
    avg = 0
    most = m.inf * -1
    lowest = m.inf
    #folder
    input()
    #enter
    input()
    #line3
    line3 = input()
    if "[" in line3:
        start = line3.index("[") + 1
        stop = line3.index("]")
        ip = line3[start:stop]
    else:
        ip = line3[8:-23]
    #packet input and recived
    for _ in range(4):
        all_reply = input()
        #if there's reply
        if "Reply" in all_reply:
            start = all_reply.index("time") + 5
            stop = all_reply.index("ms")
            time_logic = all_reply[all_reply.index("time") + 4]
            #if speed is zero
            if time_logic == "<":
                speed = 0
            else:
                speed = int(all_reply[start:stop])
            most = max(speed,most)
            lowest = min(speed,lowest)
            #Not evn div
            avg += speed
        #Failed to recived
        else:
            received -= 1
            lost += 1
    #Print
    print(f"Ping statistics for {ip}:")
    print(f"    Packets: Sent = 4, Received = {received}, Lost = {lost} ({lost/4*100:.0f}% loss),")
    if received>0:
        avg = avg // received
        print("Approximate round trip times in milli-seconds:")
        print(f"    Minimum = {lowest}ms, Maximum = {most}ms, Average = {avg}ms")
ping()
