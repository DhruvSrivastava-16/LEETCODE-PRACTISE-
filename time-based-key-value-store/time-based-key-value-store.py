class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_dict = {}
        self.key_map = {}
        

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key in self.time_dict:
            self.time_dict[key].append(timestamp)
            self.key_map[key].append(value)
        else:
            self.time_dict[key] = [timestamp]
            self.key_map[key] = [value]
        
        
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key in self.time_dict:
            t_values = self.time_dict[key]
            index = bisect.bisect_right(t_values, timestamp)
            if index-1 == len(t_values) or index == 0:
                return ''

            return self.key_map[key][index-1]
        