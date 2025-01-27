# Prerequisite

1) Install docker
2) Run RabbitMq docker container locally using this command docker run -d --hostname haroldjcastillo --name rabbit-server -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=admin -p 5672:5672 -p 1
5672:15672 rabbitmq:3-management
3) import this code either in pycharm vscode
4) first run rabbitmq_consumer.py then run websocket_server.py
5) i used ngrok to expose the websocket to public
6) run the CI workflow file in git actions which will call the websocket server

   Runs a Python script directly in the GitHub Actions workflow.
The script:
Connects to the WebSocket server.
Sends a message ("Hello from GitHub Actions!").
Waits for a response and measures the response time.
Prints the response and response time to the workflow logs.
