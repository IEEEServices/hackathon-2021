FROM python:3.8-slim
RUN apt-get update && apt-get -y install --reinstall build-essential python3-dev libopenblas-dev git wget && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install qiskit matplotlib
RUN pip install $(pip freeze 2>/dev/null| grep aqua | sed -e 's/==/[torch,pyscf]==/')
RUN pip install https://github.com/rpmuller/pyquante2/archive/master.zip
RUN pip install cvxopt
RUN mkdir /runtime
WORKDIR /runtime
COPY ./program_starter.py .
COPY ./sample_program.py program.py
RUN chmod -R go+rw /runtime
RUN chmod +x program_starter.py
CMD /bin/bash
