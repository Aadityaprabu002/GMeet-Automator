import GoogleBot
from GoogleBot import time
from TimeTable import datetime

def WaitToStart(subject):
    s_time = subject['start'].split('-')
    TimeNow = datetime.datetime.now()

    while int(s_time[0]) >= int(TimeNow.strftime('%H')) and int(s_time[1]) > int(TimeNow.strftime('%M')):
        time.sleep(5)
        TimeNow = datetime.datetime.now()


    print('REACHED START TIME')


def WaitToEnd(subject):
    TimeNow = datetime.datetime.now()
    e_time = subject['end'].split('-')
    while int(e_time[0]) >= int(TimeNow.strftime('%H')) and int(e_time[1]) > int(TimeNow.strftime('%M')) :
        time.sleep(5)
        TimeNow = datetime.datetime.now()



    print('REACHED END TIME')


def main():
    B = GoogleBot.GB()
    B.set_day_schedule()
    B.gmail_Login()

    for sub in B.subject_order_list:
        subject = B.schedule[sub]
        print('Subject:',sub)
        WaitToStart(subject)
        B.gm_Toggle_and_JoinMeeting(subject['URL'],subject,sub)
        WaitToEnd(subject)
        B.gm_LeaveMeeting(subject,sub)


if __name__ == "__main__":
    main()
