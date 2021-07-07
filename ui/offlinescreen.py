from kivy.uix.screenmanager import Screen
from ui.modals import GameModal
import threading

class OfflineScreen(Screen):
    active_pop = None #active popup on the screen

    def __init__(self,CApp,**kwargs):
        super(OfflineScreen, self).__init__(**kwargs)
        self.app = CApp

    def training(self, *args):
        caster = threading.Thread(target=self.app.game.training,args=[self],daemon=True)
        caster.start()

    def replays(self, *args):
        caster = threading.Thread(target=self.app.game.replays,args=[self],daemon=True)
        caster.start()

    def local(self, *args):
        caster = threading.Thread(target=self.app.game.local,args=[self],daemon=True)
        caster.start()

    def tournament(self, *args):
        caster = threading.Thread(target=self.app.game.tournament,args=[self],daemon=True)
        caster.start()

    def standalone(self, *args):
        caster = threading.Thread(target=self.app.game.standalone,args=[self],daemon=True)
        caster.start()
    
    def error_message(self,e):
        popup = GameModal()
        for i in e:
            popup.modal_txt.text += i + '\n'
        popup.close_btn.bind(on_release=popup.dismiss)
        popup.close_btn.text = "Close"
        if self.active_pop:
            self.active_pop.dismiss()
        popup.open()
