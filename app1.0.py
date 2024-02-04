from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

class Task:
    def __init__(self, description, deadline, importance, time_taken, urgency_score=1):
        self.description = description
        self.deadline = deadline
        self.importance = importance
        self.time_taken = time_taken
        self.urgency_score = urgency_score

def optimize_todo_list(tasks):
    # Sort tasks based on deadline, importance, urgency_score, and time taken
    sorted_tasks = sorted(tasks, key=lambda x: (x.deadline, -x.importance * x.urgency_score, x.time_taken))

    # Display optimized to-do list
    print("Optimized To-Do List:")
    for task in sorted_tasks:
        print(f"Description: {task.description}")
        print(f"Deadline: {task.deadline}")
        print(f"Importance: {task.importance}")
        print(f"Urgency Score: {task.urgency_score}")
        print(f"Time Taken: {task.time_taken} hours")
        print("-------------")

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        deadline_str = request.form['deadline']
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
        importance = int(request.form['importance'])
        time_taken = int(request.form['time_taken'])
        urgency_score = float(request.form['urgency_score']) if 'urgency_score' in request.form else 1

        task = Task(description, deadline, importance, time_taken, urgency_score)
        tasks.append(task)

    sorted_tasks = sorted(tasks, key=lambda x: (x.deadline, -x.importance * x.urgency_score, x.time_taken))

    return render_template('index.html', tasks=sorted_tasks)

if __name__ == '__main__':
    app.run(debug=True)
