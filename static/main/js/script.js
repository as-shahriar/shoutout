var home_url = "http://192.168.0.15:8000";
var luser = $("#username");
var lpass = $("#pass");
var alert = $("#alert-box");

var fname = $("#fname");
var lname = $("#lname");
var r_username = $("#reg_username");
var email = $("#email");
var r_pass = $("#reg_pass");


r_username.change(function (e) {

  $.ajax({
    type: "GET",
    url: "/username_check/",
    data: {
      username: r_username.val(),
    },
    dataType: "json",
    success: function (data) {
      // console.log("success");
      if (data.status == "404") {
        r_username.addClass("red-border");
      } else {
        r_username.removeClass("red-border");
      }
      // console.log(data.status);
    },
    error: function () {
      // console.log("Error");
    }
  });

});


function reg_validation() {
  if (fname.val() == "") {
    fname.addClass("red-border");
  } else {
    fname.removeClass("red-border");
  }
  if (lname.val() == "") {
    lname.addClass("red-border");
  } else {
    lname.removeClass("red-border");
  }
  if (r_username.val() == "") {
    r_username.addClass("red-border");
  } else {
    r_username.removeClass("red-border");
  }
  if (email.val() == "") {
    email.addClass("red-border");
  } else {
    email.removeClass("red-border");
  }
  if (r_pass.val() == "") {
    r_pass.addClass("red-border");
  } else {
    r_pass.removeClass("red-border");
  }

  if (
    fname.val() != "" &&
    lname.val() != "" &&
    r_username.val() != "" &&
    email.val() != "" &&
    r_pass.val() != ""
  ) {
    var csrftoken = getCookie("csrftoken");
    // console.log(csrftoken);

    $.ajax({
      type: "POST",
      url: "/signupjs/",
      data: {
        csrfmiddlewaretoken: csrftoken,
        fname: fname.val(),
        lname: lname.val(),
        username: r_username.val(),
        email: email.val(),
        pwd: r_pass.val()
      },
      dataType: "json",
      success: function (data) {
        console.log("success");
        if (data.status == "200") {
          location.href = home_url;
        } else {
          alert.removeClass("hide");
          $("#alert-text").text(
            "Username or Email already exists! Try another!"
          );
          alert_hide();
        }
        console.log(data.status);
      },
      error: function () {
        console.log("Error");
      }
    });
  }
  return false;
}

function login_validation() {
  if (luser.val() == "") {
    luser.addClass("red-border");
  } else {
    luser.removeClass("red-border");
  }

  if (lpass.val() == "") {
    lpass.addClass("red-border");
  } else {
    lpass.removeClass("red-border");
  }

  if (luser.val() != "" && lpass.val() != "") {
    var username = luser.val();
    var password = lpass.val();
    var csrftoken = getCookie("csrftoken");
    // console.log(csrftoken);

    $.ajax({
      type: "POST",
      url: "/loginjs/",
      data: {
        csrfmiddlewaretoken: csrftoken,
        username: username,
        password: password
      },
      dataType: "json",
      success: function (data) {
        console.log("success");
        if (data.status == "200") location.href = home_url;
        else {
          alert.removeClass("hide");
          alert_hide();
        }
      },
      error: function () {
        console.log("Error");
      }
    });
  }
  return false;
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function alert_hide() {
  setTimeout(function () {
    alert.addClass("hide");
  }, 5000);
}