from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, subject, data):
        pass

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        """
        将观察者添加到被观察者中
        """
        pass
    @abstractmethod
    def detach(self, observer):
        """
        将观察者从被观察者中移除
        """
        pass
    @abstractmethod
    def notify(self, data):
        """
        通知被观察者
        """
        pass

class LoginService(Subject):
    def __init__(self):
        self.observers = []

    def login(self, user, ip, time, district):
        self.user = user
        self.ip = ip
        self.time = time
        self.district = district
        self.notify({'user': self.user, 'ip': self.ip, 'time': self.time, 'district': self.district})

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(self, data)
   

class SMSSender(Observer):
    def __init__(self) -> None:
        super().__init__()
        self.user_ip_history = {}

    def update(self, subject, data):
        if subject.user not in self.user_ip_history:
            self.user_ip_history[subject.user] = []

        self.user_ip_history[subject.user].append({"ip": subject.ip, "time": subject.time, "district": subject.district})
        
        if len(self.user_ip_history[subject.user]) > 1:
            # 两次登录的时间间隔小于5s,但是ip发生了改变, 则认为是恶意登录
            if self.user_ip_history[subject.user][-1]['time'] - self.user_ip_history[subject.user][-1]['time'] < 5 and self.user_ip_history[subject.user][-1]['ip'] != self.user_ip_history[subject.user][-2]['ip']:
                print('--------------------------SMS发送短信---------------------------')
                print("检测到恶意登录, 用户: {}, IP: {}, 时间: {}, 地区: {}".format(subject.user, subject.ip, subject.time, subject.district))
                print('--------------------------SMS发送短信---------------------------')
                print()

class MailSender(Observer):
    def __init__(self) -> None:
        super().__init__()
        self.user_ip_history = {}

    def update(self, subject, data):
        if subject.user not in self.user_ip_history:
            self.user_ip_history[subject.user] = []

        self.user_ip_history[subject.user].append({"ip": subject.ip, "time": subject.time, "district": subject.district})
        
        if len(self.user_ip_history[subject.user]) > 1:
            # 两次登录的时间间隔小于5s,但是ip发生了改变, 则认为是恶意登录
            if self.user_ip_history[subject.user][-1]['time'] - self.user_ip_history[subject.user][-1]['time'] < 5 and self.user_ip_history[subject.user][-1]['ip'] != self.user_ip_history[subject.user][-2]['ip']:
                print('--------------------------Mail邮件提醒---------------------------')
                print("检测到恶意登录, 用户: {}, IP: {}, 时间: {}, 地区: {}".format(subject.user, subject.ip, subject.time, subject.district))
                print('--------------------------Mail邮件提醒---------------------------')
                print()

login_service = LoginService()
sms = SMSSender()
mail = MailSender()
login_service.attach(sms)
login_service.attach(mail)
login_service.login('user1', '192.168.0.1', 1, '上海')
login_service.login('user1', '192.168.0.2', 5, '美国')
