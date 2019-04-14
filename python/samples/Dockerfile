# This arg is declared before any FROM so that it is globally available (i.e., also for the COPY --from)
# Reference: https://github.com/docker/for-mac/issues/2155#issuecomment-372639972
ARG BUILD_PYTHON_VERSION
ARG BUILD_USERNAME=dummy
ARG BUILD_UID=1000
ARG BUILD_GID=1000

FROM developassion/pyenv-pipenv-python:${BUILD_PYTHON_VERSION} as base_image_python

FROM developassion/ubuntu:1.0

LABEL author="Sebastien Dubois <seb@dsebastien.net>"
LABEL description="Basic starting point for Python projects"

# We need to pass down the variables
ARG BUILD_PYTHON_VERSION
ARG BUILD_USERNAME
ARG BUILD_UID
ARG BUILD_GID

ENV PYTHON_VERSION=${BUILD_PYTHON_VERSION}
ENV USERNAME=${BUILD_USERNAME}
ENV UID=${BUILD_UID}
ENV GID=${BUILD_GID}
ENV HOME=/home/${USERNAME}

# Home for the project files
ENV PROJECT_HOME=${HOME}/src

USER root

RUN groupadd --gid 1000 --non-unique ${USERNAME} \
    && useradd --create-home --home-dir /home/${USERNAME} --uid ${UID} --gid ${GID} --non-unique --shell /bin/bash ${USERNAME} \
    && chown -R ${USERNAME} ${HOME}

WORKDIR ${HOME}

RUN mkdir -p ${PROJECT_HOME} \
    && apt-get update && apt-get -y install \
    libhunspell-dev \
    libicu-dev \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p ${PROJECT_HOME}

# extract binaries from our base python image
# get pyenv, python, pipenv and pip
COPY --from=base_image_python ${HOME_ROOT}/.pyenv ./.pyenv
# get pipenv
COPY --from=base_image_python ${HOME_ROOT}/.local ./.local

COPY --from=base_image_python ${HOME_ROOT}/.bashrc ./.bashrc

COPY ./run-app.sh run-app.sh

# pyenv: define the variables here because we're using a multi-stage build
# so those are not retrieved
# reference: https://cloud.docker.com/u/developassion/repository/docker/developassion/pyenv-pipenv-python
ENV PYENV_ROOT=${HOME}/.pyenv

# pyenv: add to path as well as locally installed packages
ENV PATH=${PYENV_ROOT}/shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:$PATH

# Load our pipfile
COPY ./Pipfile Pipfile
COPY ./Pipfile.lock Pipfile.lock
COPY ./.python-version .python-version

RUN chown -R ${USERNAME}:${USERNAME} ${HOME} \
    #&& find ${HOME}/.local -type f -exec sed -i -e "s@${HOME_ROOT}@${HOME}@g" {} \; \
    #&& find ${HOME}/.pyenv -type f -exec sed -i -e "s@${HOME_ROOT}@${HOME}@g" {} \;
    && sed -i -e "s@${HOME_ROOT}@${HOME}@g" ${HOME}/.local/bin/pipenv \
    && sed -i -e "s@${HOME_ROOT}@${HOME}@g" ${HOME}/.pyenv/shims/python \
    && sed -i -e "s@${HOME_ROOT}@${HOME}@g" ${HOME}/.pyenv/shims/pip \
    && sed -i -e "s@${HOME_ROOT}@${HOME}@g" ${HOME}/.pyenv/versions/${PYTHON_VERSION}/bin/pip \
    && sed -i -e "s@${HOME_ROOT}@${HOME}@g" ${HOME}/.pyenv/pyenv.d/exec/pip-rehash/pip

RUN cat ${HOME}/.local/bin/pipenv

# install dependencies globally
# deploy ensures that the lock file is up to date. If not, it'll fail the image build
RUN pipenv install --system --deploy

USER ${USERNAME}

CMD source $HOME/run-app.sh
