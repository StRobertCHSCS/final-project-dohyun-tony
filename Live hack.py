temps = [-8, -9, -12, -15]
wspeed = 15
extreme_cold = False

def windchill(temps, wspeed):
    global extreme_cold
    for i in range(len(temps)):
        temps[i]  = (13.12 + 0.6215*temps[i] - 11.37*wspeed*0.16 + 0.3965*temps[i]*wspeed*0.16)
        if temps[i] <= -30:
            extreme_cold = True

windchill(temps, wspeed)
print(temps)
if extreme_cold == True:
    print("EXTREME COLD ALERT")
else:
    print("NORMAL")