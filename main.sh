# !/bin/bash
pwd=`pwd`

searchTerms=(password code secret key pass open word login logon user username name account passphrase otp OTP FTP mason token userID id userid unlock cheat dictionary randomness hardword word hard)

echo Your directory is: $pwd
`echo ls` >> $pwd/outputs/learn.txt
echo What challenge number are you attempting?
read chalNum
hits=0

# search for keywords in directory
# if keyword matches directory name, log in console
# create tally for "hits"
# in future, if hits is higher for certain directories that lead to key
# tell program to target those directories sooner than directories with less hits

# Cause a glob with no results to result in empty output, rather than to evaluate
# back to itself.
shopt -s nullglob

# Expand the glob /Applications/*Adobe* into an array
dir_array=($pwd/)

# Trim the prefix /Applications/ from each element of that array
dir_array=( "${dir_array[@]}" )

# Iterate over that array

for i in "${searchTerms[@]}"
do 
  for OUTPUT in $ls
    if [["$i" == "$OUTPUT"]]
        $hits=$hits+1
        echo $OUTPUT >> $pwd/ouputs/learn.txt
    fi
done




