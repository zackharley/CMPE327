#!/usr/bin/env bash

SESSIONS_PER_DAY=3
cd ..
VALID_ACCOUNTS_FILE="$(pwd)/shared/valid_accounts_file.txt" # from the root of the project
cd integration

echo "INTEGRATION: Running daily banking simulation!"
echo

for i in $(seq 1 ${SESSIONS_PER_DAY}); do
    echo "INTEGRATION: Running daily banking simulation frontend session ${i}"
    python3 generate_random_input_file.py ${VALID_ACCOUNTS_FILE} > ${TMPDIR}/input${i}.txt
    cd ..
    python3 -m frontend ${VALID_ACCOUNTS_FILE} ${TMPDIR}/input${i}.txt
    echo
    cd integration
done

echo "INTEGRATION: Running daily banking simulation backend session"
cd ..
python3 -m backend
cd integration
echo
echo
