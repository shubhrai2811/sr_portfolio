#!/bin/bash

# Install necessary dependencies
apt-get update
apt-get install -y postgresql-server-dev-all build-essential

# Clone psycopg2 source code
git clone https://github.com/psycopg/psycopg2.git
cd psycopg2

# Build and install psycopg2
python setup.py build_ext --pg-config /usr/pgsql-<version>/bin/pg_config build
python setup.py install

# Cleanup
cd ..
rm -rf psycopg2
