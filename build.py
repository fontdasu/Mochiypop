from glyphsLib.cli import main
from fontTools.ttLib import TTFont, newTable
import glob, shutil, subprocess, os
import ufo2ft
import ufoLib2
from pathlib import Path

palt_set = "uni3042.palt", "uni3041.palt", "uni3044.palt", "uni3043.palt", "uni3046.palt", "uni3045.palt", "uni3048.palt", "uni3047.palt", "uni304A.palt", "uni3049.palt", "uni304B.palt", "uni3095.palt", "uni304C.palt", "uni304D.palt", "uni304E.palt", "uni304F.palt", "uni3050.palt", "uni3051.palt", "uni3052.palt", "uni3096.palt", "uni3053.palt", "uni3054.palt", "uni3055.palt", "uni3056.palt", "uni3057.palt", "uni3058.palt", "uni3059.palt", "uni305A.palt", "uni305B.palt", "uni305C.palt", "uni305D.palt", "uni305E.palt", "uni305F.palt", "uni3060.palt", "uni3061.palt", "uni3062.palt", "uni3064.palt", "uni3063.palt", "uni3065.palt", "uni3066.palt", "uni3067.palt", "uni3068.palt", "uni3069.palt", "uni306A.palt", "uni306B.palt", "uni306C.palt", "uni306D.palt", "uni306E.palt", "uni306F.palt", "uni3070.palt", "uni3071.palt", "uni3072.palt", "uni3073.palt", "uni3074.palt", "uni3075.palt", "uni3076.palt", "uni3077.palt", "uni3078.palt", "uni3079.palt", "uni307A.palt", "uni307B.palt", "uni307C.palt", "uni307D.palt", "uni307E.palt", "uni307F.palt", "uni3080.palt", "uni3081.palt", "uni3082.palt", "uni3084.palt", "uni3083.palt", "uni3086.palt", "uni3085.palt", "uni3088.palt", "uni3087.palt", "uni3089.palt", "uni308A.palt", "uni308B.palt", "uni308C.palt", "uni308D.palt", "uni308F.palt", "uni308E.palt", "uni3090.palt", "uni3091.palt", "uni3092.palt", "uni3093.palt", "uni3094.palt", "uni30A2.palt", "uni30A1.palt", "uni30A4.palt", "uni30A3.palt", "uni30A6.palt", "uni30A5.palt", "uni30A8.palt", "uni30A7.palt", "uni30AA.palt", "uni30A9.palt", "uni30AB.palt", "uni30F5.palt", "uni30AC.palt", "uni30AD.palt", "uni30AE.palt", "uni30AF.palt", "uni31F0.palt", "uni30B0.palt", "uni30B1.palt", "uni30F6.palt", "uni30B2.palt", "uni30B3.palt", "uni30B4.palt", "uni30B5.palt", "uni30B6.palt", "uni30B7.palt", "uni31F1.palt", "uni30B8.palt", "uni30B9.palt", "uni31F2.palt", "uni30BA.palt", "uni30BB.palt", "uni30BC.palt", "uni30BD.palt", "uni30BE.palt", "uni30BF.palt", "uni30C0.palt", "uni30C1.palt", "uni30C2.palt", "uni30C4.palt", "uni30C3.palt", "uni30C5.palt", "uni30C6.palt", "uni30C7.palt", "uni30C8.palt", "uni31F3.palt", "uni30C9.palt", "uni30CA.palt", "uni30CB.palt", "uni30CC.palt", "uni31F4.palt", "uni30CD.palt", "uni30CE.palt", "uni30CF.palt", "uni31F5.palt", "uni30D0.palt", "uni30D1.palt", "uni30D2.palt", "uni31F6.palt", "uni30D3.palt", "uni30D4.palt", "uni30D5.palt", "uni31F7.palt", "uni30D6.palt", "uni30D7.palt", "uni30D8.palt", "uni31F8.palt", "uni30D9.palt", "uni30DA.palt", "uni30DB.palt", "uni31F9.palt", "uni30DC.palt", "uni30DD.palt", "uni30DE.palt", "uni30DF.palt", "uni30E0.palt", "uni31FA.palt", "uni30E1.palt", "uni30E2.palt", "uni30E4.palt", "uni30E3.palt", "uni30E6.palt", "uni30E5.palt", "uni30E8.palt", "uni30E7.palt", "uni30E9.palt", "uni31FB.palt", "uni30EA.palt", "uni31FC.palt", "uni30EB.palt", "uni31FD.palt", "uni30EC.palt", "uni31FE.palt", "uni30ED.palt", "uni31FF.palt", "uni30EF.palt", "uni30EE.palt", "uni30F7.palt", "uni30F0.palt", "uni30F8.palt", "uni30F1.palt", "uni30F9.palt", "uni30F2.palt", "uni30FA.palt", "uni30F3.palt", "uni30F4.palt", "a_voicedcombhira.palt", "i_voicedcombhira.palt", "e_voicedcombhira.palt", "o_voicedcombhira.palt", "ka_semivoicedcombhira.palt", "ki_semivoicedcombhira.palt", "ku_semivoicedcombhira.palt", "ke_semivoicedcombhira.palt", "ko_semivoicedcombhira.palt", "n_voicedcombhira.palt", "a_voicedcombkata.palt", "i_voicedcombkata.palt", "e_voicedcombkata.palt", "o_voicedcombkata.palt", "ka_semivoicedcombkata.palt", "ki_semivoicedcombkata.palt", "ku_semivoicedcombkata.palt", "ke_semivoicedcombkata.palt", "ko_semivoicedcombkata.palt", "se_semivoicedcombkata.palt", "tu_semivoicedcombkata.palt", "to_semivoicedcombkata.palt", "husmall_semivoicedcombkata.palt", "n_voicedcombkata.palt", "uni3035.palt", "uni3033.palt", "uni3034.palt", "uni2049.palt", "exclamdbl.palt", "uni2047.palt", "uni2048.palt", "uni2049.locl.palt", "exclamdbl.locl.palt", "uni2047.locl.palt", "uni2048.locl.palt", "uni3008.palt", "uni3009.palt", "uni3010.palt", "uni3011.palt", "uni300C.palt", "uni300D.palt", "uni300A.palt", "uni300B.palt", "uni3014.palt", "uni3015.palt", "uni300E.palt", "uni300F.palt", "uni30FB.palt", "uni30FC.palt", "uniE000.palt", "uniE001.palt", "uniE002.palt", "uniE003.palt", "uniE004.palt", "uniE005.palt", "uniE006.palt", "uniE007.palt", "uniE064.palt", "uniE065.palt", "uniE082.palt", "uniE083.palt", "uniE084.palt", "uniE085.palt", "uniE086.palt", "uniE087.palt", "uniE088.palt", "uniE089.palt", "uniE08A.palt", "uniE08B.palt", "uniE08C.palt", "uniE08D.palt", "uniE08E.palt", "uniE08F.palt", "uniE090.palt", "uniE091.palt", "uniE092.palt", "uniE093.palt", "uniE094.palt", "uniE095.palt", "uniE096.palt", "uniE097.palt", "uniE098.palt", "uniE099.palt", "uniE09A.palt", "uniE09B.palt", "uniE09C.palt", "uniE09D.palt", "uniE09E.palt", "uniE09F.palt", "uniE0A0.palt", "uniE0A1.palt", "uniE0A2.palt", "uniE0A3.palt", "uniE0A4.palt", "uniE0A5.palt", "uniE0A6.palt", "uniE0A7.palt", "uniE0A8.palt", "uniE0A9.palt", "uniE0AA.palt", "uniE0AB.palt", "uniE0AC.palt", "uniE0AD.palt", "uniE0AE.palt", "uniE0AF.palt", "uniE0B0.palt", "uniE0B1.palt", "uniE0B2.palt", "uniE0B3.palt", "uniE0B4.palt", "uniE0B5.palt", "uniE0B6.palt", "uniE0B7.palt", "uniE0B8.palt", "uniE0B9.palt", "uniE0BA.palt", "uniE0BB.palt", "uniE0BC.palt", "uniE0BD.palt", "uniE0BE.palt", "uniE0BF.palt", "uniE0C0.palt", "uniE0C1.palt", "uniE0C2.palt", "uniE0C3.palt", "uniE0C4.palt", "uniE0C5.palt", "uniE0C6.palt", "uniE0C7.palt", "uniE0C8.palt", "uniE0C9.palt", "uniE0CA.palt", "uniE0CB.palt", "uniE0CC.palt", "uniE0CD.palt", "uniE0CE.palt", "uniE0CF.palt", "uniE0D0.palt", "uniE0D1.palt", "uniE0D2.palt", "uniE0D3.palt", "uniE0D4.palt", "uniE0D5.palt", "uniE0D6.palt", "uniE0D7.palt", "uniE0D8.palt", "uniE0D9.palt", "uniE0DA.palt", "uniE0DB.palt", "uniE0DC.palt", "uniE0DD.palt", "uniE0E2.palt", "uniE0E3.palt"


