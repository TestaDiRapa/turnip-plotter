# turniPlotter
A serial real-time plotter written in Python 3 for microcontrollers.

## Data Format
The plotter can plot multiple data. The different data must be separated by a tabulation and end with a newline.<br>
Examples:<br>
`printf("%d\t%d\n", valueA, valueB);`<br>
also valid<br>
`printf("%d\t%d\t%d\r\n", valueA, valueB, valueC);`<br>

## Tested microcontrollers
* STM NUCLEO F-401RE

## Installation
1.  `git clone https://github.com/TestaDiRapa/turnip-plotter.git`
2.  Navigate to the project folder
3.  `pip3 install -r requirements.txt`

