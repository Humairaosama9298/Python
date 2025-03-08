# To-Do List CLI App

A simple command-line interface (CLI) To-Do List application built using **Python** and **Click**.

---

## 🚀 Features
- Add new tasks
- List all tasks with status (✅ Completed / ❌ Pending)
- Mark tasks as complete
- Delete tasks
- Persistent storage using JSON file

---

## 📌 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Humairaosama9298/Python/tree/main/ramazan_coding_nights/todo-cli
cd todo-cli
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv .venv
```

### 3️⃣ Activate the Virtual Environment
#### Windows:
```sh
.venv\Scripts\activate
```
#### Mac/Linux:
```sh
source .venv/bin/activate
```

### 4️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 📜 Usage
### 1️⃣ Add a Task
```sh
python todo.py add "Go to Gym"
```
✅ Output:
```
Task Added Successfully: Go to Gym
```

### 2️⃣ List All Tasks
```sh
python todo.py list_tasks
```
✅ Output:
```
1. Go to Gym [❌]
```

### 3️⃣ Mark Task as Complete
```sh
python todo.py complete 1
```
✅ Output:
```
Task 1 marked as Complete. ✅
```

### 4️⃣ Delete a Task
```sh
python todo.py delete 1
```
✅ Output:
```
Removed task: Go to Gym
```

---

## 🛠 Dependencies
- **Python** (>=3.12)
- **Click** (For CLI functionality)

To install Click manually:
```sh
pip install click
```

---

## 💡 Contributing
Feel free to submit **issues** or **pull requests** if you want to improve this project! 😊

---

### 💻 Developed by [Humaira Osama](https://github.com/Humairaosama9298)
