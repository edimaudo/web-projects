var require = meteorInstall({"client":{"components":{"template.poll-form.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                         //
// client/components/template.poll-form.js                                                 //
//                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////
                                                                                           //
                                                                                           // 1
Template.__checkName("pollForm");                                                          // 2
Template["pollForm"] = new Template("Template.pollForm", (function() {                     // 3
  var view = this;                                                                         // 4
  return HTML.Raw('<form> \n    <div class="form-group question-group">\n        <label>Question</label>\n        <input type="text" name="question" class="form-control" placeholder="Your Question">\n    </div>\n\n    <div class="form-group">\n        <label>Choice #1</label>\n        <input type="text" name="choice1" class="form-control" placeholder="Choice #1">\n    </div>\n    <div class="form-group">\n        <label>Choice #2</label>\n        <input type="text" name="choice2" class="form-control" placeholder="Choice #2">\n    </div>\n    <div class="form-group">\n        <label>Choice #3</label>\n        <input type="text" name="choice3" class="form-control" placeholder="Choice #3">\n    </div>\n\n    <button type="submit" class="btn btn-lg btn-primary btn-block">Create Poll</button>\n</form>');
}));                                                                                       // 6
                                                                                           // 7
/////////////////////////////////////////////////////////////////////////////////////////////

},"template.poll.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                         //
// client/components/template.poll.js                                                      //
//                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////
                                                                                           //
                                                                                           // 1
Template.__checkName("poll");                                                              // 2
Template["poll"] = new Template("Template.poll", (function() {                             // 3
  var view = this;                                                                         // 4
  return HTML.DIV({                                                                        // 5
    class: "poll well well-lg",                                                            // 6
    "data-id": function() {                                                                // 7
      return Spacebars.mustache(view.lookup("_id"));                                       // 8
    }                                                                                      // 9
  }, "\n\n    ", HTML.H3(Blaze.View("lookup:question", function() {                        // 10
    return Spacebars.mustache(view.lookup("question"));                                    // 11
  })), "\n\n    ", Blaze.Each(function() {                                                 // 12
    return Spacebars.dataMustache(view.lookup("indexedArray"), view.lookup("choices"));    // 13
  }, function() {                                                                          // 14
    return [ "\n        ", HTML.A({                                                        // 15
      href: "#",                                                                           // 16
      class: "vote btn btn-primary btn-block",                                             // 17
      "data-id": function() {                                                              // 18
        return Spacebars.mustache(view.lookup("_index"));                                  // 19
      }                                                                                    // 20
    }, "\n            ", HTML.SPAN({                                                       // 21
      class: "votes pull-right"                                                            // 22
    }, Blaze.View("lookup:votes", function() {                                             // 23
      return Spacebars.mustache(view.lookup("votes"));                                     // 24
    })), "\n            ", HTML.SPAN({                                                     // 25
      class: "text"                                                                        // 26
    }, Blaze.View("lookup:text", function() {                                              // 27
      return Spacebars.mustache(view.lookup("text"));                                      // 28
    })), "\n        "), "\n    " ];                                                        // 29
  }), "\n\n");                                                                             // 30
}));                                                                                       // 31
                                                                                           // 32
/////////////////////////////////////////////////////////////////////////////////////////////

},"poll-form.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                         //
// client/components/poll-form.js                                                          //
//                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////
                                                                                           //
Template.pollForm.events({                                                                 // 1
  // handle the form submission                                                            // 3
  'submit form': function (event) {                                                        // 4
    // stop the form from submitting                                                       // 6
    event.preventDefault(); // get the data we need from the form                          // 7
                                                                                           //
    var newPoll = {                                                                        // 10
      question: event.target.question.value,                                               // 11
      choices: [{                                                                          // 12
        text: event.target.choice1.value,                                                  // 13
        votes: 0                                                                           // 13
      }, {                                                                                 // 13
        text: event.target.choice2.value,                                                  // 14
        votes: 0                                                                           // 14
      }, {                                                                                 // 14
        text: event.target.choice3.value,                                                  // 15
        votes: 0                                                                           // 15
      }]                                                                                   // 15
    }; // create the new poll                                                              // 10
                                                                                           //
    Polls.insert(newPoll);                                                                 // 20
  }                                                                                        // 21
});                                                                                        // 1
/////////////////////////////////////////////////////////////////////////////////////////////

},"poll.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                         //
// client/components/poll.js                                                               //
//                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////
                                                                                           //
// attach events to our poll template                                                      // 1
Template.poll.events({                                                                     // 2
  // event to handle clicking a choice                                                     // 4
  'click .vote': function (event) {                                                        // 5
    // prevent the default behavior                                                        // 7
    event.preventDefault(); // get the parent (poll) id                                    // 8
                                                                                           //
    var pollID = $(event.currentTarget).parent('.poll').data('id');                        // 11
    var voteID = $(event.currentTarget).data('id'); // create the incrementing object so we can add to the corresponding vote
                                                                                           //
    var voteString = 'choices.' + voteID + '.votes';                                       // 15
    var action = {};                                                                       // 16
    action[voteString] = 1; // increment the number of votes for this choice               // 17
                                                                                           //
    Polls.update({                                                                         // 20
      _id: pollID                                                                          // 21
    }, {                                                                                   // 21
      $inc: action                                                                         // 22
    });                                                                                    // 22
  }                                                                                        // 25
});                                                                                        // 2
/////////////////////////////////////////////////////////////////////////////////////////////

}},"template.app.body.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                         //
// client/template.app.body.js                                                             //
//                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////
                                                                                           //
                                                                                           // 1
