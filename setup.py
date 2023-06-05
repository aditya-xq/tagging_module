from setuptools import setup

setup(
    name='tagging_module',
    version='0.0.8',
    author='aditya-xq',
    author_email='adityavivek.xq@gmail.com',
    description='A lightweight rule based tech content tagging module for Python',
    packages=['tagging_module', 'tagging_module.config'],
    package_data={
        'tagging_module': ['config/rules.yml'],
    },
    include_package_data=True,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'PyYAML',
    ],
)
