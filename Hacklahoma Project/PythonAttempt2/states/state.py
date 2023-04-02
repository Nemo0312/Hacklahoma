class State:
    """A class to create a game state"""

    def __init__(self, game):
        self.game = game
        self.prev_state = None

    def update(self, delta_time, actions):
        pass

    def render(self, surface):
        pass

    def enter_state(self):
        if len(self.game.states_stack) > 0:
            self.prev_state = self.game.states_stack[-1]
        self.game.states_stack.append(self)

    def exit(self):
        self.game.states_stack.pop()
