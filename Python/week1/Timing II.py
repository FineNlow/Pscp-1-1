"""IO"""
def format_time(seconds):
    """IO"""
    if seconds < 0 or seconds > 864000000:
        return "ERR_:__:__:__"

    days = seconds // 86400
    if days > 9999:
        return "ERR_:__:__:__"
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{days:04}:{hours:02}:{minutes:02}:{seconds:02}"

secondss = int(input())
print(format_time(secondss))
