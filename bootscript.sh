sudo systemctl restart hostapd
echo Restarted  Webservice

sudo startx & echo Starting GUI

while ! xset q &>/dev/null; do
    sleep 1
done

sudo xset dpms force off

sleep 5

/home/HubTVMC/start.sh & echo Starting Control Server
/home/scripts/minecraft.sh & echo Starting Minecraft
#______________________
#/home/HubTVMC/start.sh
#echo Started Control Server

#sleep 60 && /home/scripts/minecraft.sh
#echo Started Minecraft


#sudo xset dpms force on