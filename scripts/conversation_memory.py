import os
import sys
import argparse
import json
from sentence_transformers import SentenceTransformer
import numpy as np
import redis

# Initialize connections
r = redis.Redis(host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'))
model = SentenceTransformer('all-MiniLM-L6-v2')

def store_conversation(email, message):
    # Get conversation history
    history = r.get(f"conv:{email}") or b'[]'
    history = json.loads(history)
    
    # Generate embedding
    embedding = model.encode(message).tolist()
    
    # Store in Redis
    history.append({
        "message": message,
        "embedding": embedding
    })
    
    r.setex(f"conv:{email}", 86400, json.dumps(history))  # 24h retention

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--customer-email', required=True)
    parser.add_argument('--message', required=True)
    args = parser.parse_args()
    
    store_conversation(args.customer_email, args.message)