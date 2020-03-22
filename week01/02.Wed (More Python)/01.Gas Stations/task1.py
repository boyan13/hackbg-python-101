#Gas Stations
def gas_stations(distance, tank_size, stations):
	li = []
	buf = stations[:]

	while (distance > 0):
		for i in range(len(buf)): #travel
			buf[i] -= tank_size

			if buf[0] > 0:
				return "Stuck on the road!"

		count = 0
		for i in range(len(buf)): #find how many stations will be passed
			if (buf[i] <= 0): #it was passed/reached
				count = i #currently the farthest station reached
		
		li.append(stations[count]) #station to refill at

		while count >= 0:
			del buf[0]
			del stations[0]
			count -= 1
				
		distance -= tank_size

	return li

print( gas_stations(320, 90, [50, 80, 140, 180, 220, 290])      ) #ans:[80, 180, 220, 290]
print( gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]) ) #ans:[70, 140, 240, 280, 350]