import typer
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tqdm import tqdm
from pathlib import Path


app = typer.Typer()


@app.command()
def download_from_downgit(url: str):
    cwd = Path.cwd()

    perfs = {
        "download.default_directory": f"{cwd}/",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "safebrowsing.disable_download_protection": True,
    }

    opts = Options()
    opts.binary_location = '/usr/bin/brave-browser'
    opts.add_argument("--headless=new")
    opts.add_experimental_option("prefs", perfs)

    driver = webdriver.Chrome(options=opts)

    try:
        driver.get(f"https://minhaskamal.github.io/DownGit/#/home?url={url}")
    finally:
        driver.quit()


if __name__ == "__main__":
    app()
