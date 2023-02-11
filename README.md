## Setup

1. If you don’t have Python 3.7 installed, install it

2. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/Scripts/activate
   ```

3. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

4. Make a copy of the example environment variables file
   ```bash
   $ cp .env.example .env
   ```

5. Add your OpenAI API key to the newly created .env file

6. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)
