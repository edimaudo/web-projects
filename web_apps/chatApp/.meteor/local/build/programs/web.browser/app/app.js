var require = meteorInstall({"client":{"template.main.js":function(){

////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                            //
// client/template.main.js                                                                    //
//                                                                                            //
////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                              //
                                                                                              // 1
Template.body.addContent((function() {                                                        // 2
  var view = this;                                                                            // 3
  return [ HTML.Raw("<h1>Chatapp</h1>\n  "), Spacebars.include(view.lookupTemplate("welcome")), "\n  ", Spacebars.include(view.lookupTemplate("input")), "\n  ", Spacebars.include(view.lookupTemplate("messages")) ];
}));                                                                                          // 5
Meteor.startup(Template.body.renderToDocument);                                               // 6
                                                                                              // 7
Template.__checkName("welcome");                                                              // 8
Template["welcome"] = new Template("Template.welcome", (function() {                          // 9
  var view = this;                                                                            // 10
  return HTML.Raw("<p>\n    Let's chat.\n  </p>");                                            // 11
}));                                                                                          // 12
                                                                                              // 13
Template.__checkName("messages");                                                             // 14
Template["messages"] = new Template("Template.messages", (function() {                        // 15
  var view = this;                                                                            // 16
  return Blaze.Each(function() {                                                              // 17
    return Spacebars.call(view.lookup("messages"));                                           // 18
  }, function() {                                                                             // 19
    return [ "\n    ", HTML.STRONG(Blaze.View("lookup:name", function() {                     // 20
      return Spacebars.mustache(view.lookup("name"));                                         // 21
    }), ":"), " ", Blaze.View("lookup:message", function() {                                  // 22
      return Spacebars.mustache(view.lookup("message"));                                      // 23
    }), HTML.BR(), "\n  " ];                                                                  // 24
  });                                                                                         // 25
}));                                                                                          // 26
                                                                                              // 27
Template.__checkName("input");                                                                // 28
Template["input"] = new Template("Template.input", (function() {                              // 29
  var view = this;                                                                            // 30
  return HTML.Raw('<p>Message: <input type="text" id="message"></p>');                        // 31
}));                                                                                          // 32
                                                                                              // 33
////////////////////////////////////////////////////////////////////////////////////////////////

},"main.js":function(){

////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                            //
// client/main.js                                                                             //
//                                                                                            //
////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                              //
if (Meteor.isClient) {                                                                        // 1
  Template.messages.helpers({                                                                 // 2
    messages: function () {                                                                   // 3
      return Messages.find({}, {                                                              // 4
        sort: {                                                                               // 4
          time: -1                                                                            // 4
        }                                                                                     // 4
      });                                                                                     // 4
    }                                                                                         // 5
  });                                                                                         // 2
  Template.input.events = {                                                                   // 8
    'keydown input#message': function (event) {                                               // 9
      if (event.which == 13) {                                                                // 10
        // 13 is the enter key event                                                          // 10
        if (Meteor.user()) var name = Meteor.user().profile.name;else var name = 'Anonymous';
        var message = document.getElementById('message');                                     // 15
                                                                                              //
        if (message.value != '') {                                                            // 16
          Messages.insert({                                                                   // 17
            name: name,                                                                       // 18
            message: message.value,                                                           // 19
            time: Date.now()                                                                  // 20
          });                                                                                 // 17
          document.getElementById('message').value = '';                                      // 23
          message.value = '';                                                                 // 24
        }                                                                                     // 25
      }                                                                                       // 26
    }                                                                                         // 27
  };                                                                                          // 8
}                                                                                             // 29
////////////////////////////////////////////////////////////////////////////////////////////////

}}},{"extensions":[".js",".json",".html",".css"]});
require("./client/template.main.js");
require("./client/main.js");