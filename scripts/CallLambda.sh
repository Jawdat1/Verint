

#!/bin/bash, calls Lambda to get http 200 from google.com every ten seconds for five minutes
x=1
while [ $x -le 3000 ]
do
	aws lambda invoke --function-name verintping response.json
	echo $x
	sleep 10
  x=$(( $x + 1 ))
done