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