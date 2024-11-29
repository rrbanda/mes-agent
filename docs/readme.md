# How to 

## To build agent 

```
podman build -t agent:latest .

```
## To run agent

```
podman run -d \
  --name agent \
  --network mes-agent \
  --restart=always \
  --env-file /home/rbanda/mes-agent/agent/.env \
  agent:latest
```

## To build App 
```
cd /home/rbanda/mes-agent/mesop-app/
podman build -t mesop-app:latest .
```
## To run app 

```
podman run -d \
  --name mesop-app-container \
  --network mes-agent \
  -p 8080:8080 \
  mesop-app:latest

```
