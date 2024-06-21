# Web Resume builder
- Web-based resume template built using Python, Jinja2 as web template engine and Playwright Chromium for PDF generation.
- Generates a static website and a pdf of your resume, allowing easy customization through provided assets.
- Deploys and publishes website to branch `gh-pages`.

Demo: https://disaa0.github.io/web-resume

## How to use
1. Set up your own files in the `assets` folder.
2. Modify `templates/index.html` and `assets/styles.css` to your liking.
4. Run `app.py` in your virtual environment.
5. Files are generated to `dist` folder.
6. Website is deployed to Github Pages using branch `gh-pages`
7. You can access your website in https://`[github_username]`.github.io/`[repository_name]`
   - Note: naming the repository `[github_username].github.io` will publish the website to https://`[github_username]`.github.io

## Installation

1. **Create a new repo using this template**.
2. **Clone the previously created repo**.
3. **Create and activate virtual environment**.

    ```sh
    python -m venv .venv
    source .venv/bin/activate
    ```

4. **Install dependencies**.

    Install the necessary python packages:

    ```sh
    pip install -r requirements.txt
    playwright install
    ```
