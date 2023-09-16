FROM ubuntu:22.04

LABEL author="Matthew Butner"
LABEL mainter="mfbutner@ucdavis.edu"

ARG DEBIAN_FRONTEND=noninteractive

# Python Environment Variables
ENV PYTHONIOENCODING=UTF-8
ENV PYTHONPATH=/grade/tests:/grade/serverFilesCourse

# pip Environment Variables
ENV PIP_ROOT_USER_ACTION=ignore

# Unit test style grader variables Environment Variables
ENV UTSG_RESULT_LOCATION=/grade/results/results.json
ENV UTSG_TESTS_LOCATION=/grade/tests/

# create a new user group and user to allow student run code to be run as a different user
RUN groupadd sbuser
RUN useradd -g sbuser sbuser



# install python and remove cache
RUN apt-get update && apt-get install -y  \
    acl \
    python3.11  \
    python3-pip  \
    python3.11-venv \
    && apt clean && rm -rf /var/lib/apt/lists/*



# make sure that our installed version of python3 is the one that gets run
RUN ln -sf /usr/bin/python3.11 /usr/bin/python3

# install the build dependencies
COPY build_requirements.txt /build_requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade --upgrade-strategy=eager -r /build_requirements.txt


# copy over the grader and build it
COPY unittest_style_grader /unittest_style_grader
# 1. Build
# 2. Install
# 3. make utsg_run_tests available everywhere
# 4. remove the dist file created in step 1 as it is no longer needed
# the reason I'm doing this instead of just python3 -m pip install --no-cache-dir /unittest_style_grader-1.0.0-py3-none-any.whl
# is that when I did that the package got installed as UNKNOWN and I can't figure out why
RUN python3 -m build /unittest_style_grader && \
    python3 -m pip install --no-cache-dir /unittest_style_grader/dist/unittest_style_grader-1.0.0-py3-none-any.whl && \
    ln -sf /usr/local/bin/utsg_run_tests /bin/utsg_run_tests && \
    rm -rf /unittest_style_grader/dist


