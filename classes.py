class TimeInitException(Exception):
    pass

class Schedule:
    def __init__(self, start_time, duration, weekday=None):
        """(Time, Time, int)"""
        self.start_time = start_time
        self.end_time = start_time + duration
        self.weekday = weekday

class Time:
    def __init__(self, hour=None, minute=None, total_minutes=None):
        # this would be so much more elegant with method overloading
        if hour is None and minute is None and total_minutes is None:
            raise TimeInitException("You cannot leave all the parameters blank")
        elif hour is not None and minute is not None and total_minutes is not \
        None:
            raise TimeInitException("You must specify EITHER hour and minute \
                    OR total_minutes, not both")
        elif (hour is None and minute is not None) or (hour is not None and \
                minute is None):
            raise TimeInitException("You must specify both hour and minute")

        # now the cases where everything is correct
        elif hour is not None and minute is not None:
            self.hour = hour
            self.minute = minute
        else: # total_minutes is not None
            self.hour = total_minutes // 60
            self.minute = total_minutes % 60

    def __add__(self, other):
        return Time(total_minutes=self._to_minutes()+other._to_minutes())

    def __sub__(self, other):
        return Time(total_minutes=self._to_minutes()-other._to_minutes())

    def __eq__(self, other):
        return self.hour == self.minute and other.hour == other.minute
    
    def __ne__(self, other):
        return not self == other
    
    def __lt__(self, other):
        return self._to_minutes() < other._to_minutes()

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other
    # NOTE: There is a better way to do what you just did
    
    def __repr__(self):
        return "{}:{:02d}".format(self.hour, self.minute)

    def __str__(self):
        return repr(self)

    def _to_minutes(self):
        return self.hour * 60 + self.minute
