FROM n8nio/n8n:1.24.0

# Install Python dependencies
RUN apk add --no-cache python3 py3-pip && \
    python3 -m pip install faiss-cpu numpy sentence-transformers

# Copy custom scripts
COPY scripts/ /data/scripts/
COPY workflows/ /data/workflows/

# Set environment variables
ENV N8N_BASIC_AUTH_ACTIVE=true
ENV N8N_BASIC_AUTH_USER=admin
ENV N8N_BASIC_AUTH_PASSWORD=SuperSecret123!
ENV N8N_WEBHOOK_URL=https://your-domain.com