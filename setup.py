from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='passgpy',
    version='1.0.0',
    license='MIT',
    author='Mattio-cmd',
    author_email='mattioc@protonmail.com',
    url='https://github.com/Mattio-cmd/',
    description='secure password generator written in python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=['rich'],
    keywords=['password', 'cli', 'security', 'python'],
)
