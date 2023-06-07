var subjectObject = {
    "List": {
      "ListCls" : [],
      "ListScope" : []
    },
    "Update": {
      "Update Password": [],
      "Update Permission": ["Read", "Write", "Manage"]
    },
    "Create": {
        "Scope Create" : []
      }
  }
  window.onload = function() {
    var subjectSel = document.getElementById("operation");
    var topicSel = document.getElementById("subOperation");
    var chapterSel = document.getElementById("permission");
    for (var x in subjectObject) {
      subjectSel.options[subjectSel.options.length] = new Option(x, x);
    }
    subjectSel.onchange = function() {
      //empty Chapters- and Topics- dropdowns
      chapterSel.length = 1;
      topicSel.length = 1;
      //display correct values
      for (var y in subjectObject[this.value]) {
        topicSel.options[topicSel.options.length] = new Option(y, y);
      }
    }
    topicSel.onchange = function() {
      //empty Chapters dropdown
      chapterSel.length = 1;
      //display correct values
      var z = subjectObject[subjectSel.value][this.value];
      for (var i = 0; i < z.length; i++) {
        chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
      }
    }
  }

  function printSelectedValues() {
    event.preventDefault();
    var operation = document.getElementById("operation").value;
    var subOperation = document.getElementById("subOperation").value;
    var permission = document.getElementById("permission").value;
    var region = document.getElementById("region").value;
    var environment = document.getElementById("environment").value;
    var email = document.getElementById("email").value;
    var token = document.getElementById("token").value;
    var scope = document.getElementById("scope").value;
    if (token === "" || scope === ""){
        alert("Please fill in all the compulsory fields.");
        return;
      }
    var result = "Operation: " + operation + "<br>" +
                 "SubOperation: " + subOperation + "<br>" +
                 "Permission: " + permission + "<br>" +
                 "Region: " + region + "<br>" +
                 "Environment: " + environment + "<br>" +
                 "Email: " + email +  "<br>";

    document.getElementById("result").innerHTML = result;
  }