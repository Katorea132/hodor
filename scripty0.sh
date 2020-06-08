#!/bin/bash
for i in `seq 1 1030`; do curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "id=1&holdthedoor=Submit+Query" http://158.69.76.135/level0.php & done

