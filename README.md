
a command to gather and list google compute engine machine types

this basically only does:

``` bash
gcloud compute machine-types list
```

but is actually fast after the first occurence and the sort options work

# usage

``` bash
gce fetch
gce list --name n2-highcpu-16
gce list --zone europe-west1-b
gce list --cpu 4
gce list --cpu "<4"
gce list --cpu ">4"
gce list --memory 128
gce list --memory "<128"
gce list --memory ">128"
gce list --by memory,cpu --ascending false,true
```
