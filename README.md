# Run
Check `Makefile` for specific Docker commands.
## Linux
Using make:

1. `make build`  
2. `make run`  
3. `make stop`

## Windows

1. To build - `docker build -t rcr-app`  
2. To run - `docker run --name rcr-app -d -p 80:80 rcr-app`  
3. To stop - `docker stop rcr-app`.