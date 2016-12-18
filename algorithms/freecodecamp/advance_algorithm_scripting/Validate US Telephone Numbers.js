/*
Return true if the passed string is a valid US phone number

The user may fill out the form field any way they choose as long as it is a valid US number. The following are all valid formats for US numbers:
*/

function telephoneCheck(str) {
  return str.match(/^1?[\(\s]*\d{3}[-\)\s]*\d{3}[-\s]?\d{4}$/)? true:false;
}
