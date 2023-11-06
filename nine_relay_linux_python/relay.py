import hid
# pip install hidapi

class relay:
    def __init__(self, idVendor:str="22ea", idProduct:str="005f", init="off") -> None:
        """relay controller

        Args:
            idVendor (str, optional): USB Vendor ID. Defaults to "22ea".
            idProduct (str, optional): USB Product ID. Defaults to "005f".
            init (str, optional): Init method(off: all off; on: all on). Defaults to "off".
        """
        # vendor ID str to 16bit int
        self.idVendor = int(idVendor, 16)
        
        # product ID str to 16bit int
        self.idProduct = int(idProduct, 16)
        
        self.status = [0] * 9
        self.h = hid.device()
        self.h.open(self.idVendor, self.idProduct)
        if init == "on":
            self.all_on()
        else:
            self.all_off()
            
    def __get_index(self, target):
        index_list = []
        for index, value in enumerate(self.status):
            if value == target:
                index_list.append(index)
        return index_list
    
    def on(self, relay_num:int or list) -> None:
        """ Relay on

        Args:
            relay_num (int or list): Will turn on of relay num. 0 to 8
        Raises:
            ValueError: relay_num must be 0 to 8
        """
        if type(relay_num) == int:
            if relay_num < 0 or relay_num > 8:
                raise ValueError("relay_num must be 0 to 8")
            
            send_buffter = [0] * 65
            send_buffter[1] = 0x33
            send_buffter[2] = relay_num
            send_buffter[3] = 1
            
            self.h.write(send_buffter)
            self.status[relay_num] = 1
            
        elif type(relay_num) == list:
            if len(relay_num) > 0 and len(relay_num) > 9:
                raise ValueError("relay_num list lenght must be 1 to 9")
            for i in relay_num:
                if i < 0 or i > 8:
                    raise ValueError("relay_num must be 0 to 8")
            
            last_status = self.__get_index(1)
            relay_num.extend(last_status)
            
            send_buffter = [0] * 65
            send_buffter[1] = 0x32
            send_buffter[2] = 9
            for num in relay_num:
                send_buffter[num + 3] = 1
                
            self.h.write(send_buffter)
            for num in relay_num:
                self.status[num] = 1
        
    def off(self, relay_num:int or list) -> None:
        """ Relay off

        Args:
            relay_num (int or list): Will turn off of relay num. 0 to 8
        Raises:
            ValueError: relay_num must be 0 to 8
        """
        if type(relay_num) == int:
            if relay_num < 0 or relay_num > 8:
                raise ValueError("relay_num must be 0 to 8")
            
            send_buffter = [0] * 65
            send_buffter[1] = 0x33
            send_buffter[2] = relay_num
            send_buffter[3] = 0
            
            self.h.write(send_buffter)
            self.status[relay_num] = 0
            
        elif type(relay_num) == list:
            if len(relay_num) > 0 and len(relay_num) > 9:
                raise ValueError("relay_num list lenght must be 1 to 9")
            for i in relay_num:
                if i < 0 or i > 8:
                    raise ValueError("relay_num must be 0 to 8")
            
            send_buffter = [0] * 65
            send_buffter[1] = 0x32
            send_buffter[2] = 9
            
            last_status = self.__get_index(1)
            for num in last_status:
                send_buffter[num + 3] = 1
            for num in relay_num:
                send_buffter[num + 3] = 0
            
            self.h.write(send_buffter)
            for num in relay_num:
                self.status[num] = 0
            
    def all_on(self) -> None:
        self.on([0,1,2,3,4,5,6,7,8])
        
    def all_off(self) -> None:
        self.off([0,1,2,3,4,5,6,7,8])
        
    def get_status(self) -> list:
        return self.status.copy()