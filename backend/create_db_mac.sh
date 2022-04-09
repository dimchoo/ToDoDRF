#!/usr/bin/env bash
/Applications/Postgres.app/Contents/Versions/11/bin/psql -p5433 "template1" <<EOF
CREATE DATABASE drf_db;
CREATE USER drf_user with NOSUPERUSER PASSWORD 'DRF_pass123!';
GRANT ALL PRIVILEGES ON DATABASE drf_db TO drf_user;
ALTER ROLE drf_user SET CLIENT_ENCODING TO 'UTF8';
ALTER ROLE drf_user SET default_transaction_isolation TO 'READ COMMITTED';
ALTER ROLE drf_user SET TIME ZONE 'Europe/Moscow';
ALTER USER drf_user CREATEDB;
EOF
exit
