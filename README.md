# Flask Projects: 

This repository contains two Flask projects: LoginForm and Cafe. Each project focuses on different functionalities but shares a common Flask backend.

## LoginForm

### Goals
The primary goal of this project is to build advanced forms using Flask-WTF extension. This project introduces Flask developers to Flask-WTF for easy form validation, less code, and built-in CSRF protection.

### Secrets
The end result of this project is a website that holds some secrets. Access to these secrets is restricted by requiring the correct username and password.

## Cafe

### Goals
This project aims to utilize Flask-WTF, Bootstrap-Flask, and Bootstrap classes to enhance the user experience of a website displaying cafe information. It also involves revising CSV manipulation skills.

### Requirements
1. The home page should resemble the provided style using the `css/styles.css`.
2. The `/cafes` route should render a page (`cafes.html`) with a Bootstrap table displaying data from `cafe-data.csv`.
3. The location URL should be rendered as an anchor tag within the table.
4. Clicking "Show Me!" on the home page should navigate to `cafes.html`.
5. The secret route `/add` should render `add.html`.
6. Use Flask-WTF's `render_form` to create a form in `add.html` with validation for the location URL.
7. Upon successful form submission, data should be appended to `cafe-data.csv`.

### Additional Notes
- Ensure all navigation links within the website are functional.
- Read more about Flask-WTF [here](https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/).
- Bootstrap-Flask documentation can be found [here](https://bootstrap-flask.readthedocs.io/en/stable/macros/#render-form).
- For URL validation, refer to WTForms [validators](https://wtforms.readthedocs.io/en/2.3.x/validators/) documentation.
- Switch off client-side validation with `quick_forms` as per [this Stack Overflow post](https://stackoverflow.com/a/61166621/10557313).


## How to Run
1. Clone the repository.
2. Navigate to the project directory (`LoginForm` or `Cafe`).
3. Install dependencies (`pip install -r requirements.txt`).
4. Run the Flask application (`python app.py`).

