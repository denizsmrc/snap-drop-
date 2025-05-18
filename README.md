# Snapdrop Cloud-Native Implementation

This repository contains the cloud-native implementation of Snapdrop using Google Cloud Platform (GCP).

## Architecture Overview

The system consists of the following components:
- Frontend: Containerized in GKE (Google Kubernetes Engine)
- Backend: Containerized in GKE
- Load Balancer: Google Cloud Load Balancer
- Cloud Functions: For additional features
- Monitoring: Cloud Monitoring and Logging

## Prerequisites

1. Google Cloud Platform account with billing enabled
2. Google Cloud SDK installed
3. kubectl installed
4. Docker installed
5. Node.js and npm installed

## Deployment Steps

1. **Enable Required APIs**
```bash
gcloud services enable \
  container.googleapis.com \
  cloudfunctions.googleapis.com \
  cloudbuild.googleapis.com \
  monitoring.googleapis.com \
  logging.googleapis.com
```

2. **Create GKE Cluster**
```bash
gcloud container clusters create snapdrop-cluster \
  --num-nodes=3 \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --enable-autoscaling \
  --min-nodes=3 \
  --max-nodes=10
```

3. **Deploy Kubernetes Resources**
```bash
kubectl apply -f k8s/
```

4. **Deploy Cloud Function**
```bash
cd cloud-functions/file-stats
gcloud functions deploy file-stats \
  --runtime nodejs16 \
  --trigger-http \
  --allow-unauthenticated
```

## Performance Testing

1. Install Locust:
```bash
pip install locust
```

2. Run performance tests:
```bash
locust -f locustfile.py
```

3. Open http://localhost:8089 in your browser to start the test

## Monitoring

Access the following dashboards in Google Cloud Console:
- Kubernetes Engine > Workloads
- Cloud Monitoring > Dashboards
- Cloud Logging > Logs Explorer

## Cost Optimization

The deployment is optimized to stay within the $300 GCP trial budget:
- Using e2-medium instances for cost efficiency
- Implementing proper resource limits
- Using autoscaling to scale down during low traffic
- Monitoring resource usage through Cloud Monitoring

## Security Considerations

- All services are deployed within a private VPC
- HTTPS is enabled for all external communications
- Resource limits are set to prevent DoS attacks
- Regular security updates are applied to container images

## Troubleshooting

1. Check pod status:
```bash
kubectl get pods
```

2. View pod logs:
```bash
kubectl logs <pod-name>
```

3. Check Cloud Function logs:
```bash
gcloud functions logs read file-stats
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
