import eel
# import apiForPokemonInfo
eel.init("winUi")

@eel.expose
def App():
    print("App is runing")

App()

eel.start("index.html",size= (200,500))