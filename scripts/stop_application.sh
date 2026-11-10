#!/bin/bash
docker stop flask-api || true
docker rm flask-api || true