# Connect 4 Django Web App

This is a local web application built with Django that allows users to play the classic game Connect 4.

## Getting Started

To get started with the Connect 4 Django web app, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd connect_four
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:

      ```bash
      venv\Scripts\activate
      ```

    - For macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. If you haven't already, install the Vue.js CLI

    ```bash
    npm install -g @vue/cli
    ```

6. Run database migrations:

    ```bash
    python manage.py migrate
    ```

7. Start the development server:

    ```bash
    python manage.py runserver
    ```

8. Open your web browser and visit `http://localhost:8000` to access the Connect 4 web app.

## Specifications

The Connect 4 Django web app has the following specifications:

- Users can play Connect 4 against another player in the same browser tab.
- The game board is displayed on the web page.
- Users can make moves by clicking on the desired column.
- After each move is made, the game switches to the other player.
- The game ends when a player wins or the board is full.
- Users can view their game history and statistics (feature to be added in the future).