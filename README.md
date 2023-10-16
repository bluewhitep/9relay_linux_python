# 9relay_linux_python
**Use python control ADUBRU9 board on linux**

# Install
``` bash
git clone https://github.com/bluewhitep/9relay_linux_python
cd ./9relay_linux_python
pip install -r ./requirements.txt
```

# Usage
``` python
from 9relay_linux_python.relay import relay

relay_console = relay()

# all off
relay_console.all_off()

# all on
relay_console.all_on()

# single relay on/off
relay_console.on(relay_num=0)  # RY1 contorl
relay_console.off(relay_num=0) # RY1 contorl

# mutil relay on/off
relay_console.on(relay_num=[0,2,4])  # RY1,3,5 contorl
relay_console.off(relay_num=[0,2,4]) # RY1,3,5 contorl

# get relays status
print(relay_console.status) #0:off  1:on
```

# Document
```python
relay(idVendor:str="22ea", idProduct:str="005f", init="off")
'''
Args:
    idVendor (str, optional): USB Vendor ID. Defaults to "22ea".
    idProduct (str, optional): USB Product ID. Defaults to "005f".
    init (str, optional): Init method(off: all off; on: all on). Defaults to "off".
'''

.on(relay_num:int or list)
.off(relay_num:int or list)
  Args:
    relay_num (int or list): Will turn on /off of relay num. 0 to 8
  Raises:
    ValueError: relay_num must be 0 to 8
```

---
ADUBRU9 default infomation:
* Vendor ID: 0x22ea
* Product ID: 0x005f
  
