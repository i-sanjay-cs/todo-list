```markdown
# Django To-Do List Application

## Description

This project is a modified version of an open-source Django to-do list application. The original project lacked user authentication, search functionality, and session management, which I have added. The enhancements made to the application include:

- **User Authentication:** Added registration, login, and logout functionality.
- **Search Functionality:** Implemented a search feature to filter tasks by title.
- **Session Management:** Ensured that users can only access their tasks after logging in.

Additionally, the application has been containerized using Docker and deployed on AWS Lambda for serverless execution.

## Features

- **User Registration and Authentication:** Users can register, log in, and manage their sessions.
- **Task Management:** Users can create, update, and delete tasks.
- **Search Tasks:** Users can search for tasks by title.

## Running the Application Locally

To run the application locally, follow these steps:

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/i-sanjay-cs/todo-list.git
   cd todo-list
   ```

2. **Build the Docker Image:**

   ```sh
   docker build -t my-django-app .
   ```

3. **Run the Docker Container:**

   ```sh
   docker run -p 8000:8000 my-django-app
   ```

   The application will be accessible at `http://localhost:8000`.

## Running on GitHub Codespaces

You can also run the application on GitHub Codespaces:

1. **Open the Repository in Codespaces:**
   - Click on the "Code" button in GitHub and select "Open with Codespaces".

2. **Build and Run the Docker Container:**

   Once inside the Codespace terminal, execute the following commands:

   ```sh
   docker build -t my-django-app .
   docker run -p 8000:8000 my-django-app
   ```

   The application will be available at the Codespaces URL provided.



## Tools and Resources

- **Django:** Web framework used for the application.
- **Docker:** Containerization tool used to package the application.
- **AWS Lambda:** Serverless compute service for deploying the application.
- **API Gateway:** Service to create and manage API endpoints for the Lambda function.

For any questions or issues, please refer to the GitHub repository or contact me.

