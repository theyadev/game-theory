from Styles.Copy import Copy
from Styles.User import UserInput

from utils.createPlaystyles import createPlaystyles

playstyles = {}

defaults = createPlaystyles("./playstylesDefault.json")
customs = createPlaystyles("./playstylesCustom.json")

playstyles.update(defaults)
playstyles.update(customs)

if len(playstyles) > 0:
    for name, classe in playstyles.items():
        locals()[name] = classe
