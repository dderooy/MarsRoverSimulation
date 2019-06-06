# MARS ROVER CHALLENGE

## 1. Details of Challenge

### 1a. Description:

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover’s position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be
`0, 0, N` , which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are `L` , `R` and `M` . `L` and `R` makes the rover spin 90 degrees left or right respectively, without moving from its current spot. `M` means move forward one grid
point, and maintain the same heading. Assume that the square directly North from `(x,y)` is `(x,y+1)`.

### 1b. Input:

The problem below requires some kind of input. You are free to implement any mechanism for feeding input into your solution.

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be `(0,0)` . The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover’s orientation. Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.


### 1c. Output:

The output for each rover should be its final co-ordinates and heading.


### 1d. Example of input and output

Test Input:

`5 5`

`1 2 N`

`LMLMLMLMM`

`3 3 E`

`MMRMMRMRRM`

Expected Output:

`1 3 N`

`5 1 E`


## 2. How to run the code and tests

```bash
cat integrationTest1.txt | python ./Main.py

cat integrationTest2.txt | python ./Main.py

cat integrationTest3.txt | python ./Main.py
```




## 3. Strategy
The program was desinged using an OOP approach. 
Main.py reads data from piped input file and creates a list of 'RoverPlans' containing a start point and list of commands.
The program then creates a 'Plateau' object with functions to check for collisions and boundaries. Finally the answers are 
compiled by a plotting function which creates and controls 'Rover' objects. 




## 4. General comments and future improvements
 - more testing can always be done
 - providing detailed error reporting to show which specific rovers have issues 
 - optimize and clean code further
 - setup value errors for input

