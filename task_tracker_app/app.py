from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize an empty list to store task objects
tasks = []
task_id_counter = 1 # To generate unique task IDs

def add_task(text):
    """Adds a new task to the tasks list."""
    global task_id_counter
    new_task = {
        'id': task_id_counter,
        'text': text,
        'completed': False
    }
    tasks.append(new_task)
    task_id_counter += 1
    return new_task

def get_all_tasks():
    """Returns the list of all tasks."""
    return tasks

def complete_task(task_id):
    """Marks a task as completed."""
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return True
    return False # Task not found

def delete_task(task_id):
    """Deletes a task from the tasks list."""
    global tasks
    initial_len = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    return len(tasks) < initial_len # Return True if a task was deleted

@app.route('/')
def index():
    """Main page, displays all tasks."""
    all_tasks = get_all_tasks()
    return render_template('index.html', tasks=all_tasks)

@app.route('/add', methods=['POST'])
def add_task_route():
    """Handles adding a new task."""
    task_text = request.form['task_text']
    add_task(task_text)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task_route(task_id):
    """Marks a task as complete."""
    complete_task(task_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task_route(task_id):
    """Deletes a task."""
    delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
