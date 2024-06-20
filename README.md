# static web resume template
- this project is a web-based resume template application built using Python and Jinja2.
- generates an static html and a pdf version of your resume, allowing easy customization through provided assets.
- deploys and publishes website to branch `gh-pages`

## how to use
1. edit the files in the `assets` folder:
2. run `app.py`
3. files are generated in `dist` folder.

## installation

1. **create a new repo using this template**
2. **clone the previously created repo**
3. **create and activate virtual environment**

    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

4. **install dependencies**

    install the necessary python packages:

    ```sh
    pip install -r requirements.txt
    playwright install
    ```
