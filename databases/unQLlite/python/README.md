Docker Commands

 `docker-compose up --build`

Note: `docker-compose` file already has the entry point command to start a jupyter notebook and map port `8888` to localhost

Connecting VS-CODE to JUPYTER notebook server running on docker compose command

* click on select kernel on top right
* connect to remote server
* past the url along with auth token from compose logs

e.g.

`http://127.0.0.1:8888/?token=01593ab1c5cc5f9783561d63342382f2ac505c41546d2fae`

