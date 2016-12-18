/*
Return a new array that transforms the element's average altitude into their orbital periods.
*/

//T = 2*pi sqrt(r^3 / GM) 
//t^2 = r^3*4*Pi^2/GM


function orbitalPeriod(arr) {
  tempArray = [];
  var GM = 398600.4418;
  var earthRadius = 6367.4447;
  var r = 0;
  var orbperiod = 0;
  for (var i = 0; i < arr.length;i++){
    var newperiod ={};
    r = earthRadius + arr[i].avgAlt;
    orbperiod = Math.round(Math.sqrt((Math.pow(r,3)*4*Math.pow(Math.PI,2))/GM));
    newperiod.name = arr[i].name;
    newperiod.orbitalPeriod = orbperiod;
    tempArray.push(newperiod);
  }

  return tempArray;
}