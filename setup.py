from setuptools import setup, find_packages


setup(
    name='downgit',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'downgit=downgit.main:app'
        ]
    },
    install_requires=[
        'typer',
        'selenium',
        'requests',
        'tqdm',
        'webdriver_manager'
    ]
)