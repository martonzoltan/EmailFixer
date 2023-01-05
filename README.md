# OpenAI API Email Fixer

This is an example email fixer app using OpenAI API. You give it an email an it will make it more professional and less toxic. It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd chatgptdemo
   ```

4. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

5. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

6. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)!
