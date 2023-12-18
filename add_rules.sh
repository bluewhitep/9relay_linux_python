sudo echo "SUBSYSTEMS==\"usb\", ATTRS{idVendor}==\"22ea\", ATTRS{idProduct}==\"005f\", GROUP=\"users\", MODE=\"0666\"
" > /etc/udev/rules.d/10-9relay.rules

sudo udevadm control --reload-rules && sudo udevadm trigger
