from netmiko import ConnectHandler


class Connectivity:
    """Implemented using netmiko
    Required Parameters: hostname/ip, username, password
    Optional: enable secret - if required by remote device,
    session_log - filename to record session logs
    Output Formats: List/Dictionary
    """
    
    def __init__(self, host, username, password, enable_secret=None, session_log=None):
        self.host = host
        self.username = username
        self.password = password
        self.enable_secret = enable_secret
        self.session_log = session_log

    def set_connection_params(self, device_type):
        connection_params = {
            "device_type": device_type,
            "host": self.host,
            "username": self.username,
            "password": self.password            
        }
        if self.enable_secret:
            connection_params["secret"] = self.enable_secret
        if self.session_log:
            connection_params["session_log"] = self.session_log
        return connection_params

    def send_show_command_cisco(self, command):       
        with ConnectHandler(**self.set_connection_params("cisco_ios")) as net_connect:
            return net_connect.send_command(command, use_textfsm=True)
        
    def send_config_command_cisco(self, commands):
        """Requried Params: python list of commands
        Return: String indicating commands run and build configuration status
        """

        with ConnectHandler(**self.set_connection_params("cisco_ios")) as net_connect:
            output = net_connect.send_config_set(commands)
            output += net_connect.save_config()
        return output


    
