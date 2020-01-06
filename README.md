**Scope**

http_server is used to test receiveing notifications

**Setup**
1. Setup Docker: [link](https://docs.docker.com/docker-for-windows/)
2. Setup Windows Linux Subsystem (WLS): [link](https://docs.microsoft.com/en-us/windows/wsl/install-win10)
3. Configure WLS to access Docker for Windows: [link](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)

**Start the server**

make httpserver - a new docker container running the server will launch

**Access the server**

Open a new browser instance and go to: [127.0.0.1:8080](127.0.0.1:8080)