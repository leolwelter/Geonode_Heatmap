#!/bin/bash
# deploy to geonodes-map.info
# run this from the root of the project
rsync -Pav -e "ssh -i ~/.ssh/lelotechnical-keys.pem" --exclude-from=deploy-ignore.txt "${PWD}" ubuntu@geonodes-map.info:~