
a command to gather and list google compute engine machine types

this basically only does:

``` bash
gcloud compute machine-types list
```

but is actually fast after the first occurence and the sort options work

# install

``` bash
pip install git+https://github.com/gmanchon/gce_machine_type
```

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
gce list --zone europe-west1-b --cpu ">4" --memory "<256" --by memory,cpu --ascending false,true
```
