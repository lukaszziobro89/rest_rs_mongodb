#
# Makefile
#


#===================================================
build-up:
	docker-compose --env-file .env up --build --force-recreate

build-up-dettached:
	docker-compose --env-file .env up --build -d

up:
	docker-compose --env-file .env up

up-dettached:
	docker-compose --env-file .env up -d

down:
	docker-compose down
