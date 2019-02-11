#!/bin/bash
at now +24 hours -f /home/neel_redkar/ExtempWebDownloader/uploader.sh
/home/neel_redkar/ExtempWebDownloader/updater.py
/home/neel_redkar/ExtempWebDownloader/dropbox_uploader.sh -s upload /home/neel_redkar/ExtempWebDownloader/ /
rm -r /home/neel_redkar/ExtempWebDownloader/20*
#Or run cron job and remove while and the sleep
#5 0 * * * ./uploader.sh
