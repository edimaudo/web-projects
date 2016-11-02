/*
Return the sum of all odd Fibonacci numbers up to and including the passed number if it is a Fibonacci number.

The first few numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8, and each subsequent number is the sum of the previous two numbers.

As an example, passing 4 to the function should return 5 because all the odd Fibonacci numbers under 4 are 1, 1, and 3.
*/


function checkOdd(n){
  return n % 2 !== 0;
}

function add(a, b) {
    return a + b;
}

function sumFibs(num) {
  return fib(num).filter(checkOdd).reduce(add,0);
}

function fib(n) {
  var nval = n;
  var tempArray = [];
  var a = 0, b = 1, t;
  while (n-- > 0) {
    t = a;
    a = b;
    b += t;
    tempArray.push(a);
  }
  
  function checkMax(val){
    return val <= nval;
  }
  
  return tempArray.filter(checkMax);
 
}