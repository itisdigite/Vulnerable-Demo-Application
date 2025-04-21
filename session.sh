#!/bin/bash

echo "Starting the Secure Coding Practices Demo"
python3 setupdb.py
echo "1. Input Validation and Output Encoding"
python3 app.py
echo -e "\nExecution Complete!"
echo "============================================================================================================"


echo "2. Authentication and Password Management"
python3 authentication.py
echo -e "\nExecution Complete!"
echo "============================================================================================================"


echo "3. Session Management"
cd Session_Access_Crypto
python3 user_app.py & pid1=$!
python3 admin_app.py & pid1=$!
echo "Running scripts with PIDs: $pid1 and $pid2"
wait $pid1
wait $pid2
echo -e "\nExecution Complete!"
echo "============================================================================================================"


echo "4. Access Control"
python3 access_control_admin.py & pid1=$!
python3 access_control_user.py & pid1=$!
echo "Running scripts with PIDs: $pid1 and $pid2"
wait $pid1
wait $pid2
echo -e "\nExecution Complete!"
echo "============================================================================================================"

echo "5. Cryptographic Practices"
python3 crypto_demo_app.py 
echo -e "\nExecution Complete!"
echo "============================================================================================================"
