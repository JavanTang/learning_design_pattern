# 我们在阅读文章时,如果觉得文章写的很好,我们就会评论、收藏两连发。如果处于登录情况下,
# 我们就可以直接做评论,收藏这些行为。否则,跳转到登录界面,登录后再继续执行先前的动作。
# 这里涉及的状态有两种:登录与未登录,行为有两种:评论,收藏。

from abc import ABC, abstractmethod

class Content(ABC):

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

    def is_match(self, state_info):
        return False

    @abstractmethod
    def do_action(self, state_info):
        pass


class SolidState(State):

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info <= 0

    def do_action(self, state_info):
        print('solid state, state_info is {}'.format(state_info))

    
class GaseousState(State):
    
        def __init__(self, name):
            super().__init__(name)
    
        def is_match(self, state_info):
            return state_info > 100
    
        def do_action(self, state_info):
            print('gaseous state, state_info is {}'.format(state_info))

class LiquidState(State):
    
        def __init__(self, name):
            super().__init__(name)
    
        def is_match(self, state_info):
            return state_info > 0 and state_info <= 100
    
        def do_action(self, state_info):
            print('liquid state, state_info is {}'.format(state_info))

class Water(Content):
    
        def __init__(self):
            super().__init__()
            self.add_state(SolidState('solid'))
            self.add_state(GaseousState('gaseous'))
            self.add_state(LiquidState('liquid'))
            self.__state_info = 0

        def set_temperature(self, state_info):
            self._set_state_info(state_info)
    
        def get_temperature(self):
            return self.__state_info

water = Water()
water.set_temperature(0)
water.set_temperature(50)
water.set_temperature(100)
