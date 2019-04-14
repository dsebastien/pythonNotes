# Virtual environments

## Virtual what?

Virtual environments isolate a full python installation along with all the dependencies etc. Problem of Python: global installation version vs libraries, etc: mess.

A virtual environment also includes the python binaries and core libraries!

## Why?

Avoid global installations and side-effects of dependencies and transitive dependencies. Increase build stability/reproductibility.

## v-env module
Built-in module.

Example:

`python3 -m venv foo`

This creates a virtual environment called `foo` in a sub-folder.

## virtualenv and virtualenv-wrapper
Third-party projects.

## Miniconda
Integrates package management and virtual environment management as well.

# pyenv
Tool to manage multiple versions of python on the same machine. Similar to nvm for node.

https://github.com/pyenv/pyenv
https://github.com/pyenv/pyenv-installer

## pipenv
Nice tool that integrate package management and virtual environment management: https://pipenv.readthedocs.io/en/latest/

Useful commands:

* run command with environment loaded: `pipenv run <command>`
* open shell with environment loaded: `pipenv shell`
