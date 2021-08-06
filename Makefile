#
# Makefile
#


#===================================================
build-up:
	$(info ================================  docker-compose BUILD + UP ================================)
	#docker-compose --env-file .env up --build
	docker-compose --env-file .env up --build --force-recreate
build-up-dettached:
	$(info ================================  docker-compose BUILD + UP dettached ================================)
	docker-compose --env-file .env up --build -d

up:
	$(info ================================  docker-compose UP ================================)
	docker-compose --env-file .env up

up-dettached:
	$(info ================================  docker-compose UP dettached ================================)
	docker-compose --env-file .env up -d

down:
	$(info ================================  docker-compose DOWN ================================)
	docker-compose down
