# 我们在阅读文章时,如果觉得文章写的很好,我们就会评论、
# 收藏两连发。如果处于登录情况下,我们就可以直接做
# 评论,收藏这些行为。否则,跳转到登录界面,登录后再继续
# 执行先前的动作。这里涉及的状态有两种:登录与未登录,
# 行为有两种:评论,收藏。


from abc import ABC, abstractmethod

class Context(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.current_state = None
        self.__states = []
        self.__state_info = 0

    def add_state(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def get_state(self):
        return self.current_state

    def change_state(self, state):
        if self.current_state is None:
            print('init state is {}'.format(state.name))
        else:
            print('change state from {} to {}'.format(self.current_state.name, state.name))
        self.current_state = state

    def _set_state_info(self, state_info):
        self.__state_info = state_info
        for state in self.__states:
            if state.is_match(self.__state_info):
                self.change_state(state)


class State(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    @abstractmethod
    def is_match(self, state_info):
        pass



class UserState(State):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info == 0

    @abstractmethod
    def comment(self, text):
        pass

    @abstractmethod
    def collection(self, id):
        pass



class LoginState(UserState):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info == True

    def comment(self, text):
        print('评论: {}'.format(text))
    
    def collection(self, id):
        print('收藏: {}'.format(id))

class UnLoginState(UserState):
    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info == False

    def comment(self, text):
        print('请先登录...')
    
    def collection(self, id):
        print('请先登录...')


class User(Context):
    def __init__(self):
        super().__init__()
        self.add_state(LoginState('登录状态'))
        self.add_state(UnLoginState('未登录状态'))


    def get_state_info(self):
        return self.current_state

    def set_state_info(self, state_info):
        self._set_state_info(state_info)

    def comment(self, text):
        self.get_state().comment(text)

    def collection(self, id):
        self.get_state().collection(id)

    
if __name__ == '__main__':
    user = User()
    user.set_state_info(False)
    user.comment('这篇文章很不错')
    user.collection(1)
    user.set_state_info(True)
    user.comment('这篇文章很不错')
    user.collection(1)