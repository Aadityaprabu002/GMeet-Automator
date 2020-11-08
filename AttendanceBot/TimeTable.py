import datetime
class TT:
    def __init__(self):
        self.day = ''
        self.date = ''
        self.schedule = dict()
        self.subject_order_list = []

    def set_day_schedule(self):
        self.date = datetime.datetime.now().strftime("%d")+'-'+datetime.datetime.now().strftime("%m")+'-'+datetime.datetime.now().strftime("%y")
        self.day =  datetime.datetime.now().strftime("%A")
        n = int(input('Enter number of clases today:'))
        for i in range(n):
            subject = input('Enter the subject {}:'.format(i + 1))
            print('Please carefully enter time in this format: HH-SS (24 hour format)')
            start = input('Enter the start time:')
            end = input('Enter the end time:')
            URL = input('Enter the URL / Try to copy and paste:')
            self.subject_order_list.append(subject)
            self.schedule[subject] = {
                'start': start,
                'end': end,
                # 'duration' : duration,
                'URL': URL,
                'date':self.date,
                'day':self.day
            }

