from locust import HttpUser, task, between
import random
import json

class SnapdropUser(HttpUser):
    wait_time = between(1, 5)
    
    def on_start(self):
        """Initialize user session"""
        self.client.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    @task(3)
    def browse_peers(self):
        """Simulate browsing for peers"""
        self.client.get("/")
    
    @task(2)
    def send_text(self):
        """Simulate sending text messages"""
        text_data = {
            "text": f"Test message {random.randint(1, 1000)}"
        }
        self.client.post("/send", json=text_data)
    
    @task(1)
    def send_file(self):
        """Simulate sending files"""
        # Create a small test file
        file_data = {
            "name": f"test_file_{random.randint(1, 1000)}.txt",
            "type": "text/plain",
            "size": random.randint(1000, 10000),
            "content": "Test content" * 100
        }
        
        # Send file metadata
        self.client.post("/send", json=file_data)
        
        # Simulate file transfer
        self.client.post("/file-stats", json={
            "size": file_data["size"],
            "type": file_data["type"],
            "transferSpeed": f"{random.randint(1, 10)}MB/s",
            "transferTime": f"{random.randint(1, 5)}s"
        })

    @task
    def test_endpoint(self):
        self.client.post("/test", json={"test": "data"}) 