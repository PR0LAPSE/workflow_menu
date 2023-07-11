import { app } from "/scripts/app.js";

var selectWorkflow = document.createElement("select");
selectWorkflow.id = "select_wotkflow";
selectWorkflow.style.width = "100%";
var chooseFileOption = document.createElement("option");
chooseFileOption.value = "";
chooseFileOption.text = "воркфлоу не выбран";
selectWorkflow.appendChild(chooseFileOption);
selectWorkflow.addEventListener("change", function() {
  if (this.value === "") {
    app.clean();
    app.graph.clear();
  } else {
    var selectedFile = this.value;
  
    fetch(selectedFile)
      .then(response => response.json())
      .then(data => {
        app.loadGraphData(data);
      })
      .catch(error => {
        console.error("ошибка загрузки воркфлоу из JSON:", error);
      });
  }
});

fetch("/extensions/workflow_menu/workflows_paths.txt")
  .then(response => response.text())
  .then(data => {
    var files = data.split("\n");
    files.forEach(file => {
      var option = document.createElement("option");
      option.value = file;
      option.text = file.split("/").pop().replace(".json", "");
      selectWorkflow.appendChild(option);
    });
  })
  .catch(error => {
    console.error("список воркфлоу не удалось загрузить:", error);
  });


var saveButton = document.querySelector("#comfy-save-button");
saveButton.parentNode.insertBefore(selectWorkflow, saveButton);