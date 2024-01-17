#!/bin/bash

# Install necessary dependencies
apt-get update
apt-get install -y postgresql-server-dev-all build-essential python3 python3-pip git

# Get PostgreSQL version
PG_VERSION=$(pg_config --version | grep -o -E '[0-9]+\.[0-9]+')
PG_CONFIG_PATH="/usr/pgsql-${PG_VERSION}/bin/pg_config"

# Clone psycopg2 source code
git clone https://github.com/psycopg/psycopg2.git
cd psycopg2

# Build and install psycopg2
python3 setup.py build_ext --pg-config "${PG_CONFIG_PATH}" build
python3 setup.py install

# Cleanup
cd ..
rm -rf psycopg2
