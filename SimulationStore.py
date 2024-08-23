class SimulationStore():
    def __init__(self, depth: int, actor: str):
        self.depth = depth
        self.actor = actor

    def get_depth(self):
        return self.depth
    
    def get_actor(self):
        return self.actor