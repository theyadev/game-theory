from lib.createPlaystyles import createPlaystyles
from lib.getComplexPlaystyles import getComplexPlaystyles

playstyles = createPlaystyles("./playstylesDefault.json")

playstyles.update(createPlaystyles("./playstylesCustom.json"))
playstyles.update(getComplexPlaystyles())

