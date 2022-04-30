$( document ).ready(function() {
    $("#name").html(getValue("name"));

});
function logout() {
    $.ajax({
        url: "/crm/v1/token-logout",
        type: "GET",
        success: function (result, status, xhr) {
            if (status === "success") {
                deleteAuth()
                window.location.href = "/";
            }
        }
    })
}

function createItem(key, value) {
    localStorage.setItem(key, value);
}

function getValue(key) {
    return localStorage.getItem(key);
}

function deleteAuth() {
    localStorage.removeItem("token");
    localStorage.removeItem("role");
}
