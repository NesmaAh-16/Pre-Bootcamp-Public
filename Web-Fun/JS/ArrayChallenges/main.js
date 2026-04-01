console.log("_____________ Always Hungry ____________________________")
function alwaysHungry(arr) {
    var foodFound = false;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === "food") {
            console.log("yummy");
            foodFound = true;
        }
    }
    if (!foodFound) {
        console.log("I'm hungry");
    }
}

alwaysHungry([3.14, "food", "pie", true, "food"]);
alwaysHungry([4, 1, 5, 7, 2]);

console.log("__________________________High Pass Filter _____________________________")
function highPass(arr, cutoff) {
    var filteredArr = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}

var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result);
console.log("__________________________Better than average _____________________________")
function betterThanAverage(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    var average = sum / arr.length;

    var count = 0;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > average) {
            count++;
        }
    }
    return count;
}

var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result);
console.log("_______________________Array Reverse ________________________________")
function reverse(arr) {
    var left = 0;
    var right = arr.length - 1;
    while (left < right) {
        var temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result);
console.log("______________________ Fibonacci Array_________________________________")
function fibonacciArray(n) {
    var fibArr = [0, 1];
    while (fibArr.length < n) {
        var prevNum1 = fibArr[fibArr.length - 1];
        var prevNum2 = fibArr[fibArr.length - 2];
        fibArr.push(prevNum1 + prevNum2);
    }
    return fibArr;
}

var result = fibonacciArray(10);
console.log(result); 