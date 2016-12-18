/*
Translate the provided string to pig latin.

Pig Latin takes the first consonant (or consonant cluster) of an English word, moves it to the end of the word and suffixes an "ay".
*/
function translate(str) {
  var checkval;
  var i = 0;
  if (str[i] === 'a' || str[i] === 'e' || str[i] === 'i' || str[i] === 'o' || str[i] === 'u') {
    return str + "way";
  } else {
    for (var i = 0; i < str.length; i++) {
      if (str[i] === 'a' || str[i] === 'e' || str[i] === 'i' || str[i] === 'o' || str[i] === 'u') {
        checkval = i;
        break;
      }
    }
    return str.slice(checkval, str.length) + str.slice(0, checkval) + "ay"
  }
}