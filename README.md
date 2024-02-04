# Optimo - To-Do List Optimization

## Description

Optimo is a Flask-based web application that helps users manage their tasks by optimizing the to-do list based on various criteria such as deadline, importance, urgency score, and time taken. The application provides a user-friendly interface for adding tasks and dynamically displays an optimized to-do list.

## Features

- **Task Management:** Users can add tasks with details such as name, deadline, impact score (importance), urgency score, and time taken.
  
- **Optimization Algorithm:** The to-do list is dynamically optimized using a sorting algorithm based on the following criteria:
  - **Deadline:** Tasks are sorted in ascending order of deadlines.
  - **Importance and Urgency:** Tasks are further sorted by a combination of importance and urgency score in descending order.
  - **Time Taken:** If deadlines, importance, and urgency scores are equal, tasks are sorted by time taken in ascending order.

## How to Use

1. Launch the Flask application by running the provided Python script (`app.py`).
2. Access the application through a web browser at `http://127.0.0.1:5000/`.
3. Add tasks using the "Add Task" form, providing task details and submitting the form.
4. The tasks will be dynamically displayed in an optimized order on the main page.

## Technologies Used

- **Flask:** Web framework for building the backend server.
- **HTML and CSS:** Frontend development for the user interface.
- **JavaScript:** Used for client-side interactivity, such as adding tasks and marking them as done.
- **Swiper Library:** Used for swipeable card elements in the user interface.

## Code Structure

- `app.py`: The main Flask application script.
- `templates/index.html`: HTML template for rendering the web page.
- Inline JavaScript in the HTML file for handling user interactions.

## Demo

A live demo of the application can be accessed on the provided local server. Follow the steps under "How to Use" for testing the application.

## Notes

- The application is a basic demonstration and may not include advanced features like user authentication or persistent storage of tasks.

Feel free to explore, modify, and enhance the code for your specific needs!
