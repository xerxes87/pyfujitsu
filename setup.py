from setuptools import setup

__version__ = "0.10.0.0"

setup(
    name="pyfujitseu",
    py_modules=["pyfujitseu"],
    version=__version__,
    description="Fujitsu Airconditioners",
    long_description="Python Library for interacting with Fujitsu General split AC API",
    author="Mehdi Modarressi, Fabio Mauro",
    author_email="Luckposht@gmail.com",
    url="https://github.com/bigmoby/pyfujitseu",
    download_url="https://github.com/bigmoby/pyfujitseu",
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["Fujitsu Airconditioners"],
    packages=["pyfujitseu"],
    include_package_data=True,
    install_requires=["requests", "certifi", "chardet", "idna", "urllib3"],
)
