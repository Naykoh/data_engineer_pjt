start docker-compose up

while true
do

    if curl --output /dev/null --silent --head --fail http://localhost:5000/
    then
        echo "Online"
        break
    else
        echo "Offline"
        sleep 5
    fi
done

C:\\Users\\$USERNAME\\anaconda3\\python.exe test_app.py
sleep 50