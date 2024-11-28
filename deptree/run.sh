#!/bin/bash

function get_files() {
    # depTree1

    curdir=$(pwd)
    project_dir="/home/wkaczurba/git/dashboard/backend"
    cd ${project_dir}
    mvn compile dependency:tree -DoutputFile=${curdir}/depTree1 
    cd ${curdir}
}

#function flatten() {
#    echo 'dupa'
#    # /home/wkaczurba/dashboard/backend/pom.xml
#}

# TODO: Change it so uses arg params
python3 process.py

