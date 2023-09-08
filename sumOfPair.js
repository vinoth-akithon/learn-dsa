/*
Given a sorted array and a number x, find a pair in an array whose sum is closest to x.

Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10
*/


function sumOfPair(array, x) {
    const arrayLength = array.length
    let minimum = Infinity;
    let index1 = 0, index2 = 0;
    let leftPointer = 0, rightPointer = arrayLength -1;

    while (leftPointer < rightPointer) {
        currentPoinerSum = array[leftPointer] + array[rightPointer]
        difference = Math.abs(currentPoinerSum - x);
        if (difference < minimum) {
            minimum = difference;
            index1 = leftPointer
            index2 = rightPointer
        }g
        if (currentPoinerSum > x) {
            rightPointer -= 1;
        } else {
            leftPointer +=1;
        }
    }
    
    return [ array[index1], array[index2] ]
}

// const inputArray = [10, 22, 28, 29, 30, 40], target = 54;  // --> [ 22, 30 ]
const inputArray = [1, 3, 4, 7, 10], target = 15; // --> [ 4, 10 ]
console.log(sumOfPair(inputArray, target))

