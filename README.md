#End to End Kubernetes deployment project

Steps:
1. Create simple HTTP server in python
2. Run you server Locally
3. Create a docker file for the app
4. Run your app locally using docker
5. Expose the app to the outside world
6. Wait 30 sec before start the server
7. Add a kubernetes health check toservertraffic only when the app is ready
8. Update the app to return a message from ConfigMap


```Creating Simple HTTP server```
a. Refer main.py for the code 
b. which contains simple class and a function to send response forever and if any keyboard interuption is there it will stop 

Once done create a python virtual environment
    ```python -m venv .venv```

Activate above created virtual environment for use 
    ```source ./.venv/bin/activate```

    if u are doing it via VS code u will get a notification to activate that enviromnet give yes

Then simply run the main.py file >> python main.py

Go to ur web and hit localhost:8080 to see Hello World!

This marks end of first step and second step

```Image Building```
docker build . -t username/name:tag
Refer all 4 Dockerfiles
1. Normal Docker file which is of size ~900mb
2. Slim-buster ~100mb
3. Debian based slim image ~50mb
4. Fourth file is a multistage build which uses requirements.txt, this is used if we need extra pip moduels/libs

Build these images and push them to docker hub(any Container registry)

Going forward we will using '3.DebainBasedSlimImamge' to deploy into the k8 cluster
