# get google cloud logging token and logging.writeenry to cloud logging


## steps

1. create the terraform gcloud build image in your own project
```
cd terraform
gcloud builds submit
```
2. create a service account and give it the pub/sub permission
3. give the cloud build default service account(project-number@cloudbuild.gserviceaccount.com) the cloud run admin and service account user permission at least
4. change the substitution in cloudbuild.yaml
    - _BUCKET: specifiy the terraform's state file in gcs
    - _REGION: cloud run's deployment region, default is us-central1
    - _IMAGE_NAME: image name in your project
    - _SA_MAIL: Service account email bind to the cloud run services
```
cd getLoggingToken
gcloud builds submit
```

