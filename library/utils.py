class Stoppable:
    def __init__(self):
        self.needStop = False

    def stop(self):
        self.doBeforeStop()
        self.needStop = True

    def isStopped(self):
        return self.needStop

    def doBeforeStop(self):
        pass

class Pausable:
    def __init__(self):
        self.needPause = False

    def pause(self):
        self.doBeforeStop()
        self.needPause = True
    
    def resume(self):
        self.needPause = False

    def isPaused(self):
        return self.needPause

    def doBeforeStop(self):
        pass

class Clearable:
    def clearFlags(self, default_value=False):
        if hasattr(self, 'needStop'):
            self.needStop = default_value

        if hasattr(self, 'needPause'):
            self.needPause = default_value