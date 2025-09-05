import './App.css';
import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTitle, setNewTitle] = useState("");

  const fetchTasks = () => {
    axios.get("http://127.0.0.1:8000/tasks/")
      .then((res) => setTasks(res.data))
      .catch((err) => console.log(err));
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const toggleTask = (id, completed, title) => {
    axios.put(`http://127.0.0.1:8000/tasks/update/${id}/`, {
      title,
      completed: !completed
    })
    .then(fetchTasks)
    .catch(err => console.log(err));
  };

  const updateTask = (id, newTitle, completed) => {
    axios.put(`http://127.0.0.1:8000/tasks/update/${id}/`, {
      title: newTitle,
      completed
    })
    .then(fetchTasks)
    .catch(err => console.log(err));
  };

  const deleteTask = (id) => {
    axios.delete(`http://127.0.0.1:8000/tasks/delete/${id}/`)
      .then(fetchTasks)
      .catch(err => console.log(err));
  };

  const addTask = () => {
    if (newTitle.trim() === "") return;
    axios.post("http://127.0.0.1:8000/tasks/create/", {
      title: newTitle,
      completed: false
    })
    .then(() => {
      setNewTitle("");
      fetchTasks();
    })
    .catch(err => console.log(err));
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>My Tasks</h1>

      <input
        type="text"
        placeholder="Enter new task"
        value={newTitle}
        onChange={(e) => setNewTitle(e.target.value)}
      />
      <button onClick={addTask}>Add</button>

      <ul>
        {tasks.map(task => (
          <li key={task.id}>
            <strong>{task.title}</strong> – {task.completed ? "Done" : "Not Done"}

            <button onClick={() => toggleTask(task.id, task.completed, task.title)}>
              Toggle
            </button>

            <button onClick={() => {
              const newName = prompt("Update task title:", task.title);
              if (newName) updateTask(task.id, newName, task.completed);
            }}>
              Update
            </button>

            <button onClick={() => deleteTask(task.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
