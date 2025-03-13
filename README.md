# Burst Balloons
My approach to burst balloons problem.

## Problen Statement:
A series of ordered tagged balloons are give. Each time one of them are to be exploded.
Each explosion is given a value. Value is current baloon value multipleied by neighboring
balloons. If there is no neighbour due to being first and last balloon then value 1 is assumed.
Determine sequence of explotions that will give max value in return.

## Solution
Problem is by its nature is tree type. Top level tree node contains all balloons. Algorithms will try to
explode each balloons individually. Keep this operation until all balloons are exploded. This tree nothing
but permutations tree. We need to calculate explosion value for each possible permutation.


                                            [1, 2, 3, 4]
                |1                     |2                  |3                      |4
            [2, 3, 4]              [1, 3, 4]            [1, 2, 4]               [1, 2, 3]
        |2     |3    |4         |1    |3     |4       |1     |2    |4          |1    |2    |3
       [3, 4] [2, 4]  [2, 3]   [3, 4][1, 4][1, 3]   [2, 4][1, 4][1, 2]      [2, 3][1, 3][1, 2]
      /3 \4    |2 |4   |2 |3       
    [4]  [3]  [4] [2] [3] [2]
    |4   |3
    []   []
    
At each tree layer one of remaining items gets burst and remaining items passed down to the
down layer. When tree hits deepest level, all sums already collected, all path items already collected
and result is returned in an array item. Midlevels collects return values from below and relays them to 
upper levels. Finally max value is picked among returned values.

    all possible permutations:[
    [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2]
    [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1]
    ...
    Time complexity of all permutations are n!
"""
