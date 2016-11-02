/*
Return an English translated sentence of the passed binary string.
*/

function binaryAgent(str) {

    str = str.split(" ");
    var farr = [];

    var i = 0;
    while (i < str.length) {

      farr.push(String.fromCharCode(parseInt(str[i], 2)));

      i++;
    }

    return (farr.join(""));
  }