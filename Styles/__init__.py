from Styles.Copy import Copy
from Styles.User import UserInput

from lib.createPlaystyles import createPlaystyles

__playstyles__ = createPlaystyles("./playstylesDefault.json")
__playstyles__.update(createPlaystyles("./playstylesCustom.json"))

if len(__playstyles__) > 0:
    for name, classe in __playstyles__.items():
        locals()[name] = classe
