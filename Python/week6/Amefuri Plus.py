"""amefuri plus"""
def day_night_checker(time):
    """check whether the time is "Day" or "Night" """
    if 6 <= time < 18:
        return "Day"
    return "Night" #else

def wetness_level(day, weather):
    """return drying level according to weather and day (as integer)"""
    match weather: #if rain, storm or hurricane occur, just end here
        case "R" | "r":
            return 2.00
        case "S" | "s":
            return 3.00
        case "H" | "h":
            return 0.00
    match day: #day or night
        case "Day":
            match weather:
                case "C" | "c":
                    return -0.50
                case "N" | "n":
                    return -1.00
                case "W" | "w":
                    return -1.50
        case "Night":
            match weather:
                case "C" | "c":
                    return -0.25
                case "N" | "n":
                    return -0.50
                case "W" | "w":
                    return -0.75
def main(time, all_weather):
    """main process of calculating the wetness"""
    wetness = 8
    Lost = False
    Dry = False
    for weather in all_weather:
        day = day_night_checker(time)
        time += 1
        if time >= 24:
            time = 0
        wetness += wetness_level(day, weather)
        wetness = min(wetness, 16) #wetness won't be greather than 16
        if wetness <= 0:
            Dry = True
            break
        if weather in ("H", "h"):
            Lost = True
            break
    if Lost:
        print("Lost")
    elif Dry:
        print("Dry")
    else:
        print(f"Still Wet (Wet Level: {wetness:.2f})")
main(int(input()), input())
