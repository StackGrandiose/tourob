# TOU(ring)ROB(ot)

This is a program designed for use on a robot for the "Robot Tour" Event for the 2025 Science Olympiad Season. It uses the [CircuitPython library (TBD)](https://circuitpython.org/) and uses the [Adafruit Metro M4 Express](https://www.adafruit.com/product/3382) board as the microcontroller.

- 01/05/2025: Able to pathfind to coordinates

# How-To Use

Positions on the course are determined by their X value and Y value. Y values are in reverse (going down on the coordinate plane means the Y value increases). Map dimensions must be rectangular and are defined in `MAPWIDTH` and `MAPHEIGHT`

Start and end points can be determined by changing the values in `STARTPOINT` and `ENDPOINT` in `main.py`. The order of points that the robot travels to is determined by `checkpointList[]`.

```python
checkpointList = [
        STARTPOINT, # First Destination
        [0, 0], # Next destination after STARTPOINT
        [1, 4], # Etc..
        [3, 2], # Etc..
        [3, 4], # Etc..
        ENDPOINT # Travels from [3, 4] to ENDPOINT
        ]
```

In the robot's path-finding algorithm, it accounts for walls in the course. All wall positions are defined in `wallList[]`. Their position is defined by two values, which are the coordinates of the imaginary boxes/points on both sides of the wall.

```python
wallList = [
        [[2, 0], [3, 0]], # This wall is on the border between box [2, 0] and [3, 0]
        [[1, 0], [1, 1]],
        [[3, 0], [3, 1]],
        [[0, 1], [0, 2]],
        [[0, 2], [1, 2]],
        [[2, 2], [3, 2]],
        [[1, 3], [1, 4]],
        [[3, 3], [3, 4]],
        [[1, 4], [2, 4]]
        ]

```

The program is instructed to solve the course using the `solveCourse` function.
