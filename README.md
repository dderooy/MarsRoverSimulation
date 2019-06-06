# Mars Rover Simulation

## 1. Proplem Definition


A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover’s position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be
`0, 0, N` , which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are `L` , `R` and `M` . `L` and `R` makes the rover spin 90 degrees left or right respectively, without moving from its current spot. `M` means move forward one grid
point, and maintain the same heading. Assume that the square directly North from `(x,y)` is `(x,y+1)`.

### Input:

The problem below requires some kind of input. You are free to implement any mechanism for feeding input into your solution.

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be `(0,0)` . The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover’s orientation. Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.


### Output:

The output for each rover should be its final co-ordinates and heading.


### Example

Test Input:

`5 5`

`1 2 N`

`LMLMLMLMM`

`3 3 E`

`MMRMMRMRRM`

Expected Output:

`1 3 N`

`5 1 E`


## 2. Running the code and tests
First make sure Main.py has executable permissions:
```bash
chmod +x Main.py
ls -l
```
Then run the program by piping data as input:
```bash
cat integrationTest1.txt | python ./Main.py

cat integrationTest2.txt | python ./Main.py

cat integrationTest3.txt | python ./Main.py
```

Run all the unit tests: 
```bash
python -m unittest discover
```

Assumptions:
 - Unix terminal is used for commands
 - Working directory is /MarsRoverSimulation
 - Python version is 2.7 
 

## 3. Design Strategy
The program was desinged using an OOP approach. 
Main.py reads data from piped input file and creates a list of 'RoverPlans' containing a start point and list of commands.
The program then creates a 'Plateau' object with functions to check for collisions and boundaries. Finally the answers are 
compiled by a plotting function which creates and controls 'Rover' objects. 

## 4. General comments and future improvements
 - more testing can always be done
 - provide detailed error reporting to show which specific rovers have issues 
 - optimize and clean code further
 - use better naming conventions and project structure

