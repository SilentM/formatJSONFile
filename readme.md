Details:
This challenge is written in Python3 and can be run from the terminal ("python3 challenge.py") or an IDE like PyCharm.


Assumptions:
1) I assumed the data in the JSON file can be nested to any depth so I used a recursive solution to go through all the possible nested combinations.
2) For strings contained in both dictionaries and lists, if it contains numbers, I replace it with the largest integer.
3) I represent completely empty JSON files with a single "{}".
4) I assume "extreme integer component" means the largest/max contiguous integer value present in the string

Dependencies:
All dependencies used are already part of the standard Python3 library (import json, import re).


Instructions:
1) Store the json file you want to read in the same directory/folder as the python file (challenge.py).
2) Run the "challenge.py" file (either on terminal with the "python3 challenge.py" command or an IDE like PyCharm).
3) In the console/terminal, it will ask the user to input the name of the JSON file they want to read. For example, if you have a JSON file like "input.json", enter "input.json" (without "").
4) The modified JSON string will be printed out in the terminal and will also be stored in a JSON file called "output.json" which will be created in the local directory.



How It Works (Design):

Challenge Part 1) 

- Keys with a value of 0, "", empty arrays [], and empty objects {}, should be removed such that the final result is free of these items.

Based on my assumptions written above, I decided to write a recursive function to take into account any possible depth for nested arrays/dictionaries.
Using an array I made containing the values that need to be removed [0, "", '', {}, []], I checked every nested key/value pair for this value, and removed the key/value pair accordingly


Challenge Part 2)

 - For only the value part of each key/value pair (keys should not be changed):
 - If a string contains one or more embedded integer components, replace that string with a number consisting of the most extreme integer component.

I created 2 functions:
 One that returns true if a given string contains any number 
 The other uses regex to return the maximum integer present in a given string
 
Using these 2 functions, I added an extra if-conditional in the recursive structure of my function from PART 1, to check if the value is a string type and contains numbers, and only then, replace that string with the greatest integer present inside.


Alternative Solution:
I went with a recrusive solution because it was the most flexibile for any depth of json data. However, if I made an assumption of the maximum depth possible, I would have used an iterative approach to walk through the nested children, but this would have been less flexible and robust. I also thought about seperating Part 1 and Part 2 into 2 different functions/traversals, but I realized while the time complexity would overall remain the same if we ignore coefficients, O(n), it would still take twice as long, O(2n), because I would have to walk through the json data twice. Thus, I decided to combine both Part 1 and Part 2 into 1 traversal of the json data using if-conditionals to reduce computation time, O(n).
