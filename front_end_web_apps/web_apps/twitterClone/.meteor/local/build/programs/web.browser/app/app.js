var require = meteorInstall({"client":{"template.main.js":function(require,exports,module){

////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                //
// client/template.main.js                                                                        //
//                                                                                                //
////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                  //
                                                                                                  // 1
Template.body.addContent((function() {                                                            // 2
  var view = this;                                                                                // 3
  return HTML.DIV({                                                                               // 4
    class: "row"                                                                                  // 5
  }, "\n    ", HTML.DIV({                                                                         // 6
    class: "col-md-4 col-sm-4"                                                                    // 7
  }, Spacebars.include(view.lookupTemplate("userManagement"))), "\n    ", HTML.DIV({              // 8
    class: "col-md-8 col-sm-8"                                                                    // 9
  }, Spacebars.include(view.lookupTemplate("tweetBox"))), "\n  ");                                // 10
}));                                                                                              // 11
Meteor.startup(Template.body.renderToDocument);                                                   // 12
                                                                                                  // 13
Template.__checkName("userManagement");                                                           // 14
Template["userManagement"] = new Template("Template.userManagement", (function() {                // 15
  var view = this;                                                                                // 16
  return HTML.DIV({                                                                               // 17
    class: "user-container"                                                                       // 18
  }, "\n    ", HTML.DIV({                                                                         // 19
    class: "panel panel-default userBox"                                                          // 20
  }, "\n      ", HTML.DIV({                                                                       // 21
    class: "panel-body"                                                                           // 22
  }, "\n        ", Blaze.If(function() {                                                          // 23
    return Spacebars.call(view.lookup("currentUser"));                                            // 24
  }, function() {                                                                                 // 25
    return [ "\n        ", HTML.Comment(" Message for logged in user "), "\n        ", HTML.P("Hello ", HTML.STRONG("@", Blaze.View("lookup:currentUser.username", function() {
      return Spacebars.mustache(Spacebars.dot(view.lookup("currentUser"), "username"));           // 27
    })), ", welcome to twitterClone"), "\n        ", HTML.BUTTON({                                // 28
      type: "button",                                                                             // 29
      class: "btn btn-info fullbutton",                                                           // 30
      id: "logout"                                                                                // 31
    }, "Log out"), "\n\n        " ];                                                              // 32
  }, function() {                                                                                 // 33
    return [ "\n        ", HTML.Comment(" Log in module "), "\n        ", HTML.H4("Already have an account?"), "\n        ", HTML.DIV({
      class: "form-group"                                                                         // 35
    }, "\n          ", HTML.INPUT({                                                               // 36
      class: "form-control input-sm",                                                             // 37
      id: "login-username",                                                                       // 38
      placeholder: "Username"                                                                     // 39
    }), "\n          ", HTML.INPUT({                                                              // 40
      class: "form-control input-sm",                                                             // 41
      id: "login-password",                                                                       // 42
      placeholder: "Password",                                                                    // 43
      type: "password"                                                                            // 44
    }), "\n        "), "\n\n        ", HTML.BUTTON({                                              // 45
      type: "button",                                                                             // 46
      class: "btn btn-info fullbutton login",                                                     // 47
      id: "login"                                                                                 // 48
    }, "Log in"), "\n\n\n        ", HTML.Comment(" Sign up module "), "\n        ", HTML.H4("New User?"), "\n        ", HTML.DIV({
      class: "form-group"                                                                         // 50
    }, "\n          ", HTML.INPUT({                                                               // 51
      class: "form-control input-sm",                                                             // 52
      id: "signup-username",                                                                      // 53
      placeholder: "Username"                                                                     // 54
    }), "\n          ", HTML.INPUT({                                                              // 55
      class: "form-control input-sm",                                                             // 56
      id: "signup-fullname",                                                                      // 57
      placeholder: "Full Name (Optional)"                                                         // 58
    }), "\n          ", HTML.INPUT({                                                              // 59
      class: "form-control input-sm",                                                             // 60
      id: "signup-password",                                                                      // 61
      placeholder: "Password",                                                                    // 62
      type: "password"                                                                            // 63
    }), "\n        "), "\n\n        ", HTML.BUTTON({                                              // 64
      type: "button",                                                                             // 65
      class: "btn btn-info fullbutton",                                                           // 66
      id: "signup"                                                                                // 67
    }, "Sign up"), "\n        " ];                                                                // 68
  }), "\n\n      "), "\n    "), "\n  ");                                                          // 69
}));                                                                                              // 70
                                                                                                  // 71
Template.__checkName("tweetBox");                                                                 // 72
Template["tweetBox"] = new Template("Template.tweetBox", (function() {                            // 73
  var view = this;                                                                                // 74
  return HTML.DIV({                                                                               // 75
    class: "tweetbox-container"                                                                   // 76
  }, "\n    ", HTML.DIV({                                                                         // 77
    class: "panel panel-default tweetbox"                                                         // 78
  }, "\n      ", HTML.DIV({                                                                       // 79
    class: "panel-body"                                                                           // 80
  }, "\n        ", HTML.Raw("<!-- Text box for tweet content -->"), "\n        ", HTML.TEXTAREA({
    class: "form-control",                                                                        // 82
    id: "tweetText",                                                                              // 83
    placeholder: "What's happening?",                                                             // 84
    rows: "3"                                                                                     // 85
  }), "\n\n        ", HTML.Raw("<!-- Character count & button -->"), "\n        ", HTML.DIV({     // 86
    class: "pull-right btnGroup"                                                                  // 87
  }, "\n          ", HTML.STRONG({                                                                // 88
    class: function() {                                                                           // 89
      return Spacebars.mustache(view.lookup("charClass"));                                        // 90
    }                                                                                             // 91
  }, Blaze.View("lookup:charCount", function() {                                                  // 92
    return Spacebars.mustache(view.lookup("charCount"));                                          // 93
  })), "\n\n          ", Blaze.If(function() {                                                    // 94
    return Spacebars.call(view.lookup("currentUser"));                                            // 95
  }, function() {                                                                                 // 96
    return [ "\n          ", HTML.BUTTON(HTML.Attrs({                                             // 97
      class: "btn btn-info pull-right",                                                           // 98
      type: "button"                                                                              // 99
    }, function() {                                                                               // 100
      return Spacebars.attrMustache(view.lookup("disableButton"));                                // 101
    }), "Tweet"), "\n          " ];                                                               // 102
  }, function() {                                                                                 // 103
    return [ "\n          ", HTML.BUTTON({                                                        // 104
      class: "btn btn-info pull-right",                                                           // 105
      type: "button",                                                                             // 106
      disabled: ""                                                                                // 107
    }, "Please Log In"), "\n          " ];                                                        // 108
  }), "\n        "), "\n\n      "), "\n    "), "\n  ");                                           // 109
}));                                                                                              // 110
                                                                                                  // 111
////////////////////////////////////////////////////////////////////////////////////////////////////

},"main.js":function(){

////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                                //
// client/main.js                                                                                 //
//                                                                                                //
////////////////////////////////////////////////////////////////////////////////////////////////////
                                                                                                  //
Tweets = new Meteor.Collection("tweets");                                                         // 1
                                                                                                  //
if (Meteor.isClient) {                                                                            // 3
  Template.userManagement.helpers({});                                                            // 5
  Template.userManagement.events({                                                                // 9
    'click #signup': function () {                                                                // 10
      var user = {                                                                                // 11
        username: $('#signup-username').val(),                                                    // 12
        password: $('#signup-password').val(),                                                    // 13
        profile: {                                                                                // 14
          fullname: $('#signup-fullname').val()                                                   // 15
        }                                                                                         // 14
      };                                                                                          // 11
      Accounts.createUser(user, function (error) {                                                // 19
        if (error) alert(error);                                                                  // 20
      });                                                                                         // 21
    },                                                                                            // 22
    'click #login': function () {                                                                 // 24
      var username = $('#login-username').val();                                                  // 25
      var password = $('#login-password').val();                                                  // 26
      Meteor.loginWithPassword(username, password, function (error) {                             // 28
        if (error) alert(error);                                                                  // 29
      });                                                                                         // 30
    },                                                                                            // 31
    'click #logout': function () {                                                                // 33
      Meteor.logout();                                                                            // 34
    }                                                                                             // 35
  });                                                                                             // 9
  Template.tweetBox.helpers({                                                                     // 41
    charCount: function () {                                                                      // 42
      return 140 - Session.get('numChars');                                                       // 43
    },                                                                                            // 44
    charClass: function () {                                                                      // 46
      if (Session.get('numChars') > 140) {                                                        // 47
        return 'errCharCount';                                                                    // 48
      } else {                                                                                    // 49
        return 'charCount';                                                                       // 50
      }                                                                                           // 51
    },                                                                                            // 52
    disableButton: function () {                                                                  // 54
      if (Session.get('numChars') <= 0 || Session.get('numChars') > 140 || !Meteor.user()) {      // 55
        return 'disabled';                                                                        // 58
      }                                                                                           // 59
    }                                                                                             // 60
  });                                                                                             // 41
  Template.tweetBox.events({                                                                      // 63
    'input #tweetText': function () {                                                             // 64
      Session.set('numChars', $('#tweetText').val().length);                                      // 65
    },                                                                                            // 66
    'click button': function () {                                                                 // 68
      var tweet = $('#tweetText').val();                                                          // 69
      $('#tweetText').val("");                                                                    // 70
      Session.set('numChars', 0);                                                                 // 71
                                                                                                  //
      if (Meteor.user()) {                                                                        // 72
        Tweets.insert({                                                                           // 73
          message: tweet,                                                                         // 73
          user: Meteor.user().username                                                            // 73
        });                                                                                       // 73
      }                                                                                           // 74
    }                                                                                             // 75
  });                                                                                             // 63
  Template.tweetBox.onRendered(function () {                                                      // 78
    Session.set('numChars', 0);                                                                   // 79
  });                                                                                             // 80
}                                                                                                 // 81
                                                                                                  //
if (Meteor.isServer) {                                                                            // 83
  Meteor.startup(function () {// code to run on server at startup                                 // 84
  });                                                                                             // 86
}                                                                                                 // 87
////////////////////////////////////////////////////////////////////////////////////////////////////

}}},{"extensions":[".js",".json",".html",".css"]});
require("./client/template.main.js");
require("./client/main.js");