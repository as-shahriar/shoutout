alert_hide();

function login_validation() {
    if (document.getElementById('username').value != '' && document.getElementById('pass').value != '') {
        return true;
    }
    $("#alert-box").removeClass("hide");
    alert_hide();
    return false;
}

function reg_validation() {
    if (document.getElementById('fname').value != '' && document.getElementById('lname').value != '' && document.getElementById('reg_username').value != '' && document.getElementById('reg_pass').value != '' && document.getElementById('email').value != '') {
        return true;
    }
    $("#alert-box").removeClass("hide");
    alert_hide();
    return false;
}

function alert_hide() {
    setTimeout(function () {
        $("#alert-box1").addClass("hide");
        $("#alert-box").addClass("hide");
    }, 5000);
}