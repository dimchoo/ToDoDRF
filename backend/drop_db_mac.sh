#!/usr/bin/env bash
/Applications/Postgres.app/Contents/Versions/11/bin/psql -p5433 "template1" <<EOF
DROP DATABASE drf_db;
DROP USER drf_user;
EOF
exit