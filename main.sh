# !/bin/bash
pwd=`pwd`

searchTerms(password code secret key pass open word login logon user username name account passphrase otp OTP FTP mason token userID id userid unlock cheat dictionary randomness hardword word hard)

echo Your directory is: $pwd
`echo ls` >> $pwd/outputs/learn.txt
echo What challenge number are you attempting?
read chalNum

# search for keywords in directory
# if keyword matches directory name, log in console
# create tally for "hits"
# in future, if hits is higher for certain directories that lead to key
# tell program to target those directories sooner than directories with less hits

for VARIABLE in $(searchTerms)
do 
   for OUTPUT in $ls $pwd
   do
    if $OUTPUT = $VARIABLE
        echo found `$OUTPUT` 'in' $pwd

done




