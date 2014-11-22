

Class NPC:
    def __init__(self,locx,locy,height,message):
        self.locx = locx
        self.locy = locy
        self.height = height
        self.message = message
        return
    def get_message(self):
        return self.message
    def get_locx(self):
        return self.locx
    def get_locy(self):
        return self.locy

