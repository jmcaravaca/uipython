# UIPython

Example project to use UIPath Orchestrator API in python. Boilerplate is done and examples are provided.
Authorization is based on OAuth2 flows, using Authlib.
This project uses swagger codegen for the API clients, see [my API client](https://github.com/TaruDesigns/UIPathAPI)

# Authorization

By default, client_credentials auth is setup. The id and secret are stored in config/secrets.py but it is recommended to use environment variables instead.
