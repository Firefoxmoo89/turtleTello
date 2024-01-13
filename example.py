from turtleTello.tello import Tello       			# Import Tello class

maDrone = Tello()					# Create Tello object
print("Battery:",maDrone.get_battery(),"%") 	# Display Battery

maDrone.takeoff()                       			# Drone takeoff

maDrone.forward(98)														# Move forward 98cm
maDrone.right(75)															# Move right 75cm
maDrone.back(119)															# Move back 114cm
maDrone.left(147)															# Move left 147cm
maDrone.up(50)																# Move up 50cm
	
maDrone.curve(-70,-70,0,20,0,0,60)    				# Move across curve with 
																							# points (-70,-70,0) and
																							# (20,0,0) with speed 60 

maDrone.back(20)															# Move back 20cm
maDrone.down(37)															# Move down 37cm
maDrone.right(72)															# Move right 72cm
maDrone.forward(21)														# Move forward 21cm

maDrone.land()                          			# Land the drone

input("Press enter to close")
