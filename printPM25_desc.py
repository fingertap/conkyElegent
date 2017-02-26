from CONFIGS import *
import sys
if PM25 == 'NA':
    sys.exit()
PM25 = int(PM25)
if PM25 <= 50:
    print("Good")
elif PM25 <= 100:
    print("Moderate")
elif PM25 <= 150:
    print("Unhealthy for Sensitive People")
elif PM25 <= 200:
    print("Unhealthy")
elif PM25 <= 300:
    print("Very Unhealthy")
else:
    print("Hazardous")

