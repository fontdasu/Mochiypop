from glyphsLib.cli import main
from fontTools.ttLib import TTFont, newTable
import glob, shutil, subprocess, os
import ufo2ft
import ufoLib2
from pathlib import Path

# PREP

f = open("sources/palt.txt", "r")
palt_set = []
for line in f.readlines():
    sub = str(line).rstrip().replace(";","")[4:]
    palt_set.append(sub)


def DSIG_modification(font:TTFont):
    font["DSIG"] = newTable("DSIG")     #need that stub dsig
    font["DSIG"].ulVersion = 1
    font["DSIG"].usFlag = 0
    font["DSIG"].usNumSigs = 0
    font["DSIG"].signatureRecords = []
    font["head"].flags |= 1 << 3        #sets flag to always round PPEM to integer


print ("Converting to UFO")
main(("glyphs2ufo", "sources/MochiyPop.glyphs"))

print ("[Mochiy Pop One] Compiling")
exportFont = ufoLib2.Font.open("sources/MochiyPopOne-Regular.ufo")

exportFont.lib['com.github.googlei18n.ufo2ft.filters'] = [{
    "name": "flattenComponents",
    "pre": 1,
}]

# BUILDING STANDARD VERSION

static_ttf = ufo2ft.compileTTF(exportFont, removeOverlaps=True)
DSIG_modification(static_ttf)
static_ttf["name"].addMultilingualName({'ja':'モッチーポップ One'}, static_ttf, nameID = 1, windows=True, mac=False)
static_ttf["name"].addMultilingualName({'ja':'Regular'}, static_ttf, nameID = 2, windows=True, mac=False)
print ("[Mochiy Pop One] Saving")
static_ttf.save("fonts/ttf/MochiyPopOne-Regular.ttf")

# BUILDING PROPORTIONAL VERSION

exportFont.info.familyName = "Mochiy Pop P One"

print ("[Mochiy Pop P One] Compiling")
p_ttf = ufo2ft.compileTTF(exportFont, removeOverlaps=True)
DSIG_modification(p_ttf)

p_ttf["name"].addMultilingualName({'ja':'モッチーポップ P One'}, p_ttf, nameID = 1, windows=True, mac=False)
p_ttf["name"].addMultilingualName({'ja':'Regular'}, p_ttf, nameID = 2, windows=True, mac=False)

print ("[Mochiy Pop P One] Changing metrics to proportional")

for sub in palt_set:
    split = sub.split(" by ")
    p = split[1]
    fw = split[0]
    
    p_ttf["vmtx"].metrics[fw] = p_ttf["vmtx"].metrics[p]
    p_ttf["hmtx"].metrics[fw] = p_ttf["hmtx"].metrics[p]

print ("[Mochiy Pop P One] Saving")
p_ttf.save("fonts/ttf/MochiyPopPOne-Regular.ttf")

# CLEANUP AND HINTING

shutil.rmtree("sources/MochiyPopOne-Regular.ufo")
os.remove("sources/MochiyPop.designspace")

ttf = Path("fonts/ttf")

for file in ttf.glob("*.ttf"):
    print ("["+str(file).split("/")[2][:-4]+"] Autohinting")
    subprocess.check_call(
            [
                "ttfautohint",
                "--stem-width",
                "nsn",
                str(file),
                str(file)[:-4]+"-hinted.ttf",
            ]
        )
    shutil.move(str(file)[:-4]+"-hinted.ttf", str(file))