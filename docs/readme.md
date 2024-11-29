# How to 

## To build agent 

```
podman build -t mesop-app:latest .

```
## To run agent

```
podman run -d \
  --name agent \
  --network crew-network \
  --restart=always \
  --env-file /home/rbanda/mes-agent/crew-ai-agent/.env \
  crew-ai-agent:latest
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
  --network crew-network \
  -p 8080:8080 \
  mesop-app:latest

```
