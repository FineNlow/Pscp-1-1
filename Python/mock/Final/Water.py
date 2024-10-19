"""Water"""
def main():
    """water"""
    month = int(input())
    water_price = float(input())
    water_limit = float(input())
    water_limit_price = float(input())
    water_free = float(input())
    water_used_price = []
    for _ in range(month):
        water_used = float(input())
        water_month_price = 0
        if water_used <= water_limit:
            water_month_price = water_used * water_price
        else:
            water_month_price = water_limit * water_price + \
                (water_used - water_limit) * water_limit_price
        if water_month_price > water_free:
            water_used_price.append(water_month_price)
        else:
            water_used_price.append(0)
    total_price = sum(water_used_price)
    print(f"{total_price:.2f}")
main()
