pip install .
# Do not use a trailing slash on GRAFANA_URL
export GRAFANA_URL={INSERT URL}
export GRAFANA_TOKEN={INSERT TOKEN}

grafana-backup save --components=folders,dashboards,datasources,alert-channels
