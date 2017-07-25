# !bin/bash

echo Hello World!!
echo

echo filename: $0
echo first parameter: $1
echo second parameter: $2
echo quoted values: $@
echo quoted values: $*
echo total parameters: $#
echo

cacota=10

limite=10

readonly limit
readonly cacota

echo cacota = $cacota
echo limite = $limite

if [ $cacota > $limite ]
then  echo mas de diez
else if [ $cacota == $limite ]
then echo diez justos
else echo menos de diez
fi fi
