/*
You are given a JSON object representing a part of your musical album collection. Each album has several properties and a unique id number as its key. Not all albums have complete information
*/

// Setup
// Setup
var collection = {
    "2548": {
      "album": "Slippery When Wet",
      "artist": "Bon Jovi",
      "tracks": [ 
        "Let It Rock", 
        "You Give Love a Bad Name" 
      ]
    },
    "2468": {
      "album": "1999",
      "artist": "Prince",
      "tracks": [ 
        "1999", 
        "Little Red Corvette" 
      ]
    },
    "1245": {
      "artist": "Robert Palmer",
      "tracks": [ ]
    },
    "5439": {
      "album": "ABBA Gold"
    }
};
// Keep a copy of the collection for tests
var collectionCopy = JSON.parse(JSON.stringify(collection));

// Only change code below this line
function updateRecords(id, prop, value) {
  
     if (prop !== "tracks" && value !== "") {
    collection[id][prop] = value ;
  }  
      
  else if (prop === "tracks" && value !=="") {
   
    if (collection[id].hasOwnProperty('tracks')) {
      collection[id][prop].push(value);
      
    }
    else {
      collection[id].tracks = [];
      collection[id][prop].push(value);
    }
    
  }
  
  else if (value === "") {
    delete collection[id][prop];
  }
  
  return collection;
}

// Alter values below to test your code
updateRecords(5439, "hichem", "ABBA");
// Alter values below to test your code
updateRecords(5439, "artist", "ABBA");//, artist should be "ABBA"
updateRecords(5439, "tracks", "Take a Chance on Me");//, tracks should have "Take a Chance on Me" as the last element.
updateRecords(2548, "artist", "");//, artist should not be set
updateRecords(1245, "tracks", "Addicted to Love");//, tracks should have "Addicted to Love" as the last element.
updateRecords(2468, "tracks", "Free");//, tracks should have "1999" as the first element.
updateRecords(2548, "tracks", "");//, tracks should not be set


// Alter values below to test your code
updateRecords(5439, "hichem", "ABBA");
// Alter values below to test your code
updateRecords(5439, "artist", "ABBA");//, artist should be "ABBA"
updateRecords(5439, "tracks", "Take a Chance on Me");//, tracks should have "Take a Chance on Me" as the last element.
updateRecords(2548, "artist", "");//, artist should not be set
updateRecords(1245, "tracks", "Addicted to Love");//, tracks should have "Addicted to Love" as the last element.
updateRecords(2468, "tracks", "Free");//, tracks should have "1999" as the first element.
updateRecords(2548, "tracks", "");//, tracks should not be set
