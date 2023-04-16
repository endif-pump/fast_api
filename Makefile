build:
	docker build -t fast-api:test -f docker/Dockerfile .

start:
	docker-compose -f ./docker/docker-compose.yaml up -d

stop:
	docker-compose -f ./docker/docker-compose.yaml down

restart: stop start
