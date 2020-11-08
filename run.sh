start docker build -t sentiment_analysis .
sleep 10
start docker run -p 5000:5000 sentiment_analysis
sleep 5

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

C:\\Users\\nana-\\anaconda3\\envs\\data_engineering\\python.exe test_app.py
C:\\Users\\nana-\\anaconda3\\envs\\data_engineering\\python.exe src/test/test_process_and_predict.py
sleep 50