"""Kuy"""
def cock(h, m):
    """Kuy"""
    minute_angle = m * 6
    hour_angle = h * 30 + m * 0.5
    angle_diff = abs(minute_angle - hour_angle)
    angle_diff = min(angle_diff, 360 - angle_diff)
    if hour_angle <= minute_angle and angle_diff < 6:
        print("True")
    else:
        print("False")
cock(int(input()), int(input()))
