/*
Create a function that sums two arguments together. If only one argument is provided, then return a function that expects one argument and returns the sum.

For example, add(2, 3) should return 5, and add(2) should return a function.
*/
function add() {
  if (arguments.length > 1) {
    var val1 = checkNum(arguments[0]);
    var val2 = checkNum(argumentss[1]);
    if (val1 === undefined || val2 === undefined) {
      return undefined;
    } else {
      return val1 + val2;
    }
  } else {
    var c = arguments[0];
    if (checkNum(c)) {
      // Return function that expect a second argument.
      return function(arg2) {
        // Check for non-numbers
        if (c === undefined || checkNum(arg2) === undefined) {
          return undefined;
        } else {
          // if numbers then add them.
          return c + arg2;
        }
      };
    }
  }
}

function checkNum(num) {
  if (typeof num === "number") {
    return num;
  } else {
    return undefined;
  }
}

console.log(add(2, 3));
console.log(add(2)(3));
console.log(add(2, '3'));
console.log(add(2)([3]));
