"""PH"""
ph = float(input())
Acidic = 0 <= ph < 7
Neutral = ph == 7
Alkaline = 7 < ph <= 14
Error = ph < 0 or ph > 14
PH_INDICATOR = {Acidic : "acidic", Neutral : "neutral", Alkaline : "akaline", Error : "error"}
TPH = PH_INDICATOR[True]
print(TPH)
