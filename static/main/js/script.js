var luser = $("#username");
var lpass = $("#pass");
var alert = $("#alert-box");


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
        var csrftoken = getCookie('csrftoken');
        // console.log(csrftoken);

        $.ajax({
            type: "POST",
            url: '/loginjs/',
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'username': username,
                'password': password
            },
            dataType: 'json',
            success: function (data) {
                console.log("success");
                if (data.status == "200") location.href = "";
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
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
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