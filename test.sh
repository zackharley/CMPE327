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
    -o|--output)
    OUTPUT="$2"
    shift # past argument
    shift # past value
    ;;
esac
done

TIMESTAMP=$(date "+%Y.%m.%d-%H.%M.%S")

if ! [ ${OUTPUT} ]; then
    OUTPUT="frontend/test/logs/test.${TIMESTAMP}.log"
fi

echo "TEST SESSION -- ${TIMESTAMP}" > ${OUTPUT}
echo "" >> ${OUTPUT}

if ! [[ ${FRONTEND} ||  ${BACKEND} ]]; then
    echo "You must supply a path to at least a frontend or backend test folder"
    exit
fi

if [ ${FRONTEND} ]; then
    for folder in $( ls ${FRONTEND} ); do
        for file in $( find ${FRONTEND}/${folder} -name "*.input.txt" -print0 | xargs -0 ls); do

            echo "######  Running test ${file}  ######" >> ${OUTPUT}
            ACCOUNTS_FILE=$(echo ${file} | awk -F'[.]' '{print $1}' ).accounts.txt
            OUTPUT_FILE_NAME=$(echo ${file} | awk -F'[.]' '{print $1}').output.txt
            OUTPUT_FILE=$(find ${FRONTEND}/${folder} -name "$(echo ${OUTPUT_FILE_NAME} | awk -F'[/]' '{print $4}')")
            python3 -m frontend ${ACCOUNTS_FILE} ${file}  >> ${OUTPUT} 2>&1
            echo "" >> ${OUTPUT}


            TEST_NAME=$(echo ${file} | awk -F'[.]' '{print $1}' | awk -F'[/]' '{print $4}')
            SUMMARY_FILE=$(find frontend/sessions -name "*.${TEST_NAME}.txt" -print0 | xargs -0 ls -t | head -1)
            if [ ${OUTPUT_FILE} ]; then
                echo "######  comparing ${SUMMARY_FILE} ${OUTPUT_FILE}"
                if cmp -b -s ${SUMMARY_FILE} ${OUTPUT_FILE}; then
                   echo "The files match"
                else
                   echo "The files are different"
                fi
                diff ${SUMMARY_FILE} ${OUTPUT_FILE}
                echo ""
            fi
        done
    done

    # Diff output files and logs
fi

if [ ${BACKEND} ]; then
    cd ${BACKEND}
    pwd
    # loop here
fi

echo "done"