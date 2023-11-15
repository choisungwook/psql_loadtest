CONTAINER_NAME = postegresql_test
POSTGRES_PASSWORD = password
POSTGRES_DB = test

up:
	@docker run --name=${CONTAINER_NAME} -d -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} -e POSTGRES_DB=${POSTGRES_DB} postgres:12-alpine

down:
	@docker kill ${CONTAINER_NAME}
	@docker rm ${CONTAINER_NAME}

get_max_connections:
	@PGPASSWORD=${POSTGRES_PASSWORD} docker exec -it ${CONTAINER_NAME} psql -U root -d ${POSTGRES_DB} -h 127.0.0.1 -c "SHOW max_connections;"

get_current_connections:
	@PGPASSWORD=${POSTGRES_PASSWORD} docker exec -it ${CONTAINER_NAME} psql -U root -d ${POSTGRES_DB} -c "SELECT pid,state FROM pg_stat_activity;"
