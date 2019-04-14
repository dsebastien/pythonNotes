# Dependency management

## Miniconda
https://docs.conda.io/en/latest/miniconda.html

## pipenv (preferred)
https://pipenv.readthedocs.io/en/latest/

Manages dependencies through a Pipfile containing groups of dependencies, expected python version, etc.
Can block installation of non-stable releases.

Also supports a lock file: Pipfile.lock.

Manages virtual environments and integrates nicely with pyCharm.

Useful commands:

* install deps: `pipenv install`
* install deps including dev ones: `pipenv install -d`
* update lock file: `pipenv lock`
* update all installed dependencies: `pipenv sync -d`
* run script declared in Pipfile: `pipenv run script_name`
* dependency tree: `pipenv graph`
