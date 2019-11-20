var csrftoken = getCookie("csrftoken");

$("#gender").hide();
$("#blood").hide();

$('#edit-btn').click(function (e) {
    e.preventDefault();

    var text = $('#edit-btn').val();
    if (text == "Edit") {
        document.getElementById("fname").readOnly = false;
        document.getElementById("lname").readOnly = false;
        document.getElementById("pro").readOnly = false;
        document.getElementById("city").readOnly = false;
        document.getElementById("cell").readOnly = false;
        document.getElementById("email").readOnly = false;
        $("#gender-show").hide();
        $("#blood-show").hide();
        $("#gender").show();
        $("#blood").show();
        $(this).val("Save");
    } else {

        $.ajax({
            type: "POST",
            url: "/profile_update/",
            data: {
                csrfmiddlewaretoken: csrftoken,
                f_name: $("#fname").val(),
                l_name: $("#lname").val(),
                profession: $("#pro").val(),
                city: $("#city").val(),
                cell: $("#cell").val(),
                email: $("#email").val(),
                blood: $("#blood").val(),
                gender: $("#gender").val(),
            },
            dataType: "json",
            success: function (data) {
                if (data.status == "200")
                    $("#full_name").text($("#fname").val() + " " + $("#lname").val());
                $("#gender-show").val($("#gender").val());
                $("#blood-show").val($("#blood").val());
            },
            error: function () {
                console.log("Error");
            }
        });










        $(this).val("Edit");
        $("#gender-show").show();
        $("#blood-show").show();
        $("#gender").hide();
        $("#blood").hide();
        document.getElementById("fname").readOnly = true;
        document.getElementById("lname").readOnly = true;
        document.getElementById("pro").readOnly = true;
        document.getElementById("city").readOnly = true;
        document.getElementById("cell").readOnly = true;
        document.getElementById("email").readOnly = true;
    }

});


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


$("#email").change(function (e) {
    $.ajax({
        type: "GET",
        url: "/email_check/",
        data: {
            email: $("#email").val(),
        },
        dataType: "json",
        success: function (data) {
            // console.log("success");
            if (data.status == "404") {
                $("#email").addClass("red-border");
            } else {
                $("#email").removeClass("red-border");
            }
            // console.log(data.status);
        },
        error: function () {
            // console.log("Error");
        }
    });

});



$("#submit-post").click(function (e) {
    e.preventDefault();
    var post = $("#text-post").val()
    var html = $("#recent-post").html();
    const monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"
    ];

    var user = $('#username').val();
    var img = $('#img_url').val();
    var today = new Date();
    var time = monthNames[(today.getMonth())] + ', ' + today.getDate() + ', ' + today.getFullYear();

    new_html = '<div class="panel panel-default post"> <div class="panel-body"> <div class="row"> <div class="col-sm-2"> <a class="post-avatar thumbnail" href="profile.html"><img src="' + img + '"> <div class="text-center">' + user + '</div> </a> <div class="likes text-center">0 Like</div> </div><!-- col-sm-2 end --> <div class="col-sm-10"> <div class="bubble"> <div class="pointer"> <p>' + post + '</p> </div> <div class="pointer-border"></div> </div><p class="post-actions"><a href="#">Like</a> - <a href="#">Comment</a> - <a href="#">Follow</a> - <a href="#">Delete</a></p> <p class="time">' + time + '</p> <div class="comment-form"> <form class="form-inline"> <div class="form-group"> <input type="text" class="form-control" id="exampleInputName2" placeholder="Enter Comment"> </div> <button type="submit" class="btn btn-default">Add</button> </form> </div><div class="clearfix"></div> </div> </div> </div> </div> ';
    html = new_html + html;

    if (post.length == 0) {
        $(".post-status-f").show();
        setTimeout(function () {
            $(".post-status-f").fadeOut();
        }, 5000);
    } else {
        $.ajax({
            type: "POST",
            url: "/new_post/",
            data: {
                post: post,
                csrfmiddlewaretoken: csrftoken,
            },
            dataType: "json",
            success: function (data) {
                console.log("success");
                if (data.status == '200') {
                    $("#recent-post").html(html);
                    $(".post-status-s").show();
                    setTimeout(function () {
                        $(".post-status-s").fadeOut();
                    }, 5000);
                } else {
                    $(".post-status-f").show();
                    setTimeout(function () {
                        $(".post-status-f").fadeOut();
                    }, 5000);
                }
            },
            error: function (data) {
                $(".post-status-f").show();
                setTimeout(function () {
                    $(".post-status-f").fadeOut();
                }, 5000);
            }
        });

    }

});