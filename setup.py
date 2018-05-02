from setuptools import setup, find_packages

setup(
    name="Confs",
    version="0.1",
    packages=find_packages(),
    scripts=['main.py'],
    py_modules=['confs'],
    install_requires=[
        'click==6.7',
        'Jinja2==2.10',
        'MarkupSafe==1.0'
    ],
    package_data={
        '': ['README.md', 'LICENSE']
    },
    author="Kacper Kołodziej",
    author_email="kacper-confs@kolodziej.it",
    description="""Simple dotfile manager with support for multiple hosts and
    jinja templating""",
    license="GNU GPL v3",
    keywords="dotfiles manager",
    entry_points={
        'console_scripts': [
            'confs=main:main'
        ]
    }
)
