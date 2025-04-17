#!/bin/bash

# Create the main directory
mkdir -p customer-support-agent

# Create files in the main directory
touch customer-support-agent/docker-compose.yml
touch customer-support-agent/Dockerfile
touch customer-support-agent/.env
touch customer-support-agent/README.md

# Create subdirectories and files within them
mkdir -p customer-support-agent/workflows
touch customer-support-agent/workflows/main_workflow.json
touch customer-support-agent/workflows/error_handler.json

mkdir -p customer-support-agent/scripts
touch customer-support-agent/scripts/conversation_memory.py
touch customer-support-agent/scripts/priority_calculator.js

mkdir -p customer-support-agent/config
touch customer-support-agent/config/nginx.conf

mkdir -p customer-support-agent/data/redis