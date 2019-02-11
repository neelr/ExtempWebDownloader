while [ 1 ]
do
    ./updater.py
    ./dropbox_uploader.sh -s upload ~/ExtempOffline/ /ExtempOffline
    rm -r 20*
    sleep 1d
done
#Or run cron job and remove while and the sleep
#5 0 * * * ./uploader.sh
