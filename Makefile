SHELL=/bin/sh

common:
	docker --version
	docker-compose --version
	for c in $$(docker ps -a | grep httpserver | awk '{ print $$1 }'); do docker rm -v $$c -f; done
	for c in $$(docker images -a | grep httpserver | awk '{ print $$3 }'); do docker rmi $$c -f; done
		@echo ""
	@echo "================================================================="
	@echo "                   H T T P    S E R V E R                        "
	@echo "================================================================="
	@echo ""
	docker build -t httpserver:latest .

httpserver: common
	docker run -it -p 8080:80 --name httpserver httpserver