build:
	docker build -t nodejs0 .
# docker run -p 는 [로컬에서 열 port]:[docker에서의 port] 입니다.
run:
	docker run -it -d -p 5200:5000 --env-file ../.env --name nodejs0 nodejs0
exec:
	docker exec -it nodejs0 /bin/bash
logs:
	docker logs nodejs0
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi $$(docker images -q)
