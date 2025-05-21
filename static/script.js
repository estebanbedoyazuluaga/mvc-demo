const indentSpace = 4
const randId = (min, max) => Math.floor(Math.random() * (max - min)) + min

function getAllTasks() {
    fetch("/tasks")
        .then(res => res.json())
        .then(data => {
            document.getElementById("outputArea").textContent = JSON.stringify(data, null, indentSpace);
        })
        .catch(err => {
            document.getElementById("outputArea").textContent = "An error occurred. \n" + err;
        }).finally(data => {
            delete document.getElementById("outputArea").dataset.highlighted;
            hljs.highlightAll()
        })
}

function getTaskById() {
    const taskId = document.getElementById("taskId").value;

    fetch(`/tasks/${taskId}`)
        .then(res => res.json())
        .then(data => {
            document.getElementById("outputArea").textContent = JSON.stringify(data, null, indentSpace);
        })
        .catch(err => {
            document.getElementById("outputArea").textContent = "An error occurred. \n" + err;
        }).finally(data => {
            delete document.getElementById("outputArea").dataset.highlighted;
            hljs.highlightAll()
        });

}

function createTask() {
    const newTask = {
        task_id: randId(4, 99),
        title: document.getElementById("newTaskTitle").value,
        description: document.getElementById("newTaskDescription").value
    };

    fetch("/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newTask)
    })
        .then(res => res.json())
        .then(data => {
            document.getElementById("outputArea").textContent = JSON.stringify(data, null, indentSpace);
        })
        .catch(err => {
            document.getElementById("outputArea").textContent = "An error occurred. \n" + err;
        }).finally(data => {
            delete document.getElementById("outputArea").dataset.highlighted;
            hljs.highlightAll()
        });
}

function deleteTaskByID() {
    const taskId = document.getElementById("deleteTaskID").value
    fetch(`/tasks/${taskId}`, { method: 'DELETE' })
        .then(res => res.json())
        .then(data => {
            document.getElementById("outputArea").textContent = JSON.stringify(data, null, indentSpace)
        })
        .catch(err => {
            document.getElementById("outputArea").textContent = "An error occurred. \n" + err;
        }).finally(data => {
            delete document.getElementById("outputArea").dataset.highlighted;
            hljs.highlightAll()
        });
}
