# Development environment installation and config

## Install all prereqs

### Docker and Docker compose
* Docker: we use it to run/host our dependencies (and we deploy to it too)
* Docker compose: we use it to easily run our application
  * https://docs.docker.com/compose/install/

### pyenv
We use it to manage Python versions and stay isolated from the operating system managed version (e.g., under *nix).

* official repo: https://github.com/pyenv/pyenv
* easy to use installer: https://github.com/pyenv/pyenv-installer

Don't forget to add it to your shell config:
```
export PYENV_ROOT=$HOME/.pyenv
append_to_path $PYENV_ROOT/bin
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

### Python
With pyenv installed: `pyenv install <version>`.
Check the `.python-version` file to know which one is needed.

That installs it on your system but *does not activate it globally by default*.

If the install fails, you might also need other libs. Take a look at the `Dockerfile` for the full list.

TIP: If you adapt the python version in the .python-version file, then you'll also need to rebuild the container.

### pip
Will be installed by pyenv along with Python, but you might want to have it available globally. You can do that using `pyenv global <python version>`.

### pipenv
We use pipenv to manage project dependencies and locking to have deterministic builds.

Installation is easy: `pip install --user pipenv`

## Build your local development container
Execute the following script:

```
chmod +x ./util_create.sh
./util_create.sh
```

NOTE: If you need to recreate the container, do use the script, and not `docker-compose build` directly! Otherwise the required environment variables / arguments won't be available / up to date.

## Deploy locally with Docker
You can start the local Docker containers using:

```
chmod +x ./util_start.sh
./util_start.sh
```

## Install your local environment

### Using Docker as a remote interpreter (recommended)
Cleanest as it does not depend on your local environment.

For pyCharm / IntelliJ, see here: https://www.jetbrains.com/help/pycharm/using-docker-as-a-remote-interpreter.html

### Using your local environment
If you can't work with Docker as a remote interpreter, then you can install everything locally.

Run ´pipenv install --dev` from the project root folder.

pipenv will:
* create a virtualenv for you under ~/.local/share/virtualenvs/...-<hash of your local path>
* install everything for you, including the development tools (e.g., black, pytest, etc)

Once installed, either run commands using `pipenv run ...`, or open a shell with the virtual environment activated using `pipenv shell`

## Install the git hooks for code style and formatting
Run `pre-commit install` to install the hooks.

Once done, whenever you commit something, the script will execute and will automatically fix the code formatting and perform checks (see readme).
