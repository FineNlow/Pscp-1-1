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
        water_month_price = water_used * water_price
        if water_month_price < water_free:
            water_used_price.append(0)
        elif water_used <= water_limit:
            water_used_price.append(water_month_price)
        else:
            water_out_of_limit = water_used - water_limit
            month_price_using = water_limit * water_price
            out_price = water_out_of_limit * water_limit_price
            total_month_price = month_price_using + out_price
            if total_month_price <= water_free:
                water_used_price.append(0)
            else:
                water_used_price.append(total_month_price)
    total_price = sum(water_used_price)
    print(f"{total_price:.2f}")
main()
