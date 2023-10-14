from datetime import datetime


class Log:
    """Format Cisco log message, ignores year in the Log message as that is not quote common."""
    def __init__(self, timestamp=None, facility=None,
                 severity_level=None, mnemonic=None, description=None):
        self._timestamp = timestamp
        self._facility = facility
        self._severity_level = severity_level
        self._mnemonic = mnemonic
        self._description = description

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = value

    @property
    def facility(self):
        return self._facility

    @facility.setter
    def facility(self, value):
        self._facility = value

    @property
    def severity_level(self):
        return self._severity_level

    @severity_level.setter
    def severity_level(self, value):
        self._severity_level = value

    @property
    def mnemonic(self):
        return self._mnemonic

    @mnemonic.setter
    def mnemonic(self, value):
        self._mnemonic = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def load_from_string(self, log_string):
        log_list = log_string.split(": ")
        if len(log_list) > 2:
            self.timestamp = datetime.strptime(log_list[0].strip("*"), "%b %d %H:%M:%S.%f")
            self.facility = log_list[1].split("-")[0]
            self.severity_level = int(log_list[1].split("-")[1])
            self.mnemonic = log_list[1].split("-")[2]
            self.description = log_list[2]

    def __str__(self):
        return (datetime.strftime(self.timestamp, "%b %d %H:%M:%S.%f") + " " + self.facility + "-" +
                str(self.severity_level) + "-" + self.mnemonic + ": " + self.description)

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.description == other.description
