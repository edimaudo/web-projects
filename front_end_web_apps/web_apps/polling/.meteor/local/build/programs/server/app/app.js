var require = meteorInstall({"collections":{"polls.js":function(){

//////////////////////////////////////////////////////////////////////////////////
//                                                                              //
// collections/polls.js                                                         //
//                                                                              //
//////////////////////////////////////////////////////////////////////////////////
                                                                                //
Polls = new Mongo.Collection('polls');                                          // 1
//////////////////////////////////////////////////////////////////////////////////

}},"server":{"bootstrap.js":function(){

//////////////////////////////////////////////////////////////////////////////////
//                                                                              //
// server/bootstrap.js                                                          //
//                                                                              //
//////////////////////////////////////////////////////////////////////////////////
                                                                                //
// run this when the meteor app is started                                      // 1
Meteor.startup(function () {                                                    // 2
  // if there are no polls available create sample data                         // 4
  if (Polls.find().count() === 0) {                                             // 5
    // create sample polls                                                      // 7
    var samplePolls = [{                                                        // 8
      question: 'Is Meteor awesome?',                                           // 10
      choices: [{                                                               // 11
        text: 'Of course!',                                                     // 12
        votes: 0                                                                // 12
      }, {                                                                      // 12
        text: 'Eh',                                                             // 13
        votes: 0                                                                // 13
      }, {                                                                      // 13
        text: 'No. I like plain JS',                                            // 14
        votes: 0                                                                // 14
      }]                                                                        // 14
    }, {                                                                        // 9
      question: 'Is CSS3 Flexbox the greatest thing since array_slice(bread)?',
      choices: [{                                                               // 19
        text: '100% yes',                                                       // 20
        votes: 0                                                                // 20
      }, {                                                                      // 20
        text: '200% yes',                                                       // 21
        votes: 0                                                                // 21
      }, {                                                                      // 21
        text: '300% yes',                                                       // 22
        votes: 0                                                                // 22
      }]                                                                        // 22
    }]; // loop over each sample poll and insert into database                  // 17
                                                                                //
    _.each(samplePolls, function (poll) {                                       // 28
      Polls.insert(poll);                                                       // 29
    });                                                                         // 30
  }                                                                             // 32
});                                                                             // 34
//////////////////////////////////////////////////////////////////////////////////

},"main.js":["meteor/meteor",function(require,exports,module){

//////////////////////////////////////////////////////////////////////////////////
//                                                                              //
// server/main.js                                                               //
//                                                                              //
//////////////////////////////////////////////////////////////////////////////////
                                                                                //
var Meteor = void 0;                                                            // 1
module.importSync("meteor/meteor", {                                            // 1
  Meteor: function (v) {                                                        // 1
    Meteor = v;                                                                 // 1
  }                                                                             // 1
}, 0);                                                                          // 1
Meteor.startup(function () {// code to run on server at startup                 // 3
});                                                                             // 5
//////////////////////////////////////////////////////////////////////////////////

}]}},{"extensions":[".js",".json"]});
require("./collections/polls.js");
require("./server/bootstrap.js");
require("./server/main.js");
//# sourceMappingURL=app.js.map
