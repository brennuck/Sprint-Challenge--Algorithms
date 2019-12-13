#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 0(n)
Linear complexity because it relies on a single loop executing n times

b) O(n log n)
This algorithm has a lineararithmic runtime complexity. Runtime complexity is shown to be between linear and polynomial.

c) 0(n)
The function is being called recursively n times before reaching base case

## Exercise II

Start at the half way point of the building and drop an egg

If it breaks, go to the halfway point between the bottom of the floor and your current floor and repeat

Otherwise if it does not break, go to the halfway point between your current floor and the top floor and repeat

If (Floor Break Level) - 1 is equal to the floor where the egg doesn't break

Then Floor Break Level is F

This would run at 0(log(n)) complexity