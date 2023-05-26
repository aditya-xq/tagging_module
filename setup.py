from setuptools import setup

setup(
    name='tagging_module',
    version='0.0.6',
    author='aditya-xq',
    author_email='adityavivek.xq@gmail.com',
    description='A lightweight rule based tech content tagging module for Python',
    packages=['tagging_module'],
    package_data={
        'tagging_module': ['config/rules.yml'],
    },
    include_package_data=True,
    install_requires=[
        'PyYAML',
    ],
)
