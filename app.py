import yaml, shutil, os, asyncio, shutil
from datetime import datetime
from jinja2 import Environment, PackageLoader, select_autoescape
from playwright.async_api import async_playwright
env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape(enabled_extensions=('html'))
)

def read_data(filename):
    with open(filename, 'r') as file:
        data = yaml.safe_load(file)
    return data

def get_updated():
    now = datetime.now()
    updated = date_string = now.strftime("%B %d, %Y")
    return updated


def remove_dir(output_path: str):
    if os.path.isdir(output_path):
        shutil.rmtree(output_path)

def write_html(file: str, output_path: str):
    with open(output_path + 'index.html', 'w') as f:
        f.write(file)

def copy_assets(assets_path: str, output_path: str):
    assets = ["photo.jpg", "favicon.ico", "styles.css"]
    for asset in assets:
        source_path = assets_path + asset
        destination_path = output_path + asset
        if os.path.isfile(source_path):
            shutil.copyfile(source_path, destination_path)
        else:
            print(f"Error: File {source_path} does not exist.")

async def url_to_pdf(url, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('file:///' + url, wait_until='networkidle')
        await page.pdf(
            path=output_path,
            format='A4',
            margin={
                'top': '2.54cm',
                'right': '2.54cm',
                'bottom': '2.54cm',
                'left': '2.54cm'
            },
            print_background=True,
            
            )
        await browser.close()

assets_path = "./assets/"
output_path = "./dist/"

template = env.get_template("index.html")
data = read_data('assets/metadata.yaml')
updated = get_updated()
pdf_name = data["pdf_name"]

resume = template.render(data=data, updated=updated)

remove_dir(output_path)
os.mkdir(output_path)

write_html (resume, output_path)

copy_assets(assets_path, output_path)

index_path = os.path.abspath(output_path+'index.html')
asyncio.run(url_to_pdf(index_path, output_path=output_path + pdf_name))