Template.body.addContent((function() {                                                     // 2
  var view = this;                                                                         // 3
  return [ HTML.Raw("<!-- PULL IN THE POLL CREATION FORM -->\n  "), HTML.DIV({             // 4
    class: "container"                                                                     // 5
  }, "\n    ", HTML.DIV({                                                                  // 6
    class: "row"                                                                           // 7
  }, "\n      ", HTML.DIV({                                                                // 8
    class: "col-md-6 col-md-offset-3"                                                      // 9
  }, "\n        ", Spacebars.include(view.lookupTemplate("pollForm")), "\n      "), "\n    "), "\n  "), HTML.Raw("  \n\n  <!-- LOOP OVER POLLS AND SHOW EACH -->\n  "), HTML.DIV({
    class: "polls"                                                                         // 11
  }, "\n      ", Blaze.Each(function() {                                                   // 12
    return Spacebars.call(view.lookup("polls"));                                           // 13
  }, function() {                                                                          // 14
    return [ "\n          ", Spacebars.include(view.lookupTemplate("poll")), "\n      " ];
  }), "\n  ") ];                                                                           // 16
}));                                                                                       // 17
Meteor.startup(Template.body.renderToDocument);                                            // 18
                                                                                           // 19
/////////////////////////////////////////////////////////////////////////////////////////////

},"app.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                         //
// client/app.js                                                                           //
//                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////
                                                                                           //
Template.body.helpers({                                                                    // 1
  polls: function () {                                                                     // 3
    return Polls.find();                                                                   // 4
  }                                                                                        // 5
}); // adds index to each item                                                             // 1
                                                                                           //
UI.registerHelper('indexedArray', function (context, options) {                            // 10
  if (context) {                                                                           // 11
    return context.map(function (item, index) {                                            // 12
      item._index = index;                                                                 // 13
      return item;                                                                         // 14
    });                                                                                    // 15
  }                                                                                        // 16
});                                                                                        // 17
/////////////////////////////////////////////////////////////////////////////////////////////

}},"collections":{"polls.js":function(){

/////////////////////////////////////////////////////////////////////////////////////////////
//                                                                                         //
// collections/polls.js                                                                    //
//                                                                                         //
/////////////////////////////////////////////////////////////////////////////////////////////
                                                                                           //
Polls = new Mongo.Collection('polls');                                                     // 1
/////////////////////////////////////////////////////////////////////////////////////////////

}}},{"extensions":[".js",".json",".html",".css"]});
require("./client/components/template.poll-form.js");
require("./client/components/template.poll.js");
require("./client/template.app.body.js");
require("./client/components/poll-form.js");
require("./client/components/poll.js");
require("./client/app.js");
require("./collections/polls.js");