"""WeightStation"""
def weightstation():
    """WeightStation"""
    avg_weight = float(input())
    weight_1 = float(input())
    weight_2 = float(input())
    weight_3 = float(input())

    weight_4 = avg_weight * 4 - (weight_1 + weight_2 + weight_3)

    total_weight = weight_1 + weight_2 + weight_3 + weight_4

    if total_weight > 15000:
        print("Overweight")
    else:
        max_allowed_difference = avg_weight / 2

        if (abs(weight_1 - avg_weight) > max_allowed_difference or
            abs(weight_2 - avg_weight) > max_allowed_difference or
            abs(weight_3 - avg_weight) > max_allowed_difference or
            abs(weight_4 - avg_weight) > max_allowed_difference):
            print("Unbalance")
        else:
            print(f"Pass {weight_4:.2f}")
weightstation()
