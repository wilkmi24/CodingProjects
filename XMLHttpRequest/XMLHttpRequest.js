function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.openreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML = 
            this.responseText;
        }
    };
    xhttp.open("GET", "ajax_info.txt.rtf", true);
    xhttp.send();
}