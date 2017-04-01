/*
Convert the characters "&", "<", ">", '"' (double quote), and "'" (apostrophe), in a string to their corresponding HTML entities.
*/

function convert(str) {
  return str = str.replace(/\&/g, "&amp;").replace(/\</g, "&lt;").replace(/\>/g, "&gt;").replace(/\'/g, "&apos;").replace(/\"/g, "&quot;");
}