p_ttf = TTFont("/Users/aaronbell/Documents/LocalProjects/Google_CJK/Mochiypop/fonts/ttf/MochiyPopPOne-Regular.ttf")

for glyph in palt_set:
    p_ttf["hmtx"].metrics[glyph[:-5]] = p_ttf["hmtx"].metrics[glyph]

p_ttf.save("/Users/aaronbell/Documents/LocalProjects/Google_CJK/Mochiypop/fonts/ttf/MochiyPopPOne-tweaked.ttf")



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
    "name": "decomposeComponents",
    "pre": 1,
}]

static_ttf = ufo2ft.compileTTF(exportFont, removeOverlaps=True)
DSIG_modification(static_ttf)
static_ttf["name"].addMultilingualName({'ja':'モッチーポップ One'}, static_ttf, nameID = 1, windows=True, mac=False)
static_ttf["name"].addMultilingualName({'ja':'Regular'}, static_ttf, nameID = 2, windows=True, mac=False)
print ("[Mochiy Pop One] Saving")
static_ttf.save("fonts/ttf/MochiyPopOne-Regular.ttf")

exportFont.info.familyName = "Mochiy Pop P One"

print ("[Mochiy Pop P One] Compiling")
p_ttf = ufo2ft.compileTTF(exportFont, removeOverlaps=True)
DSIG_modification(p_ttf)

p_ttf["name"].addMultilingualName({'ja':'モッチーポップ P One'}, p_ttf, nameID = 1, windows=True, mac=False)
p_ttf["name"].addMultilingualName({'ja':'Regular'}, p_ttf, nameID = 2, windows=True, mac=False)

print ("[Mochiy Pop P One] Changing full width kana metrics to proportional")

for glyph in palt_set:
    p_ttf["hmtx"].metrics[glyph[:-5]] = p_ttf["hmtx"].metrics[glyph]

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