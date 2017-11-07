#!/usr/bin/env bash

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case ${key} in
    -f|--frontend)
    FRONTEND="$2"
    shift # past argument
    shift # past value
    ;;
    -b|--backend)
    BACKEND="$2"
    shift # past argument
    shift # past value
    ;;
esac
done

if ! [[ ${FRONTEND} ||  ${BACKEND} ]]; then
    echo "You must supply a path to at least a frontend or backend test folder"
    exit
fi

if [ ${FRONTEND} ]; then
    for folder in $( ls ${FRONTEND} ); do
        for file in $( find ${FRONTEND}/${folder} -name "*.input.txt" -print0 | xargs -0 ls); do

            echo "######  Running test ${file}  ######"
            ACCOUNTS_FILE=$(echo ${file} | awk -F'[.]' '{print $1}' ).accounts.txt
            python3 -m frontend ${ACCOUNTS_FILE} ${file}
            echo ""
        done
    done
fi

if [ ${BACKEND} ]; then
    cd ${BACKEND}
    pwd
    # loop here
fi

echo "done"