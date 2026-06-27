distance_mi = 20
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

if distance_mi == 0:
    print(bool(distance_mi))

if distance_mi <= 1 and is_raining == 0 or (distance_mi >= 1 and distance_mi <= 6 and is_raining == 0 and has_bike ==1) or (distance_mi >= 6 and has_ride_share_app == 1):
    print('True')