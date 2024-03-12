# H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). 
# Determine the angle (in degrees) of the hour hand on the clock face right now.

# the clock is circular which means that the hour hand goes around 360 degrees
# there are 12 hours in a clock so to get the angle for one hour is 360 / 12. Hour multiplied 30
# to get the value for a minute 360/ 12 * 60. Getting minutes value. To get minutes value minute * 0.5
# to get the value for a second 360/ 12 * 60 To get second value multiply by 1/120

hour = int(input('Hour Value: '))
minutes = int(input('Minutes Value: '))
seconds = int(input('Seconds Value: '))

val_hour = hour * 30
val_minutes = minutes * 0.5
val_seconds = (seconds * (1/120))

total_degree = val_hour + val_minutes + val_seconds
print(total_degree)