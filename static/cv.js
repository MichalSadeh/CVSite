function myName() {
    var text = "My name is Michal Sadeh";
    document.getElementById("button").innerHTML = text;
}

function valid() {
    const inpObj = document.getElementById("phone");
    if (!inpObj.checkValidity()) {
        document.getElementById("demo").innerHTML = inpObj.validationMessage;
    } else {
        document.getElementById("demo").innerHTML = "Input OK";
    }
}