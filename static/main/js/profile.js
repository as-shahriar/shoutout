$('#edit-btn').click(function (e) {
    e.preventDefault();

    var text = $('#edit-btn').val();
    if (text == "Edit") {

        $(this).val("Save");
    } else {
        $(this).val("Edit");
    }

});