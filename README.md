# Cache-Memory
This is my first student programming assignment - a simple cache memory compiler simulation.

Main vairables:

'cache' (list, MAX size 8) : empty list where the integers from the requests list will be stored according to the compiling method selected.
'requests' (list) : Empty list at first which is then filled with user input of integers. This list is then iterated over user compiling method to fill the cache list.


First the user is prompted to enter, one at a time, whatever integers they like, and as many as they want until they wish to stop, at which point they will press 0.
Then they are prompted to enter either 1, 2, or Q, with each option having an effect on how the 'memory cache' is compiled:

1 - First in First Out - With this method the requests list is iterated over and added to the cache list. If the cache list becomes full, the first integer from cache is popped from the list and the new integer is appended to the end.
2 - Least Frequently USed - In this method when the cache becomes full, a dictionary is used to track how many times each integer has appeared in requests, and the integer with the lowest value is removed from the cache, with the new integer being added to the end of the list. In the event that two or more integers with the same number of appearances are in the cache, we simply remove the smallest integer.
Q - Exits the program.

In each case of compiling as the requests list is iterated over the word 'hit' will be printed to the screen if the integer is already in the cache and the word 'miss' will be printed if it is not. Finally the finished cache itself will be printed to the screen and the information will be reset. Both cache and request will be wiped and the user will be returned to the beginning where they will be prompted to enter integers all over again.
