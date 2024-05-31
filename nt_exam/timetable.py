class Time:
    def __init__(self, hour, minute, seconds):
        self.hour = hour
        self.minute = minute
        self.seconds = seconds


class TimeTable(Time):
    def __init__(self, hour, minute, seconds, subject, classroom):
        super().__init__(hour, minute, seconds)
        self.subject = subject
        self.classroom = classroom


time_table1 = TimeTable(9, 0, 0, "Math", "Auditorium")
time_table2 = TimeTable(10, 0, 0, "English", "Classroom 1")
time_table3 = TimeTable(11, 0, 0, "Science", "Lab")
time_table4 = TimeTable(12, 0, 0, "History", "Classroom 2")
time_table5 = TimeTable(13, 0, 0, "Art", "Art Room")


def get_subject_at_time(time, time_tables):
    for tt in time_tables:
        if tt.hour == time.hour and tt.minute == time.minute and tt.seconds == time.seconds:
            return tt.subject
    return None


time_tables = [time_table1, time_table2, time_table3, time_table4, time_table5]

time = Time(10, 0, 0)
subject = get_subject_at_time(time, time_tables)
print(subject)  # prints: English
