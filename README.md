# docker-container-scheduler

A small and effective docker container to schedule other containers to run.  
You might want to schedule container to create backup, to run heavy tasks, to execute automated checks or 
to perform clean-ups.

## Usage

The schedule is set through the `CONTAINERS_SCHEDULE` environment variable with a json array describing the container 
to schedule:
```json
[
    {
        "container": "container_name_1",
        "crontab": "*/1 * * * *"
    },
    {
        "container": "container_name_2",
        "crontab": "0 4 * * *"
    }
]
```

To debug your crontab expressions, keep an eye on [Crontab guru](https://crontab.guru/)

## Security implications

The container requires accessing the docker socket.  
This may have serious **security implications**. The scheduler container can take control of the docker host instance
and be able to download images, create new containers and run/stop/delete containers.  
You are strongly discouraged from giving the scheduler container any kind of external access (tcp/udp ports, 
sockets, etc). Please, use it only to schedule the run of other containers and take the surface attack as low 
as possible.

## Examples (compose.yaml)

The [compose.yaml](<https://github.com/yusefmaali/docker-container-scheduler/blob/master/compose.yaml>) file is a fully working example of a docker compose file.  
It will create three containers executing a simple bash script (`sh -c 'exit 0'`).  
The `scheduler` container will run the three containers every 1 min, every 2 mins and every 3 mins.  
Take a look at the logs to see how the scheduler works.

## Meta

Yusef Maali - contact@yusefmaali.net

Distributed under the MIT license. See [LICENSE.txt](<https://github.com/yusefmaali/docker-container-scheduler/blob/master/LICENSE.txt>) for more information.

https://github.com/yusefmaali/docker-container-scheduler
