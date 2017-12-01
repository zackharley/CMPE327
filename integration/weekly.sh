#!/usr/bin/env bash

BANKING_DAYS_IN_A_WEEK=5

echo
echo "INTEGRATION: Running weekly banking simulation!"
echo
echo

for i in $(seq 1 ${BANKING_DAYS_IN_A_WEEK}); do
    echo "######## STARTING BANKING DAY ${i} ########"
    ./daily.sh
    echo
done

echo "INTEGRATION: Completed weekly banking simulation!"