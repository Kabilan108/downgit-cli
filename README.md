# DownGit CLI

DownGit CLI is a command-line interface tool that allows you to download files or directories from GitHub repositories using the [DownGit service](https://minhaskamal.github.io/DownGit/#/home?url=https:%2F%2Fgithub.com%2Fmodal-labs%2Fmodal-examples%2Ftree%2Fmain%2F06_gpu_and_ml%2Fopenai_whisper%2Fpod_transcriber). It is built with Python and uses Selenium WebDriver for browser automation.

## Installation

To install DownGit CLI use the command below:

```shell
pip install git+https://github.com/Kabilan108/downgit-cli.git
```

## Usage

To use DownGit CLI, you need to run the main.py script with the URL of the GitHub file or directory you want to download. Here is an example:

This will download the specified file or directory to the current working directory.

Please note that DownGit CLI uses the Brave browser for Selenium WebDriver. Make sure you have the Brave browser installed and its binary location is correctly specified in the main.py script.
