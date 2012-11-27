__author__ = 'matt'

"""
Ripped off 1 and 2 algorithm from Jeff.
I decided to add functions in the class to
convert between seconds and hms.
"""

class Time(object):
    """Stores time in hours minutes seconds"""
    def __init__(self, hours, minutes, seconds, timestamp=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.timestamp = timestamp
        self.to_seconds # Call to_seconds at construction to populate that value

    @property
    def to_seconds(self):
        """Convert time to seconds (from Jeff's Code"""
        self.timestamp = self.seconds + (self.minutes * 60) + (self.hours * 3600)
        return self.timestamp

    @property
    def to_hms(self):
        """Convert timestamp to hours minutes seconds"""
        """
        Why is this function returning None. It was because print_time()
        was a subroutine that printed a timestamp, as opposed to returning a value
        back to the caller, this function
        """
        totalTime = self.timestamp
        self.hours = totalTime / 3600
        totalTime -= self.hours * 3600
        self.minutes = (totalTime / 60)
        totalTime -= self.minutes * 60
        self.seconds = totalTime
        return print_time(self)

    def increment(self,inseconds):
        """increment a Time instance by a given number of seconds"""
        self.timestamp += inseconds
        self.to_hms

def print_time( t ) :
    """A function to print out a time"""
    assert isinstance(t, Time)
    return "%d:%02d:%02d" % (t.hours, t.minutes, t.seconds )

def is_after(t1, t2) :
    assert isinstance(t1, Time)
    assert isinstance(t2, Time)
    s1 = t1.to_seconds
    s2 = t2.to_seconds
#    return s2 > s1 # I think it's the other way?
    return s1 > s2

if __name__ == '__main__':
    # Create Example Times using a 24-hr Format
    t1 = Time(11,20,50)
    t2 = Time(15,20,10)

    # Test second conversion
    print 't1 seconds: %s' % t1.to_seconds
    print 't2 seconds: %s' % t2.to_seconds
    print is_after(t1,t2)

    # Test Time class methods. Convert from seconds to HMS and back.
    print t1.to_seconds
    print t1.to_hms
    print t1.to_seconds

    # Test Increment method.
    print print_time(t1)
    t1.increment(120)

    print getattr(t1, 'to_hms')
    print getattr(t1, 'hours')
