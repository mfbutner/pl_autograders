FROM richardsmashington/unittest_style_grader:latest

LABEL author="Matthew Butner"
LABEL mainter="mfbutner@ucdavis.edu"

RUN apt-get update && apt-get install -y  \
    g++   \
    gcc  \
    valgrind \
    make \
    cmake && \
    apt clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt


