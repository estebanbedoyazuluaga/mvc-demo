const indentSpace = 4
const randId = (min, max) => Math.floor(Math.random() * (max-min)) + min

function getAllTasks() {
    fetch("/tasks")
        .then(res => res.json())
        .then(data => {
            document.getElementById("outputArea").textContent = JSON.stringify(data, null, indentSpace);
        })
        .catch(e => {
            console.log(e)
        })
}

function getTaskById() {
    const taskId = document.getElementById("taskId").value;
    if (taskId) {
        fetch(`/tasks/${taskId}`)
            .then(res => res.json())
            .then(data => {
                document.getElementById("outputArea").textContent = JSON.stringify(data, null, indentSpace);
            })
            .catch(error => {
                document.getElementById("outputArea").textContent = "Task not found";
            });
    }
}

function createTask() {
    const newTask = {
        id: randId(5, 1000),
        title: document.getElementById("newTaskTitle").value,
        description: document.getElementById("newTaskDescription").value
    };

    fetch("/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        // we're not displaying the text so no need to use the second and third fields
        body: JSON.stringify(newTask)
    })
        .then(res => res.json())
        .then(data => {
            document.getElementById("outputArea").textContent = JSON.stringify(data, null, indentSpace);
        });
}

function deleteTaskByID() {
    const taskId = document.getElementById("deleteTaskID").value
    if (taskId) {
        fetch(`/tasks/${taskId}`, {method: 'DELETE'})
            .then(res => res.json())
            .then(data => {
                document.getElementById("outputArea").textContent = JSON.stringify(data, null, indentSpace)
            })
    }
}