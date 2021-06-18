# Simulating Qiskit Runtime locally

The Dockerfile builds a container similar to the ones used by Qiskit Runtime.
By default it installs the Runtime sample program `sample_program`.

To use this local environment: 

1. Clone this repo.

1. Build the Docker image:

    ```
    cd runtime_local
    docker build -t runtime_local .
    ```

1. Start the Docker container:

   ```
   docker run --rm -it -d runtime_local
   ```
   
1. Dump program input parameters into a `params.json` file. 
A file is used because there is size limitation on stdin arguments.
For example the content of `params.json` may look like
   
   ```
   $ cat params.json
   {"iterations": 2}
   ```

1. Copy `params.json` into Docker container:

   ```
   docker cp ./params.json <CONTAINER>:/runtime/params.json
   ```

1. Invoke the runtime program:

   ```
   docker exec <CONTAINER> /runtime/program_starter.py
   ``` 

1. Kill your container when done:

   ```
   docker stop <CONTAINER>
   ```

There will be scripts to do all these steps.
