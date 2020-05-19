var require = meteorInstall({"client":{"main.html":["./template.main.js",function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////
//                                                                         //
// client/main.html                                                        //
//                                                                         //
/////////////////////////////////////////////////////////////////////////////
                                                                           //
module.exports = require("./template.main.js");                            // 1
                                                                           // 2
/////////////////////////////////////////////////////////////////////////////

}],"template.main.js":function(){

/////////////////////////////////////////////////////////////////////////////
//                                                                         //
// client/template.main.js                                                 //
//                                                                         //
/////////////////////////////////////////////////////////////////////////////
                                                                           //
                                                                           // 1
Template.body.addContent((function() {                                     // 2
  var view = this;                                                         // 3
  return Spacebars.include(view.lookupTemplate("resolution"));             // 4
}));                                                                       // 5
Meteor.startup(Template.body.renderToDocument);                            // 6
                                                                           // 7
Template.__checkName("resolution");                                        // 8
Template["resolution"] = new Template("Template.resolution", (function() {
  var view = this;                                                         // 10
  return "Hello";                                                          // 11
}));                                                                       // 12
                                                                           // 13
/////////////////////////////////////////////////////////////////////////////

},"main.js":["meteor/templating","meteor/reactive-var","./main.html",function(require,exports,module){

/////////////////////////////////////////////////////////////////////////////
//                                                                         //
// client/main.js                                                          //
//                                                                         //
/////////////////////////////////////////////////////////////////////////////
                                                                           //
var Template = void 0;                                                     // 1
module.importSync("meteor/templating", {                                   // 1
  Template: function (v) {                                                 // 1
    Template = v;                                                          // 1
  }                                                                        // 1
}, 0);                                                                     // 1
var ReactiveVar = void 0;                                                  // 1
module.importSync("meteor/reactive-var", {                                 // 1
  ReactiveVar: function (v) {                                              // 1
    ReactiveVar = v;                                                       // 1
  }                                                                        // 1
}, 1);                                                                     // 1
module.importSync("./main.html");                                          // 1
Template.hello.onCreated(function () {                                     // 6
  function helloOnCreated() {                                              // 6
    // counter starts at 0                                                 // 7
    this.counter = new ReactiveVar(0);                                     // 8
  }                                                                        // 9
                                                                           //
  return helloOnCreated;                                                   // 6
}());                                                                      // 6
Template.hello.helpers({                                                   // 11
  counter: function () {                                                   // 12
    return Template.instance().counter.get();                              // 13
  }                                                                        // 14
});                                                                        // 11
Template.hello.events({                                                    // 17
  'click button': function (event, instance) {                             // 18
    // increment the counter when button is clicked                        // 19
    instance.counter.set(instance.counter.get() + 1);                      // 20
  }                                                                        // 21
});                                                                        // 17
/////////////////////////////////////////////////////////////////////////////

}]}},{"extensions":[".js",".json",".html",".css"]});
require("./client/template.main.js");
require("./client/main.js");