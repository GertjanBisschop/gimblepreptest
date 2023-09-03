from setuptools import setup, find_packages

setup(
	entry_points={
        'console_scripts': [
            'gimblepreptest=cli.interface:main'
        ]
    },
    packages=["cli", "lib"],
    package_dir={
        "": ".",
        "cli": "./cli",
        "lib": "./lib",
    },
)