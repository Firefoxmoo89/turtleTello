# Welcome!
***This is the fancy Turtle Tello Simulator!***  
If you are using this project, you should be familiar with both [python Turtle Graphics](https://docs.python.org/3/library/turtle.html) and [python Tello drones](https://pypi.org/project/easytello/#description).  

### What does it do?
This project is an attempt to simulate a tello drone through turtle, allowing those with limited access to drones to test their code beforehand.  
The syntax of the Tello object is exactly the same as easytello.tello, just change the import to "turtleTello" instead of "easytello" and it will be ready to go instantly!  
*from easytello.tello import tello -> from turtleTello.tello import Tello*  
*from easytello import tello -> from turtleTello import Tello*  
*import easytello -> import turtleTello*  

### But wait...
One might feel the need to point out an issue with this ambitious project: tello drones work in a 3d environment, and turtle is only 2 dimentional.  
In effort to make the turtle workspace as effective as possible, the turtle will act as a drone with the window being a top view (above the drone). To show height, a meter will be on the side. If exact data is neccessary, the "get_height" method is still available.  

## You are ready to get started! 
With the basic idea in place, pop in some code into the main.py file and get going!
It is highly recommended you take a brief look through the module itself as it provides an explanation for each method. If you would like a more detailed list of the capabilities and limitations of this project specifically you may continue reading.

### Let's look at some specifics...
- Measurements in turtle pixels are directly proportional to the tello cm parameters for simplicity. If a drawing ends up smaller or larger than wanted, an optional "scaleFactor" parameter is available when the Tello object is created. The value is based on a percentage (100=normal).
- Due to the nature of turtle, the turtle can only move forward and back. to allow for the drone ability of moving side to side, basic trigonometry has been put in place for the turtle to move directly to the correct xy coodinate that would correspond.
- To ensure there are no bugs with code pasted in, every function has been made available. Any function that is pointless to the simulation simply outputs nonsense :)
- To make the speed as realistic as possible, the turtle has been set to the slowest speed and must wait a second between each called method.
- The meter in the bottom right is run by a second turtle that moves up or down in direct proportion to the up and down method. Both the meter turtle and the drone turtle increase in brightness when moved up and decrease in brightness when moved down. If one would prefer, an option to remove the meter turtle is available when the Tello object is called.
 - With version 2.0 came much improved curves. Now, any 2-dimensional curve is ready to go, and is still great when moved along the z axis a bit. However, curves that are largely vertical get a bit confusing. If it is directly vertical, the drone will just move to the two points, which is what you would actually see from a top view. If the curve is just offset, a small circle will be drawn while a real curve like that from an overhead perspective would look like a partial ellipse. Regardless, this still portrays the positioning correctly. Movement along the z plane is rendered at the end, but future versions will have it live time while the drone is flying through the x and y planes.
- If one were to try calling movement methods on a drone before taking off, the drone would reply with a "motor stop." To help remind people to takeoff, the same has been implemented here, and most functions will not work until "takeoff" has been called.
- Total traveled distance is tracked (mostly) and can be called with the "tof" method, just like the drones.
- Speed can be changed and read, but the actual speed of the turtle will not change because it's slowest speed is still too fast for the drone.
- Be sure to check out the link in the "streamon" method for actual footage of a drone's flight!

> Shoutout to the amazing Mr. Kunz of Utah County Academy of Sciences who brings the wonderful world of mechatronics and physics to his students!
###### Brought to you by Christopher Beadle, UCAS class of 2023. You can reach me at firefoxmoo@gmail.com for any questions or comments.