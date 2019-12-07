$(".delete-comment").click(function (e) {
    e.preventDefault();
    id = $(this).data("id");

    $.ajax({
        type: "POST",
        url: "/delte_comment/",
        data: {
            comment_id: id,
            csrfmiddlewaretoken: csrftoken,
        },
        dataType: "json",
        success: function (response) {
            if (response.status == "200") {
                $("#comment-" + id).fadeOut();
            } else {
                alert("Error in Comment Deletion.");
            }
        },
        error: function (response) {
            alert("No internet connection");
        }
    });

});


$(".comment-delete-btn").on("click", "a", function (e) {
    e.preventDefault();
    id = $(this).data("id");
    $.ajax({
        type: "POST",
        url: "/delte_comment/",
        data: {
            comment_id: id,
            csrfmiddlewaretoken: csrftoken,
        },
        dataType: "json",
        success: function (response) {
            if (response.status == "200") {
                location.reload();
            } else {
                alert("Error in Comment Deletion.");
            }
        },
        error: function (response) {
            alert("No internet connection");
        }
    });

});