from postgres:11
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=testpass
ENV POSTGERS_DB=asgi_test
COPY db/create_asgi_test.sql /docker-entrypoint-initdb.d/
