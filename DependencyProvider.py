from abc import ABC, abstractmethod
import SimulationStore

class DependencyProvider(ABC):

    @abstractmethod
    def provider():
        pass


class WriterDepthProviderImpl(DependencyProvider, SimulationStore):    
    def provider(self):
        pass

class WriterActorProviderImpl(DependencyProvider, SimulationStore):    
    def provider(self):
        pass
