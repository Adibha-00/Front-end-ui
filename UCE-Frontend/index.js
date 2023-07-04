var subjectObject = {
    "LIST": {
      "listacls" : [],
      "listscope" : []
    },
    "UPDATE": {
      "updatepassword": [],
      "updatepermission": ["READ", "WRITE", "MANAGE"]
    },
    "CREATE": {
        "SCOPECREATE" : []
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

 /* function convertjson() {
      const form = document.getElementById('data');
      const formData = new FormData(form);
      const jsonObject = Object.fromEntries(formData);
      const jsonString = JSON.stringify(jsonObject);
      console.log(jsonString); 
  
  };*/
   

        const form = document.getElementById('data');
        const resultDiv = document.getElementById('result');

        form.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(form);
            fetch('/process_form', {     /*forms a POST request to the python server, with the form data as response body */ 
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                resultDiv.innerHTML = data.result;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });