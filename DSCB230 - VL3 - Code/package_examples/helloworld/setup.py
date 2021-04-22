from setuptools import setup

setup(
    name='helloworld',
    version='0.0.1',
    description='Say hello!',
    py_modules=['helloworld'],
    package_dir={'':'src'},
    install_requires = [
        "pandas>=1.1.0"
    ]
)