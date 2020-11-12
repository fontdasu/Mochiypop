from glyphsLib.cli import main
from fontTools.ttLib import TTFont, newTable
import glob, shutil, subprocess, os
import ufo2ft
import ufoLib2
from pathlib import Path

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
static_ttf = ufo2ft.compileTTF(exportFont)
DSIG_modification(static_ttf)
print ("[Mochiy Pop One] Saving")
static_ttf.save("fonts/ttf/MochiyPopOne-Regular.ttf")

print ("[Mochiy Pop P One] Changing full width metrics to proportional")
for glyph in exportFont.glyphOrder:
    if ".palt" in glyph:
        palt_LSB = exportFont[glyph].getLeftMargin(exportFont.layers["public.default"])
        palt_RSB = exportFont[glyph].getRightMargin(exportFont.layers["public.default"])
        exportFont[glyph[:-5]].setLeftMargin(palt_LSB, exportFont.layers["public.default"])
        exportFont[glyph[:-5]].setLeftMargin(palt_RSB, exportFont.layers["public.default"])

exportFont.info.familyName = "Mochiy Pop P One"

print ("[Mochiy Pop P One] Compiling")
p_ttf = ufo2ft.compileTTF(exportFont)
DSIG_modification(p_ttf)
print ("[Mochiy Pop P One] Saving")
p_ttf.save("fonts/ttf/MochiyPopPOne-Regular.ttf")

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