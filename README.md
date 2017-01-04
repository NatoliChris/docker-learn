# Learning Docker

## Tutorials Followed:

- https://prakhar.me/docker-curriculum/

## What is docker

1. Container deployment, all packages and dependencies in a box
2. A sandbox?
3. Deployment of VMs, carry the OS around to easily mark and deploy all parts.

## Terminology

- *Images*: application blueprints (through ``docker pull``)
- *Containers*: Created from docker **Images**
- *Docker Daemon*: The background process running docker
- *Docker Client*: The command line interacting with daemon
- *Docker Hub*: Registry of docker images, need to sign up for the service: https://hub.docker.com

## Docker

### Run command

```
docker run
```

Runs a command inside a container, it may be running a specific item, launching a web service
or many different possibilities.

Example: ``docker run hello-world``

#### Interacting with Containers

You can interact using the ``-i`` flag, but to open a ``tty`` then you can do something like:

```
docker run -it container_here sh
```

### Listing Docker Machines Running

``docker ps`` or ``docker ps -a`` will show the open containers and what is running.

