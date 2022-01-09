from lib.getBasicPlaystyles import getBasicPlaystyles
from lib.getComplexPlaystyles import getComplexPlaystyles

playstyles = {}

playstyles.update(getBasicPlaystyles("./playstylesDefault.json"))
playstyles.update(getBasicPlaystyles("./playstylesCustom.json"))

playstyles.update(getComplexPlaystyles("./Styles"))

