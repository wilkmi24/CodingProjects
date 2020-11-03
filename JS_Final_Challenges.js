function validateForm() {
    var x = document.forms["myForm"] ["phonenumber"].value;
    if (x =="") {
        alert("Phone number must be filled in");
        return false;
    }
}

function openForm() {
    document.getElementById("myForm2").style.display = "block";
} 
function closeForm() {
    document.getElementById("myForm2").style.display = "none";
}