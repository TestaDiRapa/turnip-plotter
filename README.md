# turniPlotter
A serial real-time plotter written in Python 3 for microcontrollers.

# Data Format
The plotter can plot multiple data. The different data must be separated by a tabulation and end with a newline.<br>
Examples:
`printf("%d\t%d\n", valueA, valueB);`
also valid
`printf("%d\t%d\t%d\r\n", valueA, valueB, valueC);`

## Tested microcontrollers
* STM NUCLEO F-401RE

