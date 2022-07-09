from setuptools import setup

__version__ = "0.10.0.0"

setup(
    name="pyfujitseu",
    py_modules=["pyfujitseu"],
    version=__version__,
    description="Fujitsu Airconditioners",
    long_description="Python library to control Fujitsu General Airconditioners on AylaNetworks IoT platform",
    author="Mehdi Modarressi, Fabio Mauro",
    author_email="Luckposht@gmail.com",
    url="https://github.com/xerxes87/pyfujitseu",
    download_url="https://github.com/xerxes87/pyfujitseu",
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["ialarmXR", "antifurtocasa365", "alarm"],
    packages=["pyfujitseu"],
    include_package_data=True,
    install_requires=["requests", "certifi", "chardet", "idna", "urllib3"],
)
