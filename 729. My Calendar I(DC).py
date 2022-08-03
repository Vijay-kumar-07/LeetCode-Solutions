# Question:

# You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

# A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

# The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

# Implement the MyCalendar class:

# MyCalendar() Initializes the calendar object.
# boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

# Input
# ["MyCalendar", "book", "book", "book"]
# [[], [10, 20], [15, 25], [20, 30]]
# Output
# [null, true, false, true]

# Explanation
# MyCalendar myCalendar = new MyCalendar();
# myCalendar.book(10, 20); // return True
# myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
# myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

class MyCalendar:

    def __init__(self):
        self.calendar = []
    def book(self, start, end):
        right = len(self.calendar)
        if right == 0:
            self.calendar.append((start, end))
            return True
        left = 0
        while left < right:
            mid = int(left + (right-left)/2)
            if self.calendar[mid][1] <= start:
                left = mid + 1
            else:
                right = mid
        if left == 0:
            if self.calendar[left][0] >= end:
                self.calendar.insert(0, (start, end))
                return True
            else:
                return False
        elif left == len(self.calendar):
            if self.calendar[left - 1][0] <= start:
                self.calendar.append((start, end))
                return True
            else:
                return False
        if left - 1 >= 0 and self.calendar[left-1][1] <= start and self.calendar[left][0] >= end:
            self.calendar.insert(left, (start, end))
            return True
        return False
        


# Your MyCalendar object will be instantiated and called as such:
obj = Mycalendar()
obj.book(10,20)
obj.book(25,35)
obj.book(50,60)
obj.book(61,63)
obj.book(21,27)