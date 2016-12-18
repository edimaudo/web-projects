/*
Implement a way of converting two dates into a more friendly date range that could be presented to a user.

It must not show any redundant information in the date range.

For example, if the year and month are the same then only the day range should be displayed.

Secondly, if the starting year is the current year, and the ending year can be inferred by the reader, the year should be omitted.

Input date is formatted as YYYY-MM-DD
*/
console.log(friendly(['2015-07-01', '2015-07-04']));
console.log(friendly(['2017-01-01', '2017-01-01']));
console.log(friendly(['2015-12-01', '2016-02-03']));

function friendly(str) {
  var date1 = new Date(str[0].slice(0, 4), str[0].slice(5, 7) - 1, str[0].slice(8, 10));
  var date2 = new Date(str[1].slice(0, 4), str[1].slice(5, 7) - 1, str[1].slice(8, 10));
  var year1 = date1.getFullYear();
  var month1 = date1.getMonth();
  var day1 = date1.getDate();
  var year2 = date2.getFullYear();
  var month2 = date2.getMonth();
  var day2 = date2.getDate();

  var timeDiff = Math.abs(date2.getTime() - date1.getTime());
  var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
  var tempArray = [];

  //same dates
  if (diffDays === 0) {
    tempArray.push(monthInfo(month1) + " " + getOrdinal(day1) + ", " + year1);
  } //first check month and year are the same
  else if (year1 === year2 && month1 === month2) {
    tempArray.push(monthInfo(month1) + " " + getOrdinal(day1), getOrdinal(day2));
    // 2 months aparts
  } else if (diffDays < 70) {
    tempArray.push(monthInfo(month1) + " " + getOrdinal(day1), monthInfo(month2) + " " + getOrdinal(day2));
    //one month apart
  } else if (month2 - month1 === 1) {
    tempArray.push(monthInfo(month1) + " " + getOrdinal(day1), monthInfo(month2) + " " + getOrdinal(day2));
    //default
  }  else {
    tempArray.push(monthInfo(month1) + " " + getOrdinal(day1) + ", " + year1, monthInfo(month2) + " " + getOrdinal(day2) + ", " + year2);
  }
  return tempArray;
}

function monthInfo(num) {
  var monthdata = [
    [0, 'January'],
    [1, 'February'],
    [2, 'March'],
    [3, 'April'],
    [4, 'May'],
    [5, 'June'],
    [6, 'July'],
    [7, 'August'],
    [8, 'September'],
    [9, 'October'],
    [10, 'November'],
    [11, 'December']
  ];
  for (var i = 0; i < monthdata.length; i++) {
    if (num === monthdata[i][0]) {
      return monthdata[i][1];
    }
  }
}

function getOrdinal(n) {
  var s = ["th", "st", "nd", "rd"],
    v = n % 100;
  return n + (s[(v - 20) % 10] || s[v] || s[0]);
}