#!/bin/bash

# Set current directory
PWD=`pwd`

# Change to directory where the database is located
cd logbook

# Perform SQL Dump
pg_dump logbookdb > logbook_export

# Change back to original directory
cd $PWD