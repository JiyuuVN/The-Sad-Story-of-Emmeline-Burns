# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# backgrounds
image bg barrow = "bg/graveyard.jpg"
image bg barrow2 = "bg/graveyard2.jpg"
image bg lake = "bg/lake.jpg"
image bg room2 = "bg/room2.jpg"
image bg room1 = "bg/room.jpg"
image bg white = "white.png"

# cg
image bg toma op = "cg/toma op.png"
image bg toma op2 = "cg/toma op2.png"
image bg tomaemmy = "cg/tomaemmy.png"
image bg lake_cg = "cg/lake.png"
image bg emmyintro = "cg/emmyintro.png"
image bg emmyintro2 = "cg/emmyintro2.png"
image bg lillycg = "cg/lillycg.png"
image cg1 = "cg/cg1.jpg"
image cg2_2 = "cg/cg2_2.jpg"
image cg3 = "cg/cg3.jpg"
image cg4 = "cg/cg4.jpg"
image cg4_2 = "cg/cg4_2.jpg"
image cg5 = "cg/cg5.jpg"
image cg5_2 = "cg/cg5_2.png"
image cg6 = "cg/cg6.jpg"

init:
    image cg1_sepia = im.Grayscale("cg/cg1.jpg")
    image cg2_sepia = im.Grayscale("cg/cg2_2.jpg")

# misc
image night = "night.png"
image splash1 = "gui/splash1.png"
image splash2 = "gui/splash2.png"
image splashfree = "gui/splashfree.png"
image cred1 = "credits/cred1.png"
image cred2 = "credits/cred2.png"
image cred3 = "credits/cred3.png"
image cred4 = "credits/cred4.png"
image cred5 = "credits/cred5.png"
image credit1 = "credits/credits1.png"
image credit_2 = "credits/credits2.png"
image credit__3 = "credits/credits3.png"
image credit___4 = "credits/credits4.png"
image credit____5 = "credits/credits5.png"
image bg desk = "credits/desk.jpg"
image credut = "credits/credits.png"
image thanku = "credits/thanks.png"

# toma
image toma normal n = im.FactorScale("toma/tomaneutral.png", 0.26)
image toma normal a = im.FactorScale("toma/toma normal a.png", 0.26)
image toma blush a = im.FactorScale("toma/toma blush a.png", 0.26)
image toma closed n = im.FactorScale("toma/toma closed n.png", 0.26)
image toma closed a = im.FactorScale("toma/toma closed a.png", 0.26)
image toma ehe a = im.FactorScale("toma/toma ehe a.png", 0.26)
image toma ehe n = im.FactorScale("toma/toma ehe n.png", 0.26)
image toma smile a = im.FactorScale("toma/toma smile a.png", 0.26)
image toma smile n = im.FactorScale("toma/toma smile n.png", 0.26)
image toma shock a = im.FactorScale("toma/toma shock a.png", 0.26)
image toma shock n = im.FactorScale("toma/toma shock n.png", 0.26)
image toma shockblush a = im.FactorScale("toma/toma shockblush a.png", 0.26)
image toma gneh n = im.FactorScale("toma/toma gneh n.png", 0.26)
image toma gneh2 n = im.FactorScale("toma/toma gneh2 n.png", 0.26)
image toma gneh3 n = im.FactorScale("toma/toma gneh3 n.png", 0.26)
image toma pout n = im.FactorScale("toma/toma pout n.png", 0.26)
image toma poutblush n = im.FactorScale("toma/toma poutblush n.png", 0.26)
image toma sad a = im.FactorScale("toma/toma sad a.png", 0.26)
image toma sad n = im.FactorScale("toma/toma sad n.png", 0.26)
image toma sad2 a = im.FactorScale("toma/toma sad2 a.png", 0.26)
image toma sad2 n = im.FactorScale("toma/toma sad2 n.png", 0.26)
image toma sad3 a = im.FactorScale("toma/toma sad3 a.png", 0.26)
image toma scared n = im.FactorScale("toma/toma scared n.png", 0.26)
image toma scared2 n = im.FactorScale("toma/toma scared2 n.png", 0.26)
image toma sigh n = im.FactorScale("toma/toma sigh n.png", 0.26)
image toma frown a = im.FactorScale("toma/toma frown a.png", 0.26)
image toma frown n = im.FactorScale("toma/toma frown n.png", 0.26)
image toma skeptical a = im.FactorScale("toma/toma skeptical a.png", 0.26)
image toma sadblush n = im.FactorScale("toma/toma sadblush n.png", 0.26)
image toma sadblush a = im.FactorScale("toma/toma sadblush a.png", 0.26)
image toma angryblush n = im.FactorScale("toma/toma angryblush n.png", 0.26)
image toma poutblush a = im.FactorScale("toma/toma poutblush a.png", 0.26)
image toma shockblush n = im.FactorScale("toma/toma shockblush n.png", 0.26)
image toma smileblush a = im.FactorScale("toma/toma smileblush a.png", 0.26)

# emmy
image emmy normal n = im.FactorScale("emily/emmy neutral n.png", 0.38)
image emmy normal a = im.FactorScale("emily/emmy normal a.png", 0.38)
image emmy heh n = im.FactorScale("emily/emmy heh n.png", 0.38)
image emmy angry n = im.FactorScale("emily/emmy angry n.png", 0.38)
image emmy angry2 n = im.FactorScale("emily/emmy angry2 n.png", 0.38)
image emmy angry3 n = im.FactorScale("emily/emmy angry3 n.png", 0.38)
image emmy angry4 n = im.FactorScale("emily/emmy angry4 n.png", 0.38)
image emmy angryblush n = im.FactorScale("emily/emmy angryblush n.png", 0.38)
image emmy huh a = im.FactorScale("emily/emmy huh a.png", 0.38)
image emmy huh n = im.FactorScale("emily/emmy huh n.png", 0.38)
image emmy frown n = im.FactorScale("emily/emmy frown n.png", 0.38)
image emmy_bruises = im.FactorScale("emily/emmy bruises.png", 0.38)
image emmy pout a = im.FactorScale("emily/emmy pout a.png", 0.38)
image emmy pout n = im.FactorScale("emily/emmy pout n.png", 0.38)
image emmy pout2 a = im.FactorScale("emily/emmy pout2 a.png", 0.38)
image emmy poutblush n = im.FactorScale("emily/emmy poutblush n.png", 0.38)
image emmy sad a = im.FactorScale("emily/emmy sad a.png", 0.38)
image emmy sad n = im.FactorScale("emily/emmy sad n.png", 0.38)
image emmy sad2 a = im.FactorScale("emily/emmy sad2 a.png", 0.38)
image emmy sad2 n = im.FactorScale("emily/emmy sad2 n.png", 0.38)
image emmy sad3 n = im.FactorScale("emily/emmy sad3 n.png", 0.38)
image emmy shock a = im.FactorScale("emily/emmy shock a.png", 0.38)
image emmy shock n = im.FactorScale("emily/emmy shock n.png", 0.38)
image emmy shockblush a = im.FactorScale("emily/emmy shockblush a.png", 0.38)
image emmy shocksad a = im.FactorScale("emily/emmy shocksad a.png", 0.38)
image emmy smile a = im.FactorScale("emily/emmy smile a.png", 0.38)
image emmy smile n = im.FactorScale("emily/emmy smile n.png", 0.38)
image emmy tease n = im.FactorScale("emily/emmy tease n.png", 0.38)
image emmy teaseblush n = im.FactorScale("emily/emmy teaseblush n.png", 0.38)
image emmy wink a = im.FactorScale("emily/emmy wink a.png", 0.38)
image emmy wink n = im.FactorScale("emily/emmy wink n.png", 0.38)
image emmy wink2 a = im.FactorScale("emily/emmy wink2 a.png", 0.38)
image emmy wink2 n = im.FactorScale("emily/emmy wink2 n.png", 0.38)
image emmy frown n = im.FactorScale("emily/emmy frown n.png", 0.38)
image emmy frown a = im.FactorScale("emily/emmy frown a.png", 0.38)
image emmy smirk a = im.FactorScale("emily/emmy smirk a.png", 0.38)
image emmy ehe n = im.FactorScale("emily/emmy ehe n.png", 0.38)
image emmy shocksad n = im.FactorScale("emily/emmy shocksad n.png", 0.38)
image emmy shocksad2 n = im.FactorScale("emily/emmy shocksad2 n.png", 0.38)
image emmy ehe a = im.FactorScale("emily/emmy ehe a.png", 0.38)
image emmy smile2 a = im.FactorScale("emily/emmy smile2 a.png", 0.38)
image emmy smile2 n = im.FactorScale("emily/emmy smile2 n.png", 0.38)

image emmy sad a 2 = im.FactorScale("emily/emmy sad a.png", 0.68)
image emmy sad n 2 = im.FactorScale("emily/emmy sad n.png", 0.68)
image emmy sad2 a 2 = im.FactorScale("emily/emmy sad2 a.png", 0.68)
image emmy sad2 n 2 = im.FactorScale("emily/emmy sad2 n.png", 0.68)
image emmy sad3 n 2 = im.FactorScale("emily/emmy sad3 n.png", 0.68)
image emmy shocksad n 2 = im.FactorScale("emily/emmy shocksad n.png", 0.68)
image emmy shocksad2 n 2 = im.FactorScale("emily/emmy shocksad2 n.png", 0.68)
image emmy shock n 2 = im.FactorScale("emily/emmy shock n.png", 0.68)

image emmy normal n 2 = im.FactorScale("emily/emmy neutral n.png", 0.55)
image emmy_bruises 2 = im.FactorScale("emily/emmy bruises.png", 0.55)

image emmy2 normal n = im.FactorScale("emily/emmy2 normal n.png", 0.38)
image emmy2 smile n = im.FactorScale("emily/emmy2 smile n.png", 0.38)
image emmy2 shock n = im.FactorScale("emily/emmy2 shock n.png", 0.38)
image emmy2 smirk n = im.FactorScale("emily/emmy2 smirk n.png", 0.38)
image emmy2 huh n = im.FactorScale("emily/emmy2 huh n.png", 0.38)
image emmy2 smirk2 n = im.FactorScale("emily/emmy2 smirk2 n.png", 0.38)
image emmy2 wink n = im.FactorScale("emily/emmy2 wink n.png", 0.38)
image emmy2 normal a = im.FactorScale("emily/emmy2 normal a.png", 0.38)
image emmy2 smile a = im.FactorScale("emily/emmy2 smile a.png", 0.38)
image emmy2 shock a = im.FactorScale("emily/emmy2 shock a.png", 0.38)
image emmy2 smirk a = im.FactorScale("emily/emmy2 smirk a.png", 0.38)
image emmy2 huh a = im.FactorScale("emily/emmy2 huh a.png", 0.38)
image emmy2 smirk2 a = im.FactorScale("emily/emmy2 smirk2 a.png", 0.38)
image emmy2 wink a = im.FactorScale("emily/emmy2 wink a.png", 0.38)
image emmy2 pout n = im.FactorScale("emily/emmy2 pout n.png", 0.38)
image emmy2 angry n = im.FactorScale("emily/emmy2 angry n.png", 0.38)
image emmy2 angry2 n = im.FactorScale("emily/emmy2 angry2 n.png", 0.38)
image emmy2 angry3 n = im.FactorScale("emily/emmy2 angry3 n.png", 0.38)
image emmy2 ehe n = im.FactorScale("emily/emmy2 ehe n.png", 0.38)
image emmy2 frown n = im.FactorScale("emily/emmy2 frown n.png", 0.38)
image emmy2 sad n = im.FactorScale("emily/emmy2 sad n.png", 0.38)
image emmy2 sad2 n = im.FactorScale("emily/emmy2 sad2 n.png", 0.38)
image emmy2 frown a = im.FactorScale("emily/emmy2 frown a.png", 0.38)

image emmy3 angry n = im.FactorScale("emily/emmy3 angry n.png", 0.38)
image emmy3 angry2 n = im.FactorScale("emily/emmy3 angry2 n.png", 0.38)
image emmy3 angry3 n = im.FactorScale("emily/emmy3 angry3 n.png", 0.38)
image emmy3 frown n = im.FactorScale("emily/emmy3 frown n.png", 0.38)
image emmy3 sad n = im.FactorScale("emily/emmy3 sad n.png", 0.38)
image emmy3 pout n = im.FactorScale("emily/emmy3 pout n.png", 0.38)
image emmy3 sigh n = im.FactorScale("emily/emmy3 sigh n.png", 0.38)
image emmy3 sadshock n = im.FactorScale("emily/emmy3 sadshock n.png", 0.38)
image emmy3 ehe n = im.FactorScale("emily/emmy3 ehe n.png", 0.38)
image emmy3 smile n = im.FactorScale("emily/emmy3 smile n.png", 0.38)
image emmy3 smile a = im.FactorScale("emily/emmy3 smile a.png", 0.38)
image emmy3 smirk a = im.FactorScale("emily/emmy3 smile a.png", 0.38)
image emmy3 smirk2 a = im.FactorScale("emily/emmy3 smile a.png", 0.38)
image emmy3 huh a = im.FactorScale("emily/emmy3 huh a.png", 0.38)
image emmy3 shock n = im.FactorScale("emily/emmy3 shock n.png", 0.38)
image emmy3 smile2 n = im.FactorScale("emily/emmy3 smile2 n.png", 0.38)
image emmy3 smile2 a = im.FactorScale("emily/emmy3 smile2 a.png", 0.38)
image emmy3 wink a = im.FactorScale("emily/emmy3 wink a.png", 0.38)

# cornelia

image cornelia normal n = im.FactorScale("cornelia/cornelia normal n.png", 0.385)
image cornelia normal a = im.FactorScale("cornelia/cornelia normal a.png", 0.385)
image cornelia smile n = im.FactorScale("cornelia/cornelia smile n.png", 0.385)
image cornelia smileblush n = im.FactorScale("cornelia/cornelia smileblush n.png", 0.385)
image cornelia pout n = im.FactorScale("cornelia/cornelia pout n.png", 0.385)
image cornelia pout a = im.FactorScale("cornelia/cornelia pout a.png", 0.385)
image cornelia poutblush n = im.FactorScale("cornelia/cornelia poutblush n.png", 0.385)
image cornelia poutblush a = im.FactorScale("cornelia/cornelia poutblush a.png", 0.385)
image cornelia angry n = im.FactorScale("cornelia/cornelia angry n.png", 0.385)
image cornelia angry2 n = im.FactorScale("cornelia/cornelia angry2 n.png", 0.385)
image cornelia angryblush n = im.FactorScale("cornelia/cornelia angryblush n.png", 0.385)
image cornelia cry n = im.FactorScale("cornelia/cornelia cry n.png", 0.385)
image cornelia cry a = im.FactorScale("cornelia/cornelia cry a.png", 0.385)
image cornelia cry2 a = im.FactorScale("cornelia/cornelia cry2 a.png", 0.385)
image cornelia ehe n = im.FactorScale("cornelia/cornelia ehe n.png", 0.385)
image cornelia sad a = im.FactorScale("cornelia/cornelia sad a.png", 0.385)
image cornelia sad n = im.FactorScale("cornelia/cornelia sad n.png", 0.385)
image cornelia sad2 n = im.FactorScale("cornelia/cornelia sad2 n.png", 0.385)
image cornelia sadblush a = im.FactorScale("cornelia/cornelia sadblush a.png", 0.385)
image cornelia shock n = im.FactorScale("cornelia/cornelia shock n.png", 0.385)
image cornelia shock a = im.FactorScale("cornelia/cornelia shock a.png", 0.385)
image cornelia shockblush a = im.FactorScale("cornelia/cornelia shockblush a.png", 0.385)
image cornelia shockblush n = im.FactorScale("cornelia/cornelia shockblush n.png", 0.385)
image cornelia frown n = im.FactorScale("cornelia/cornelia frown n.png", 0.385)
image cornelia frown a = im.FactorScale("cornelia/cornelia frown a.png", 0.385)
image cornelia sadblush n = im.FactorScale("cornelia/cornelia sadblush n.png", 0.385)
image cornelia sadblush2 n = im.FactorScale("cornelia/cornelia sadblush2 n.png", 0.385)
image cornelia angry a = im.FactorScale("cornelia/cornelia angry a.png", 0.385)
image cornelia angry2 a = im.FactorScale("cornelia/cornelia angry2 a.png", 0.385)
image cornelia smirk a = im.FactorScale("cornelia/cornelia smirk a.png", 0.385)

image fog_bg:
    contains:
        "fog3.png"
        xanchor -1.0
        linear 27.0 xanchor 1.0
        repeat
    contains:
        "fog2.png"
        xanchor -1.0
        linear 130.0 xanchor 1.0
        repeat
    contains:
        "fog2.png"
        xanchor 0.0
        linear 110.0 xanchor 1.0
        repeat

image fog_fg:
    contains:
        "fog.png"
        xanchor 0.0
        linear 20.5 xanchor 1.0
        repeat
    contains:
        "fog3.png"
        xanchor -1.0
        linear 80.0 xanchor 1.0
        repeat
    contains:
        "fog3.png"
        xanchor -1.0
        linear 40.0 xanchor 1.0
        repeat
        
image fog_fg2:
    contains:
        "fog.png"
        xanchor 0.0
        linear 20.5 xanchor 1.0
        repeat
    contains:
        "fog4.png"
        xanchor -1.0
        linear 40.0 xanchor 1.0
        repeat
    contains:
        "fog3.png"
        xanchor 0.0
        linear 20.0 xanchor 1.0
        repeat
        
image fog_fg3:
    contains:
        "fog.png"
        xanchor 0.0
        linear 28.5 xanchor 1.0
        repeat
    contains:
        "fog4.png"
        xanchor -1.0
        linear 48.0 xanchor 1.0
        repeat
    contains:
        "fog3.png"
        xanchor 0.0
        linear 17.0 xanchor 1.0
        repeat
    
    
image grain:
    "grain/grain1.png" with Dissolve(0.25, alpha=True)
    0.2
    "grain/grain2.png" with Dissolve(0.25, alpha=True)
    0.2
    "grain/grain3.png" with Dissolve(0.25, alpha=True)
    0.2
    "grain/grain4.png" with Dissolve(0.25, alpha=True)
    0.2
    "grain/grain3.png" with Dissolve(0.25, alpha=True)
    0.2
    "grain/grain2.png" with Dissolve(0.25, alpha=True)
    0.2
    repeat
    
image grain2:
    "grain/grain2 1.png" with Dissolve(0.25, alpha=True)
    0.15
    "grain/grain2 2.png" with Dissolve(0.25, alpha=True)
    0.15
    "grain/grain2 4.png" with Dissolve(0.25, alpha=True)
    0.15
    "grain/grain2 2.png" with Dissolve(0.25, alpha=True)
    0.15
    "grain/grain2 3.png" with Dissolve(0.25, alpha=True)
    0.15
    "grain/grain2 4.png" with Dissolve(0.25, alpha=True)
    0.15
    repeat
    
# characters
define t = Character("Toma", what_prefix="“", what_suffix="”", color="#C266C2", font = "dancing.ttf", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed", what_outlines=[ (1, "#000000") ], who_outlines=[ (1, "#000000") ])
define e = Character("Emily", what_prefix="“", what_suffix="”", color="#C266C2", font = "dancing.ttf", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed", what_outlines=[ (1, "#000000") ], who_outlines=[ (1, "#000000") ])
define ew = Character("???", what_prefix="“", what_suffix="”", color="#C266C2", font = "dancing.ttf", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed", what_outlines=[ (1, "#000000") ], who_outlines=[ (1, "#000000") ])
define c = Character("Cornelia", what_prefix="“", what_suffix="”", color="#C266C2", font = "dancing.ttf", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed", what_outlines=[ (1, "#000000") ], who_outlines=[ (1, "#000000") ])
define em = Character("Emmeline", what_prefix="“", what_suffix="”", color="#C266C2", font = "dancing.ttf", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed", what_outlines=[ (1, "#000000") ], who_outlines=[ (1, "#000000") ])
define nv = Character(None, kind=nvl, ctc="ctc_animation_nvl", ctc_pause="ctc_animation_nvl", ctc_position="fixed")
define p = Character("Phillip", what_prefix="“", what_suffix="”", color="#C266C2", font = "dancing.ttf", what_outlines=[ (1, "#000000") ], who_outlines=[ (1, "#000000") ])
define tw = Character("Toma?", what_prefix="“", what_suffix="”", color="#C266C2", font = "dancing.ttf", ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed", what_outlines=[ (1, "#000000") ], who_outlines=[ (1, "#000000") ])
define narrator = Character(None, ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed", xpos=0.09, ypos=0.06, what_outlines=[ (1, "#000000") ])
define w = Character(None, ctc="ctc_animation", ctc_pause="ctc_animation", ctc_position="fixed", xpos=0.09, ypos=0.06, what_color="#000000", what_outlines=[ (0, "#FFFFFF") ], what_drop_shadow = [(0, 0)], window_background="textbox2.png")

# transitions
define eyeopen = ImageDissolve("transitions/trans1.png", 1.1, ramplen=60)
define eyeclose = ImageDissolve("transitions/trans1.png", 1.1, ramplen=60, reverse=True)
define clockwipe = ImageDissolve("transitions/wipe.png", 1.5, ramplen=50)
define wipeup_slow = ImageDissolve("transitions/wipeup.png", 1.5, ramplen=60)
define wipeup_norm = ImageDissolve("transitions/wipeup.png", 0.9, ramplen=120)
define wipedown_slow = ImageDissolve("transitions/wipeup.png", 1.5, ramplen=60, reverse=True)
define wiperight_slow = ImageDissolve("transitions/wipeleft.png", 1.5, ramplen=140, reverse=True)
define wipeleft_slow = ImageDissolve("transitions/wipeleft.png", 1.5, ramplen=140, reverse=False)
define wipeleft_fast = ImageDissolve("transitions/wipeleft.png", 0.8, ramplen=140, reverse=False)
define slow_dissolve = Dissolve(2.0)
define wipe = ImageDissolve("transitions/wipetrans.png", 1.5, ramplen=140, reverse=True)
define dooropen = ImageDissolve("transitions/dooropen.png", 1.1, ramplen=60, reverse=True)
define doorclose = ImageDissolve("transitions/dooropen.png", 1.1, ramplen=60, reverse=False)
define tear = ImageDissolve("transitions/tear.png", 2.0, ramplen=70, reverse=False)
define tear2 = ImageDissolve("transitions/tear.png", 2.0, ramplen=70, reverse=True)
define wavetrans1 = ImageDissolve("transitions/wavetrans.png", 1.0, ramplen=40, reverse=True)
define wavetrans2 = ImageDissolve("transitions/wavetrans.png", 1.0, ramplen=40, reverse=False)
define wavetrans1_f = ImageDissolve("transitions/wavetrans.png", 0.32, ramplen=20, reverse=True)
define wavetrans2_f = ImageDissolve("transitions/wavetrans.png", 0.32, ramplen=20, reverse=False)
define wavetrans1_fast = ImageDissolve("transitions/wavetrans.png", 0.6, ramplen=20, reverse=True)
define wavetrans3 = ImageDissolve("transitions/wavetrans2.png", 1.0, ramplen=40, reverse=True)
define wavetrans4 = ImageDissolve("transitions/wavetrans2.png", 1.0, ramplen=40, reverse=False)
define wavetrans3_f = ImageDissolve("transitions/wavetrans2.png", 0.5, ramplen=40, reverse=True)
define wavetrans4_f = ImageDissolve("transitions/wavetrans2.png", 0.5, ramplen=40, reverse=False)
define spoopy = ImageDissolve("transitions/spoopy.png", 1.4, ramplen=150)
define circleirisout = ImageDissolve("transitions/id_circleiris.png", 1.0, ramplen=100)
define circleirisin = ImageDissolve("transitions/id_circleiris.png", 1.0, ramplen=100, reverse=True)
define heart = ImageDissolve("transitions/hearttrans.png", 1.1, ramplen=5)
define hearttrans1 = ImageDissolve("transitions/hearttrans.png", 1.1, ramplen=5)
define hearttrans2 = ImageDissolve("transitions/hearttrans.png", 1.1, reverse=True, ramplen=5)
define wipedown_fast = ImageDissolve("transitions/wipeup.png", 0.5, ramplen=60, reverse=True)

init:
    transform bounce:
        linear 0.2 xoffset 0 yoffset 14
        linear 0.2 xoffset 0 yoffset 0
        
init:
    transform twirl:
        linear 0.35 xoffset 25 yoffset 0
        linear 0.25 xoffset 0 yoffset 0
        linear 0.35 xoffset -25 yoffset 0
        linear 0.25 xoffset 0 yoffset 0
        
    transform right_left:
        linear 0.0 xoffset -150 yoffset 0
        linear 8.0 xoffset 120 yoffset 0
        
    transform right_left2:
        linear 0.0 xoffset -100 yoffset 0
        linear 25.0 xoffset 200 yoffset 0
        
    transform right_left3:
        linear 0.0 xoffset -60 yoffset 80
        linear 25.0 xoffset 240 yoffset 80
        
    transform right_left4:
        linear 0.0 xoffset -60 yoffset 50
        linear 25.0 xoffset 240 yoffset 50
        
    transform right_left5:
        linear 0.0 xoffset -600 yoffset -900
        linear 25.0 xoffset 400 yoffset -900
        
    transform right_left6:
        linear 0.0 xoffset 0 yoffset 50
        linear 25.0 xoffset 300 yoffset 50
        
    transform right_left7:
        linear 0.0 xoffset 60 yoffset 100
        linear 25.0 xoffset 360 yoffset 100
        
    transform cree:
        linear 0.0 xoffset 0.0 yoffset -50
        linear 7.0 xoffset 0.0 yoffset 10
        
    transform cree2:
        linear 0.0 xoffset 0.0 yoffset -30
        linear 17.0 xoffset 0.0 yoffset 60
        
    transform logodesu:
        linear 0.0 xoffset 0.0 yoffset -40
        linear 3.0 xoffset 0.0 yoffset 0
        



init:
    $ close = Position(xpos=0.5, xanchor=0.5, ypos=0.88, yanchor=0.5)
    $ close_left = Position(xpos=0.05, xanchor="left", ypos=0.8, yanchor=0.5)
    $ close_right = Position(xpos=0.4, xanchor="left", ypos=0.8, yanchor=0.5)
    
    $ left2_t = Position(xpos=0.3, xanchor="center", ypos=0.61, yanchor=0.5)
    $ cent_t = Position(ypos=0.61, yanchor=0.5, xpos=0.5, xanchor=0.5,)
    
    $ right2_e = Position(xpos=0.5, xanchor="left", ypos=0.63, yanchor=0.5)
    $ cent_e = Position(ypos=0.61, yanchor=0.5, xpos=0.5, xanchor=0.5,)
    $ left2_e = Position(xpos=0.3, xanchor="center", ypos=0.63, yanchor=0.5)
    $ close_e = Position(ypos=0.58, yanchor=0.5)
    
    $ left2_c = Position(xpos=0.3, xanchor="center", ypos=0.62, yanchor=0.5)
    $ right2_c = Position(xpos=0.5, xanchor="left", ypos=0.62, yanchor=0.5)
    
init python:

    style.nvl_window.background = "nvl.png"
    style.nvl_window.left_padding = 185
    style.nvl_window.right_padding = 185
    style.nvl_window.ypadding = 150
    
image ctc_animation = Animation("ctc/ctc13.png", 0.15, "ctc/ctc12.png", 0.05, "ctc/ctc11.png", 0.05, "ctc/ctc10.png", 0.05, "ctc/ctc9.png", 0.05, "ctc/ctc8.png", 0.05, "ctc/ctc7.png", 0.05,"ctc/ctc6.png", 0.05, "ctc/ctc5.png", 0.05, "ctc/ctc4.png", 0.05, "ctc/ctc3.png", 0.05, "ctc/ctc2.png", 0.05, "ctc/ctc.png", 0.15, "ctc/ctc2.png", 0.05, "ctc/ctc3.png", 0.05, "ctc/ctc4.png", 0.05, "ctc/ctc5.png", 0.05, "ctc/ctc6.png", 0.05, "ctc/ctc7.png", 0.05, "ctc/ctc8.png", 0.05, "ctc/ctc9.png", 0.05, "ctc/ctc10.png", 0.05, "ctc/ctc11.png", 0.05, "ctc/ctc12.png", 0.05, xpos=0.94, ypos=0.895, xanchor=1.0, yanchor=1.0)

image ctc_animation_nvl = Animation("ctc/ctc13.png", 0.15, "ctc/ctc12.png", 0.05, "ctc/ctc11.png", 0.05, "ctc/ctc10.png", 0.05, "ctc/ctc9.png", 0.05, "ctc/ctc8.png", 0.05, "ctc/ctc7.png", 0.05,"ctc/ctc6.png", 0.05, "ctc/ctc5.png", 0.05, "ctc/ctc4.png", 0.05, "ctc/ctc3.png", 0.05, "ctc/ctc2.png", 0.05,"ctc/ctc.png", 0.15, "ctc/ctc2.png", 0.05, "ctc/ctc3.png", 0.05, "ctc/ctc4.png", 0.05, "ctc/ctc5.png", 0.05, "ctc/ctc6.png", 0.05, "ctc/ctc7.png", 0.05, "ctc/ctc8.png", 0.05, "ctc/ctc9.png", 0.05, "ctc/ctc10.png", 0.05, "ctc/ctc11.png", 0.05, "ctc/ctc12.png", 0.05, xpos=0.94, ypos=0.785, xanchor=1.0, yanchor=1.0)

label splashscreen:
    play sound "sfx/fire.mp3"
    scene black
    $ renpy.pause(0.5)
    show splash1 with tear
    $ renpy.pause(1.2)
    stop sound fadeout 0.5
    show splash2 at logodesu
    with slow_dissolve
    $ renpy.pause(2.0)
    return


# The game starts here.
label start:
    
    stop music fadeout 1.5
    
    image op1 = Text("{size=35}My name is Toma Andrews, and I am a victim of identity theft.{/size}", text_align=0.5, color="#FFFFFF")
    image text1 = Text("{size=35}{i}I{/i} would be so much better.{/size}", text_align=0.5, color="#FFFFFF")
    image grave = Text("{size=30}{i}Here lies the body of Phillip Burns, 1807-1851.{w}{vspace=30}Also Perdita Burns, wife of the above, 1811-1851.{w}{vspace=30}Also Emmeline Burns, their beloved daughter, 1836-1851.{w}{vspace=30}May their souls rest in peace.{/i}{/size}", text_align=0.5, color="#FFFFFF")
    image text2 = Text("{size=35}Now I, Toma Andrews, a recovering victim of identity theft, hope that I can become something beautiful, too.{/size}", text_align=0.5, color="#FFFFFF")
    image text3 = Text("{size=35}The next day...{/size}", text_align=0.5, color="#FFFFFF")
  

    scene black
    with dissolve
    
    $ renpy.pause(0.5)
    
    scene bg toma op with wipe
    $ renpy.pause(0.5)
    show op1:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with tear
    with Pause(2.0)
    scene black with wipe
    nvl show wipe
    
    play music "music/sad.mp3" fadein 1.0
    
    nv "Проверка. НЯНЯНЯ!!! NYAAAA~!! It’s all Aunt Kathryn’s fault, of course. Most things are, according to Mum."
    nv "Stealing Mum’s favourite dress when they were both schoolgirls was bad enough, but stealing the name of her first (and only) daughter? Now, that’s a low not many of us can sink to within our lifetimes."
    nv "My name was supposed to be Amelia. Mum has always loved the name Amelia, ever since she was a young girl. Mum was all set to call me Amelia if I was a girl, Thomas if I was a boy (after her dad), until Aunt Kathryn ruined everything."
    
    nvl clear
    
    nv "As luck would have it, Aunt Kathryn fell pregnant with her first child before my mum fell pregnant with me. Their due dates were also very similar, only a few weeks apart."
    nv "Though Mum and Aunt Kathryn have never been particularly close (I think there was too much childhood bullying, which was a touch too mean-spirited to be forgiven in adulthood with a laugh and a ‘what were we like?!’), they spent more time together during their twin pregnancies than they had done over the last decade ."
    nv "They attended the same hospital for their check-ups and went to the same support group for pregnant women at the civic centre, and their rocky relationship improved over complaints about bladder infections, morning sickness, and uncontrollable cravings for anchovies (Mum) or smoked cheese (Aunt Kathryn)."
    nv "And then Aunt Kathryn stole my name."
    
    nvl clear
    
    nv "Though Aunt Kathryn is one year younger than my mum, she always seemed to get things first. She was the first to have her period, to piece her ears, and to have a serious boyfriend."
    nv "She was the first to have a baby, too."
    nv "A baby girl."
    nv "A girl called Amelia."
    
    nvl clear
    
    nv "Mum didn’t know what to do, having her dream name stolen from her so suddenly. She had half a mind to confront Aunt Kathryn about it, but in the end decided against it. She had only just begun to repair her relationship with her sister, and she didn’t want this to drive a wedge between them once more."
    nv "But she was still annoyed."
    nv "She still is."
    
    nvl clear
    
    nv "Mum could have strengthened her resolve and named me Amelia regardless, but the name didn’t feel special anymore. Not when Aunt Kathryn had used it."
    nv "In the end, after much deliberation, Mum decided that she would just go with her second option. Thomas."
    nv "Naturally, given I was a girl, Thomas was out of the question. Was there a female variant of Thomas, then? Thomasina? Thomasandria? Thomasetta?"
    nv "Maybe not."
    nv "There was Toma, however. Toma Andrews."
    nv "And that’s how I got my name."
    nv "That might explain why I don’t like it very much."
    
    nvl clear
    
    nv "My name isn’t really mine. Like clothes that are two sizes too big, it doesn’t fit me properly. It never has done. That’s because it was never intended for me."
    nv "If had been called Amelia instead, would my life be any different? Would it change who I am?"
    nv "I don’t know, because I’ve never been an Amelia. I’m just Toma. The weird girl with the weird name."
    nv "And my name isn’t the only weird thing about me."
    
    nvl clear
    
    nv "Ever since I can remember, my mum has been obsessed with family history. She says it’s like playing detective — peeking back into the past with only fragments of information in an attempt to piece together the truth."
    nv "I think Mum fancies herself as a Miss Marple figure. She always did like Agatha Christie, and though she prefers Poirot, I don’t think she’s European enough to pull Poirot off. Neither does she has a moustache."
    nv "Mum took me to the local library with her when I was small, so she could keep a watchful eye over my little blonde head while she delved deep into the annals of our family’s long lost history. There, she would spend hours and hours searching through the filing cabinets and online databases, digging through reams of old newspapers that dated all the way back to the 1700s, on the hunt for articles about the Spencers or the Kendalls or the Lintons or the Becketts or the Bradfords."
    
    nvl clear
    
    nv "Fortunately for us, our family used to be rather wealthy back in the day. In fact, I think Grandpa Thomas (Mum’s dad) was rather well-off himself. Perhaps not as well-off as the Bowers or the Becketts, though, and certainly not as well-off as the Lintons."
    nv "Mum says it’s a lot easier to research your family tree if you come from a wealthy lineage. There are more records kept on the comings and goings of rich people, as opposed to street beggars or paupers. That’s probably because of the money."
    nv "As soon as money is involved, people will pay attention to you. It was like that back in the 1700s, and it’s exactly the same now."
    
    nvl clear
    
    nv "I remember that the floors were hard, covered in a dark green carpet that was uncomfortable and scratchy, and the walls were a dull grey like the concrete blocks in a multi-storey carpark."
    nv "Even though Mum got me a library card so I could check out any book I wanted, I inevitably got bored within the first half hour or so. There are only so many times you can re-read volumes of {i}Goosebumps{/i}."
    nv "Despite these inconveniences, however, I still found the stories Mum would tell me about my long-dead relatives interesting. They were stories that sounded impossible to a small girl like me — things I could imagine occurring within novels, but not in real life."
    nv "Stories about my Great Great Grandfather, Zachary Kendall, who used to be a priest, but was fired from his post after he physically assaulted a member of his congregation while drunk on Christmas Day. Stories about my great Great Great Aunt, Maribel Spencer, who ran away from home at the age of fifteen to marry her middle-aged piano teacher, Roger Beckett."
    
    nvl clear
    
    nv "I don’t know why, but these stories my mum told me, of unknown people from unfamiliar times, always resonated with me. Maybe it was because they weren’t fictional characters from the pages of books, or celebrities smiling shiny smiles on magazine covers."
    nv "These people were all part of me."
    nv "I wouldn’t be alive right now without Zachary Kendall, even if he did beat up a member of his congregation, and I wouldn’t be alive without Maribel Spencer, even if she did have a thing for older men who could play a semi-decent Für Elise."
    nv "In a way, I owe them. I owe them a lot."
    nv "I suppose what they say is true. Blood really is thicker than water."
    
    nvl clear
    
    nv "And, speaking of blood, the local library wasn’t the only place my mum’s investigations led her, oh no. That was just the tip of the iceberg."
    nv "She used to take me to cemeteries a lot, too."
    nv "Not just the cemetery in here, Barrowby All Saints, but cemeteries all across Lincolnshire — sometimes even further afield, to Yorkshire or Leicestershire."
    
    nvl clear
    
    nv "The thing about family history is, if you get obsessed with it like Mum, birth certificates and death certificates stop being enough. You want to see real evidence of your ancestor’s past lives — concrete proof that Zachary Kendall and Maribel Spencer really did exist on this earth, and really did make a difference."
    nv "And, for a less romantic explanation, you also want to double-check the facts, to ensure Zachary Kendall’s remains really are buried in St. Mary’s churchyard in Beverly, like his death certificate states."
    nv "Hence, the graveyards."
    nv "Lots and lots of graveyards."
    
    nvl clear
    
    nv "Every weekend, without fail, my mum would take me on a trip to a graveyard, searching for ancestors. Sometimes we’d turn it a game. We’d challenge one another, to see who could find Rose Bradford’s final resting place the quickest. The winner got to choose what we’d listen to in the car on the way home."
    nv "Being my mum’s daughter, I hated her taste in music (I still do), and I was desperate to beat her."
    nv "I got quite good at finding graves, if I do say so myself. Even though I was around seven or eight, and my legs weren’t as long as my mum’s, I was able to beat her nine times out of ten."
    nv "I used to think she was going easy on me. Now, I’m not so sure."
    nv "I just have a talent. I’m good at finding dead people — even if they have been dead for two centuries, and all that’s left behind are bones."
    
    nvl clear
    
    nv "Now, let me just get one thing straight. I’m not crazy. I don’t think dead people call out to me or anything. I’ve never seen a ghost before, excluding the ones in horror movies. I suppose you could just call it a coincidence."
    nv "Still, it’s quite a strange coincidence."
    nv "Whenever I went into a graveyard with my mum, I just knew where to look, almost instinctively. My feet just happened to lead me to a tombstone, and via some strange skill I might have inherited from Rose Bradford, the self-proclaimed psychic, I was usually right."
    nv "That might be why I’m so obsessed with cemeteries, even now."
    nv "Just like some people prefer hot weather, others cold, I like graveyards. They remind me of my childhood: of fun times spent with my mum, searching for my relatives."
    
    nvl clear
    
    nv "When I went out looking for graves with my mum, I was almost always right."
    nv "Ever since I started attending St. Hugh’s college, however, I’ve only ever felt wrong."
    nv "Though I get good grades in most of my classes, I’m hopelessly lost when it comes to anything beyond that. I have hardly any friends, other than Hattie."
    nv "I’m nothing like Amelia Miller, who just so happens to be in the same form group as me. She’s always surrounded by people. They all love her."
    
    nvl clear
    
    nv "Would they love me instead if I had been called Amelia, like I should have been?"
    nv "I don’t know."
    nv "What I do know is, though it’s unfair and ridiculous and I don’t dislike Amelia, I can’t help but be jealous of her. She’s from a wealthy family, she has nice skin and pretty blue eyes, and she’s incredibly popular."
    nv "I, on the other hand, am awkward and shy, and I can’t hold a conversation with anybody other than Hattie."
    nv "That might be another reason why I like graveyards. There are a lot of people in them, but they can’t bother me like they do in school. They’re dead, and that’s perfectly fine by me."
    nv "As the saying goes, dead men tell no tales. They only leave tales behind, which we can examine as we see fit."
    
    nvl clear
    
    nv "That’s why I came to Barrowby All Saints this Friday, instead of catching the bus to go to school, like I was supposed to. Like my mum believed I did."
    nv "I just wanted some time off. A few moments where I can stop being Toma, a half-formed name bastardised from my grandfather’s, and be the girl I always wanted to be."
    nv "If only I had been born as an Amelia."
    nv "Then, my life would be so much better."
    
    nvl clear
    
    nvl hide dissolve
    
    scene bg white with wipe
    scene bg toma op
    show text1:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with tear
    stop music fadeout 1.0
    $ renpy.pause(1.5)
    scene bg white with tear2
    $ renpy.pause(0.3)
    scene bg barrow2
    show fog_bg
    show fog_fg
    with wipe
    
    window show dissolve
    
    play music "music/lazy afternoon.mp3" fadein 1.0
    
    "The day is slightly overcast for early autumn, and a thick layer of fog creeps along the ground, chilling my ankles and making me shiver. The grass is still wet with morning dew, but the soil beneath it is firm and hard."
    "I suppose that’s to be expected. You wouldn’t want to build a graveyard on marshland, where people run the risk of falling through the earth and into the graves."
    "I might have an affinity for the dead (more than I do with the living), but not even I fancy popping in for an impromptu visit with Gerald Fisher, 1843-1912, and Aline, wife of the above."
    
    play ambience "sfx/wind.ogg" fadein 0.8
    
    "It’s cold, too. The wind snakes down my spine, and I shiver. It isn’t a rough wind, though. Instead, it’s soft, brushing past my cheeks and through my hair in an almost apologetic manner."
    "The leaves on the trees are dark green, some slowly beginning to turn red and yellow, but the sun in the sky is obscured by clouds, so everything looks dull and grey."
    
    play sound "sfx/footsteps.mp3" fadein 1.0
    
    "With every step I take, my feet crunch over the stray leaves, but that’s the only sound I can hear."
    "Just me, the wind, and the leaves."
    
    stop ambience fadeout 1.2
    show toma smile a at cent_t behind fog_fg with dissolve
    
    "I walk through these well-trodden paths, pausing to examine each tombstone that catches my interest."
    "There’s something strangely inviting about these old slabs of the stone, almost as though they’re greeting me — and why wouldn’t they? I come here often enough. They should know me by now."
    "Any mother who isn’t mine would probably find their only daughter’s obsession with graveyards unsettling. Fortunately, my mum is just as weird as I am, so she doesn’t question it. She must know my love of graveyards is all her fault."
    
    show toma smile n
    
    "As I walk, I nod my head in recognition as I pass each tombstone: Alistair Doncaster, Irene Douglas, Charlotte Draper, Doreen Hughes, Abel Johnson, Genevieve Parsons, Aubrey Wedgewood..."
    
    stop sound fadeout 1.5
    
    "I wonder about these people, reduced to nothing more than names and bones. What lives did they lead? Were they happy, sad, or merely bemused by the string of coincidences which led them into this world?"
    "For Alistair Doncaster, that happened in 1879. For Irene Douglas, it was 1894."
    
    show toma closed n
    
    "What was the world like back then, when these people were alive, and their footsteps — not mine — crunched the leaves underfoot, or fell firmly against the compacted earth?"
    "I don’t know. It’s hard for me to imagine it."
    
    show toma normal a
    
    "As I meander deeper and deeper through the lines of graves, like Alice sinking into Wonderland, I start to wonder. What would it be like if I was already dead?"
    
    stop music fadeout 1.5
    window hide dissolve
    scene black with eyeclose
    
    play ambience "sfx/wind.ogg" fadein 0.5
    
    "When I close my eyes, the cold wind blowing across my cheeks, I swear I can almost smell it — the earth in my nostrils, the scent of decay."
    
    play sound "sfx/footstep.mp3"
    
    "Ah..."
    
    stop ambience fadeout 0.5
    scene bg barrow2
    show fog_bg
    show toma shock n at cent_t
    show fog_fg
    with eyeopen
    
    "I turn my head, blinking. What was that sound? It was almost like a footstep — but that can’t be. I’m the only person here, after all."
    "At least, I thought I was."
    "Evidently, I’m not anymore."
    
    window hide dissolve
    
    play music "music/little flower.ogg" fadein 1.0
    
    scene bg emmyintro:
        size (1280, 720) crop (0, 580, 1280, 720)
        linear 20.0 crop (0, 0, 1280, 720)
    with wipe
    
    w "A young girl stands there, her arms held by her sides, her eyes wide and blue. Her hair is loose, light brown, and flutters in the breeze, her fringe cut just above her eyebrows. She wears a white dress, long and modest, which falls to her ankles."
    w "Her dress is comprised of a number of layers, and looks like something that belongs to another era, another time — an England when Queen Victoria was on the throne, and the horse and carriage was still the main way people got about, and it was socially acceptable to wear bonnets in public."    
    w "I stare at her."
    w "She looks like nobody I’ve ever seen before, save characters in period dramas. There’s something so unrealistic about her appearance that I can hardly bring myself to believe she’s really real."
    w "Maybe that’s why I do something I rarely ever do."
    w "My curiosity unsticks my throat, and I find myself asking her a question."
    
    stop music fadeout 0.5
    
    scene bg barrow2
    show fog_bg
    show toma normal a at left2_t
    show emmy normal n at right2_e
    show emmy_bruises at right2_e
    show fog_fg
    with wipe
    
    window show dissolve
 
    play music "music/lazy afternoon.mp3" fadein 1.0
    
    t "Are you going to a costume party?"
    show emmy frown n
    "The girl blinks. For a few moments she, too, seems surprised, but this look quickly passes."
    show emmy normal a
    ew "Oh, are you referring to this old thing?"
    show toma skeptical a
    t "That dress doesn’t look like some ‘old thing’. It’s expensive, right?"
    show emmy frown a
    ew "I believe it was rather costly when Father first purchased it. Now, however... I am not particularly well-versed in the economy, so I could not give you an answer."
    show toma normal n
    t "Father?"
    "What kind of girl calls their Dad ‘Father’?"
    show toma gneh2 n
    "Maybe I’m just biased, because my dad vanished before I was even born (Mum told me he couldn’t cope with the commitment — ‘Which was quite funny, really, because he had no qualms about commitment when he asked me to sleep with him’), but ‘Father’ sounds far too old fashioned."
    "And I haven’t even touched on everything else she said."
    show emmy smile n
    ew "Oh, um..."
    "The girl smiles. Her face remains pale, and does not flush, but I can imagine blood coursing beneath her cheeks all the same. She gives the impression of blushing, even though she does not."
    ew "I suppose most people would use ‘Dad’ nowadays. Forgive me. I am not familiar with such a phrase, and it sounds quite peculiar to my tongue."
    show toma normal n
    "And the plot thickens."
    "My questions only seem to invite more questions, and I find myself becoming drawn towards this strange girl despite myself."
    "I want to know who this girl is. I want to understand her."
    "It must be this feeling, this desperate thirst for hidden knowledge, which encouraged Mum to track down what now remains of Zachary Kendall, Maribel Spencer, Rose Bradford, and the rest."
    show toma normal a
    t "So, um... I’ve not seen you around Barrowby before. Do you live here?"
    show emmy normal n
    ew "I have lived here for a very long time."
    show toma frown n
    t "But you don’t look much older than I am."
    show emmy normal a
    ew "I will be fifteen years old this December. At least, I should be."
    show toma normal a
    "So she’s fourteen, too. Just like me."
    t "You say you’ve lived here for a long time, but I’ve never seen you before. You don’t go to St. Hughes, do you?"
    show emmy sad n
    "The girl shakes her head."
    show toma frown a
    t "So, which school do you go to? Ruskin? Sandon? Not Walton Girls?"
    "She shakes her head again."
    t "Then, are you home-schooled?"
    "That would explain what she’s doing in this graveyard at half past seven on a Friday morning, wearing such a strange outfit she may as well have fled from one of those ‘Ye Olde Fashioned Photographie Parloure’ places."
    show emmy frown a
    ew "I, um... I suppose I was home-schooled, yes. I have never been to school before. I used to have Ellie, but I have not seen her in some time."
    show toma frown n
    t "Ellie? A private tutor?"
    show emmy ehe n
    ew "Something like that, yes. She was rather strict. She got so angry when I eluded her attempts to teach me about Queen Elizabeth, and instead escaped to the Lintons’ estate."
    "She smiles a soft, gentle smile, much like an old woman with rheumy eyes recalling a fond memory, already half forgotten."
    "I don’t know if I’ve ever seen anybody my age make such a peculiar face before."
    "Just who is this girl...?"
    t "But you don’t have a tutor anymore?"
    show emmy sad n
    ew "There wouldn’t be much point."
    "Then is she one of those YouTube celebrities? Judging by her clothes, I can imagine her as one of those eccentric, self-proclaimed ‘living dolls’, who get millions of hits on their videos just for eating food and staring at the camera."
    show toma ehe a
    t "So, um... I’m sorry, this is the first question I should have asked, before I started with all the personal details. What’s your name?"
    show emmy smile n
    e "Emily."
    show toma normal a
    t "Emily..."
    "I think I can remember that. It’s a common name. There are two Emilys in my class: Emily Hargreaves and Emily Turner."
    show toma sad n
    "I don’t know if that name fits the girl in front of me, though. It sounds too simple for her. Something about the name she offered seems strangely unfinished, cut short, like a sentence that ends without a full stop."
    "I don’t investigate any further, however. I hardly know the girl. What right do I have to interrogate her?"
    show emmy smile n
    e "And, if it would not be too rude, may I inquire as to what I should call you?"
    show toma shockblush a
    t "Oh, um..."
    "Of course, I should have expected this question. When somebody asks for your name, it is only polite to ask for theirs in return. Otherwise, you run the risk of looking rude."
    "Is there any greater snub in this world than refusing to recognise somebody’s name? What are human beings without names? Failing to acknowledge a name is like failing to acknowledge somebody’s existence."
    show toma sad a
    "But this is a question I have never liked answering. Just what {i}is{/i} my name?"
    "It says Toma on my birth certificate, but I can’t quite bring myself to believe that. Not when I was fated, before I took my first breath, to be called Amelia instead."
    show emmy huh a
    e "Oh my, do not look so troubled! You will make me feel guilty!"
    show toma shock a
    t "I-I’m sorry!"
    show emmy smile n at bounce
    e "Ha. What a funny girl. You don’t need to apologise."
    "So, this girl is calling me funny, is she? Given she’s dressed like that, that comment kind of stings..."
    e "And you do not need to tell me your name if you do not wish to. We all have our own secrets."
    show toma shockblush a
    t "A-Are you sure you don’t mind?"
    show emmy smile a
    e "I am quite sure. After all, I could just make up a name for you instead!"
    show toma sad a
    t "Well..."
    show emmy smirk a
    e "I hope you are not adverse to this suggestion? I rather like giving people nicknames!"
    e "I would always call Miss Warren Ellie — her first name was Helena, you see — and she got mad at me because of {i}that{/i}, too."
    show emmy angry4 n
    e "‘This girl has no manners!’, she would always say. ‘She may have a pretty face, but she behaves like a guttersnipe!’"
    show emmy smile a
    e "Not that I gave a button what she thought. Father was paying her enough, so I thought it best to make her work for her wages. She may have found me irritating, but I certainly wasn’t boring!"
    t "... I suppose it’s fine. It doesn’t bother me."
    "Anything would be better than Toma."
    e "Well, let me see..."
    "Emily looks me up and down, one finger against her lower lip. She’s smiling, but it isn’t the same shy, self-contained smile from before."
    "This smile is rather more teasing. Her eyes flash mischievously, like a naughty schoolgirl’s in an Enid Blyton story."
    "She’ll be talking about condensed milk and tinned sardines next, I’m sure of it."
    show emmy smile n
    e "It is true we do not know one another very well, but that is just in the present. I feel like we could become quite close friends, if given the chance!"
    show emmy frown n
    e "You remind me so much of her, after all... Can it be a mere coincidence?"
    show toma frown a
    t "Her?"
    show emmy frown a
    e "Mm. I thought so from behind, too, but when you turned about it became clearer than ever. You have her nose, and her eyes. Maybe you even have her forehead, too — but it’s hard to tell, since it’s all covered in hair."
    show toma sad n
    "I look down at the floor, suddenly awkward, and dig the tip of my school shoe into the earth. I shift my right foot slightly, making a small indention in the ground — a minute grave for an ant."
    "I don’t know if I like being compared to somebody else. I do that enough myself with Amelia Miller."
    t "Um... Even if I do look like one of your friends, I don’t know if I would want their name. I-I was hoping for a name of my own..."
    show emmy shock n
    e "Yes, of course! You do not need to worry about that. I would never be so callous as to dress you in the title of another! I apologise if it seemed that way!"
    "She does sound sorry, too. Truly sorry."
    show emmy sad n
    e "Even if you look like her, you are not her. You couldn’t be. It isn’t possible."
    show emmy normal a
    e "Let me see. A name for you. A name that belongs only to you, and only to you..."
    show emmy smile n
    e "Ah, I think I have it!"
    show toma normal n
    t "You do?"
    e "Yes! From now on, you can be Verity."
    t "Verity?"
    show emmy huh a
    e "Do you like it?"
    show toma smile a
    t "It’s pretty. Much prettier than my real name."
    show emmy smile n
    "Emily smiles, her face flushing (though, once more, it doesn’t really flush — I just imagine that it does) with happiness."
    e "I’m so glad! I thought virtue names might be too anachronistic nowadays, but I truly am fond of them."
    show emmy frown a
    e "One of my aunts was called Charity, and my grandmother was Patience. Not that she was particularly patient, according to my father. She used to hit him for the smallest of misdemeanours."
    show toma normal a
    show emmy normal n
    e "... But that was a long time ago."
    show emmy huh a
    e "At any rate, I am curious. Why are you in a gloomy place like this at such an hour, when you should be at school?"
    show toma blush a
    t "Oh, um... I just like graveyards, I suppose. They’re relaxing."
    show emmy shock a
    show emmy frown a
    e "I don’t know if I have met many people in my life who share that opinion! Why do you think such a strange thing?"
    show toma normal n
    t "I’m not sure. I just like them. Graveyards are nice and quiet, and people don’t come here very often. When they do, they’re usually quiet, too. It’s the respectful thing to do."
    "Apart from the local boys who tramp about here, drunk, on Friday nights, and piss on the graves and scrawl rude words on them."
    show toma gneh n
    "I glance at a nearby grave, that of an Elijah (or Elisha?) Farrow. Somebody has scrawled across the top of it, in black marker pen, {b}GOD IS DEAD{/b}."
    show toma sigh n
    "It seems we have a Banksy of our own living in Barrowby. Who would have thought?"
    show toma normal a
    t "And I like thinking of stories, too."
    show emmy frown a
    e "Stories?"
    show toma smile a
    "I nod."
    t "Graves are small, so the people buried underneath them are turned into names and dates, nothing more. I think there must be more to these people than that, though."
    show toma closed a
    t "What were their parents like? Did they have any siblings? What was their job? Were they happy? What about all the people they met, whose lives they may have influenced?"
    t "I don’t know about all those things. I never will."
    show toma sad n
    t "It’s fascinating, but... At the same time, it’s a little sad, too."
    show toma sadblush n
    "I blush, my hands hanging limply at my sides. Did I say too much? I think I might have said too much."
    "This is why I don’t talk to people at school, other than Hattie. It’s because I’m weird, and I know my fellow classmates — Emily Hargreaves and Emily Turner included — would just laugh at me."
    "Well, maybe Amelia wouldn’t. Amelia’s too nice to laugh at anybody."
    show toma blush a
    t "T-That’s what I think, anyway. It probably sounds stupid, though."
    show emmy normal n
    e "No, I believe you made some good points."
    show toma shockblush a
    t "I-I did?"
    show emmy sad n
    e "Yes. Every person has a story, and there is not enough space on a single tombstone to tell it."
    show emmy sad2 n
    e "The sad truth is, there are so many people in this world it is not possible to remember every single story."
    e "As the years go by, they fall by the wayside. The dead must always concede to the whims of the living — even in places like this. "
    show emmy angry n
    "Emily looks back at Elijah (or Elisha) Farrow’s grave, decorated with the biting political commentary {b}GOD IS DEAD{/b}, and sighs."
    show emmy normal n
    e "I like thinking of stories, too. In fact, I could tell you a story of my own. I have been turning it over in my head for quite some time now, and I would be intrigued to hear your response."
    show toma normal n
    "So she’s interested in writing stories, is she? No wonder she seems so peculiar. Those who fancy themselves as writers always are."
    show toma ehe a
    t "I... I-I wouldn’t mind, I suppose..."
    show emmy frown n
    e "Are you quite sure? I don’t want to bore you, and I cannot remember the last time anybody wanted to hear what I had to say."
    show toma shockblush a
    t "N-No, I’m quite sure! I would love to hear it! Um... There was nothing else I wanted to do here, anyway."
    "Nothing other than wander, trying to avoid thinking about school next Monday, and how much trouble I’ll be in when it’s discovered I’ve been playing truant."
    show toma sad a
    "I always run away from problems. I have done ever since I was a child. I must have inherited that admirable trait from my dad, alongside his last name."
    show emmy normal n
    e "Well then. If you want to follow me."
    
    stop music fadeout 1.0
    
    play sound "sfx/footsteps.mp3" fadein 0.5
    hide emmy
    hide emmy_bruises
    with dissolve
    
    show toma at cent_t with move
    
    "Emily turns about, her hair fluttering, and slips by the graveyards like a shadow."
    
    window hide dissolve
    scene bg barrow
    show fog_bg
    show toma normal n at left2_t
    show fog_fg
    with wiperight_slow
    window show dissolve
    
    "I follow her, curious yet cautious, as she leads me behind the church, where the trees are thicker and there are yet more graves, hiding beneath the shadows."
    
    show emmy normal n at right2_e behind fog_fg
    show emmy_bruises at right2_e behind fog_fg
    with dissolve
    
    stop sound fadeout 1.5
    play music "music/sad.mp3" fadein 1.0
    
    "She draws my attention to a tombstone, just one tombstone of many. It juts out of the grass like a tooth from a gum, slightly crooked. A few cracks run down its dark grey sides, and the top of the grave is fringed with pale yellow lichen."
    show toma normal n
    show emmy sad2 n
    "The name engraved into the tombstone is a little difficult to see, impressed only shallowly, and written in a cursive hand that makes my eyes hurt."
    "I didn’t explore the graveyards of Lincolnshire in my youth for nothing, though, and I am more skilled than most teenage girls when it comes to reading inscriptions on gravestones."
    "It would be embarrassing if, after all my training, I was not able to decipher something like this."
    
    window hide dissolve
    
    scene black with wipe
    $ renpy.pause(0.5)
    show cg5
    show fog_fg2
    show cg5_2
    show fog_fg3
    with wipe
    $ renpy.pause()
    
    scene bg barrow
    show fog_bg
    show toma scared n at left2_t
    show emmy normal n at right2_e
    show emmy_bruises at right2_e
    show fog_fg
    with wipe
    
    window show dissolve
    
    "I shift, suddenly uncomfortable. Graveyards don’t usually make me uncomfortable — it’s the world of the living that I can’t stand — but there’s something about this tombstone that strikes a discordant note within me, as though played on a un-tuned piano."
    t "They all died on the same year..."
    show emmy frown n
    e "They did indeed. And all on the same day, too."
    show toma sad2 n
    "I turn away from the grave, the final remnant of the unfortunate Burns family, and bite my lower lip."
    "It feels like something icy has ensnared my heart — slimy fingers dredged up from the bottom of a scum-speckled lake."
    "When I next speak, my voice is barely whisper, even quieter than that of the wind that shifts the dead leaves about my feet."
    show toma sad a
    t "How do you know that?"
    show emmy normal n
    e "It’s just a story. I already told you that."
    t "I-I suppose so, but..."
    "But when Emily said it, it didn’t sound like a story. Instead, she sounded deadly serious. She looks serious, too. Her eyes are narrowed, her lips pursed, her face stark white, as though carved from stone."
    "The fog swirls about us like a veil. I swear it’s grown even thicker than it was ealier this morning. I can taste the fog at the back of my throat when I inhale, and I cough. It tastes cold, rank, and repulsive."
    "The taste of death."
    "Just who is Emily, anyway? She doesn’t look like any girl I know. She doesn’t act like any girl I know."
    "I’m almost tempted to believe... But that would be ridiculous, wouldn’t it? Wouldn’t it?"
    show emmy frown n
    e "So. Should I tell you my story? I must warn you, it’s rather dour. Then again, given our setting, what other kind of story could it be?"
    show emmy sad2 n
    e "You should already know how it ends, after all."
    
    stop music fadeout 1.0

    window hide dissolve
    
    play ambience "sfx/fire.mp3" fadein 0.5
    scene black
    show image "grain" onlayer texture
    with tear
    
    nvl show tear
    
    nvl clear
    
    nv "Emmeline Burns, born in 1836 to Phillip and Perdita Burns, led a charmed life. Her family was rather well-to-do, her grandfather being a lawyer, her father a banker, and she grew up in a large townhouse with five bedrooms on the outskirts of Barrowby."
    nv "Given her father’s profession, he was often away in London on business, but this did not upset Emmeline. She was old enough to understand that her father needed to work so they could afford her nice house, and her fine clothes, and the ribbons she wore in her hair, so she did not complain."
    nv "Though she did not see her father for months at a time, when he returned home it was always with a present for Emmeline, and a kiss on her cheek, and it was as though he had never been away at all."
    
    nvl clear
    
    nv "Phillip was a kind man, though he may not have been a paragon of manly virtues (‘He’s the runt of the litter. If he were a pig, we would have drowned him in the well,’ Grandmother Patience always griped)."
    nv "He was not naturally predisposed to the world of financing, he did have a good head on his shoulders, and was relatively intelligent. Not even Grandmother Patience could deny that."
    nv "It was through his quick wits, rather than his magnetic charisma (of which he was sorely lacking), that Phillip had been able to expand upon the Burns family’s fortune, as he had invested a good deal of their money into the stock market."
    
    nvl clear
    
    nv "Emmeline Burns really did love her father, despite his lack of presence in her life — or maybe because of it. They do say, after all, that absence makes the heart grow fonder."
    nv "Even when Phillip was not at home, Emmeline had a great deal to busy her day with, and she was never bored or lonely. She would help her mother with the embroidery, or she would exchange idle gossip with the servants, or she would go for long walks around the countryside, eating blackberries from the hedgerows and identifying the trees by their leaves."
    nv "Emmeline’s long-suffering governess, Helena Warren, certainly had her hands full when it came to disciplining her rowdy pupil. Though Emmeline was not unintelligent, she had been born with the disposition of a sea captain or a polar explorer, and she was physically incapable of remaining in one place for too long."
    nv "That is, unless she was with Cornelia Linton."
    
    nvl clear
    
    nv "Emmeline and Cornelia had known one another since they were both young girls, they were almost inseparable. They spent most of their waking hours together, sitting by the lakeside in the Lintons’ private estate."
    nv "They would stare out across the untroubled water, which carried along with it lily pads, reeds, and fish with shimmering scales, and they would talk, sipping raspberry lemonade."
    nv "Both Cornelia and Emmeline would wear pale colours during the summer, and they would pick at their long skirts in an attempt to cool themselves down, in a manner that would have appalled their mothers."
    nv "Fortunately, their mothers never intruded upon them when they were at the lake."
    
    nvl clear
    
    nv "Everyone in Barrowby knew that the lake in the Lintons’ estate belonged to Cornelia and Emmeline. They had claimed it through the countless hours they had whiled away by those grassy banks, feeding the fish and dipping their bare toes into the water, which made the two girls squeal. As such, it was their private land — a secret garden everyone knew of, but nobody was heartless enough to intrude upon."
    
    nvl clear
    nvl hide dissolve
    
    stop ambience fadeout 0.5
    hide image "grain" onlayer texture    
    scene bg lake
    show emmy3 smile n at left2_e
    show cornelia normal n at right2_c
    with tear
    window show dissolve
    
    play ambience "sfx/forest2.mp3" fadein 1.5
    play music "music/hikari.mp3" fadein 1.5
    
    em "So, how is your embroidery coming along?"
    
    show cornelia pout n
    play sound "sfx/thud.mp3"
    with hpunch
    
    "Cornelia pouted, giving Emmeline a light shove in the shoulder."
    c "Oh, please, do not ask me about my embroidery! You know better than anybody how dreadful I am at it. I have no hand-eye coordination whatsoever!"
    
    play sound "sfx/thud.mp3"
    with vpunch
    
    show emmy3 smirk a
    
    "Emmeline giggled, returning Cornelia’s shove with one of her own."
    em "I do not understand how you can be that terrible at sewing, Nellie. It is hardly a science!"
    show cornelia angry a
    c "It may be simple for you, but it is not so for me. Engaging in an activity I have no talent for is incredibly disheartening, and I keep poking myself in the fingers with the sewing needle."
    show emmy3 huh a
    em "Ooh, let me see!"
    show cornelia shock n
    c "What? No!"
    show cornelia pout n
    "Cornelia’s pout deepened, and she held her hands behind her back, attempting to hide them."
    c "Why do you wish to see my hands, anyway? Do you want to gloat?"
    show emmy3 shock n
    em "Me? Gloat? I would {i}never{/i}! I just want to see the wounds that have been dealt to you despite your best efforts, my dear Cornelia, so I may applaud you for your bravery!"
    show cornelia angry n
    c "Hmph. Forgive me for being so cynical, but I suspect you may be making fun of me."
    show emmy3 smile n
    em "Of course I will forgive you. You cannot help but be cynical, given your father fancies himself as a philosopher. It must run in your family."
    show cornelia frown n
    c "Indeed, he does. Our library is full of Hegel and Kant, though I doubt he understands it. Mother says he just wants to show off at dinner parties, like a peacock."
    show emmy3 huh a
    em "How is he able to show off if he is unable to understand the material he speaks of?"
    show cornelia normal a
    c "It is nothing more than bluster. Mother says pretence is one of the key traits a man must possess if he wishes to be successful in this world."
    show emmy3 smile n
    em "My father is a rather earnest man. He could not lie if his life depended on it — especially not about philosophy."
    show cornelia sad n
    c "And that is why my mother worries for you, Emmeline. She has said as much before."
    show emmy3 pout n
    em "She need not concern herself with my family! We may not be as rich as you, but what we lack in wealth we make up for with raw talent!"
    show cornelia shockblush n
    c "A-Are you saying I am not talented?"
    show emmy3 smirk a
    em "I am saying, it is somewhat sad that a fourteen year old girl such as yourself still cannot sew a single comforter."
    show cornelia angry n at bounce
    c "H-Hey...!"
    "Cornelia, who had let her guard slip as she pondered her father’s ill-fated attempts to ingratiate himself with the intelligentsia of the age, tried to obscure her hands behind her back once more, but it was already too late."
    
    show cg2_2 with wipe:
        size (1280, 720) crop (200, 260, 640, 360)
        linear 15.0 crop (320, 360, 640, 360)
    
    c "W-What are you doing, Emmy?"
    em "I am examining your hands, as I said I would — and, oh dear."
    "Emmeline tutted and shook her head, her fingers linked with Cornelia’s as lovers might."
    em "They are such beautiful hands, with such smooth skin, yet they are marked all over with red dots! It appears as though you have been used as a human pincushion!"
    c "I-I already told you, Emmy, I have no skills when it comes to sewing! Why must you tease me so?"
    em "I was not teasing you, I was honouring your efforts."
    c "T-That is a bald-faced lie, and we both know it! If you had any ounce of respect for me, you would not be smiling like that!"
    em "Like what?"
    c "Like {i}that{/i}. Now let go of me!"
    
    hide cg2_2
    show cg2_2
    with wipe
    
    "But Emmeline did not. Instead, she continued to stand there, skirts fluttering about her legs, attempting to peer into Cornelia’s grumpy little face with undisguised amusement."
    c "Emmy, I told you to let go! Why do you not heed my wishes?"
    em "Because seeing you blush is so much fun, of course!"
    c "E-Emmy...!"
    "If Cornelia had the use of both her hands, perhaps she would have hit Emmeline upside for the head for her insolence. As it was, she did not, given she was restrained by Emmeline, and all she could do was glare."
    "Glare, and blush."
    "Cornelia blushed a lot. That was one of the downsides of having such fair skin. That, and when she poked herself in the hand with the sewing needle, as she was so prone to doing, the red welts that resulted stood out sharply, starkly, against her milky complexion."
    em "Why are you acting so coy, Cornelia? I know you enjoy my company really."
    c "I... B-Be that as it may, you are behaving rather childishly right now, and I have no desire to indulge your whims."
    em "Honestly?"
    c "Honestly."
    em "Even if those whims are your own as well?"
    c "Well..."
    "Cornelia let her head hang, her face turning just a shade darker."
    "Certainly, this was not the first time that the two girls had held hands. They had been friends ever since they were small, and they were not unfamiliar with the sensation of the other’s skin."
    "In fact, they were more well versed with one another’s bodies than one might have expected."

    window hide dissolve
    nvl clear
    scene black
    show image "grain" onlayer texture
    with wipe
    nvl show dissolve
    
    nv "Though their mothers would have scolded them for the unladylike manner with which they comported themselves when left alone by the lakeside, they would have been {i}scandalised{/i} to learn of the other, more intimate, actions that had taken place between the two girls."
    nv "It had only been a month or so ago when, drunk on the lazy heat of the encroaching summer, the two girls had slowly, lackadaisically, shared their first kiss — not a kiss on the cheek, or the temple, as they had done during their babyhood, but a true kiss typically shared between adults of the opposite sex."
    nv "Neither of them knew who had instigated the kiss, or why they had lingered for so long in such a manner, their lips pressed together, but both agreed after the fact that they had liked it."
    nv "It had just felt right."
    
    nvl clear
    
    nv "As such, without giving these moments of intimacy too much thought, the two girls had continued to display their affection for one another in such a manner all through the summer of 1851."
    nv "Such kisses and caresses might have been uncommon between two women, but what of it? Why should they not kiss one another if they wanted to? The lakeside was their own private haunt, their secret garden, and nothing could intrude upon them there — not even so-called ‘common decency’."
    nv "That was another question: why {i}should{/i} it be indecent? Emmeline did not understand. She loved Cornelia, and Cornelia loved her, and was that not enough?"
    nv "Even if it was not enough for the rest of the world, it was more than enough for her."
    
    nvl clear
    nvl hide dissolve
    
    stop ambience fadeout 0.5
    hide image "grain" onlayer texture
    scene bg lake
    show emmy3 smile n at left2_e
    show cornelia normal n at right2_c
    with tear2
    
    window show dissolve
    
    play ambience "sfx/forest2.mp3" fadein 1.5
    
    em "You know, you really are beautiful."
    show cornelia shockblush n
    c "D-Do you honestly think so?"
    show emmy3 smile n
    em "Of course. I thought so, from the moment I was old enough to understand what beauty is. You are one of the loveliest people I have ever seen."
    show cornelia sadblush n
    c "I-Is that why you like me, then? Because you think I am pretty?"
    show emmy3 smirk a
    em "Maybe~ We humans are fickle beings, after all. Isn’t your father proof enough of that?"
    show cornelia poutblush a
    c "H-How cruel, Emmy! If you are only kissing me because you think I am pretty, then maybe I should re-evaluate the nature of our relationship! You are nothing more than a rake! You are even worse than that awful Wedgewood boy!"
    show emmy3 shock n
    em "You would compare me to Aubrey Wedgewood? My dear Cornelia, I am wounded! I am nothing at all like that boorish fop!"
    show cornelia frown n
    c "Well, I wonder. He can be awfully {i}insistent{/i}, too. It is not fitting for a young man."
    show emmy3 angry n
    em "Of course it is not fitting. Did you know, he even deigned to take my hand during your mama’s garden party last week?"
    show cornelia shock n
    c "Honestly?"
    show emmy3 angry2 n
    em "Indeed! I would have slapped him, Nellie, had his mother not happened upon us."
    show cornelia frown n
    c "Did she scold him?"
    em "Lady Wedgewood? Of course not."
    "Emmeline spat on the floor, and did not even have the courtesy to wipe her mouth with a handkerchief afterwards."
    "Under normal circumstances, Cornelia would have scolded Emmeline for her poor manners, but on this score she relented. Thinking about Aubrey Wedgewood often made her want to spit, too."
    show emmy3 angry n
    em "She dotes on that spoilt son of hers. Why, she probably believes him to be the second coming of Christ, though he flirts with every single woman in the village, old or young!"
    show emmy3 angry2 n
    em "You see, Nellie, I am nothing like Aubrey! I would rather die than become a rover like him!"
    show emmy3 smirk a
    em "My feelings for you, my dear Cornelia, are moulded from a different cast. You have captured my heart with your ephemeral beauty, and now mine eyes can wander no further! You are my sweet red rose, newly sprung in June!"
    show cornelia shockblush n
    c "W-Well..."
    "Cornelia, flustered though she was by Emmeline’s teasing, had enough wits about her to recognise that line."
    "Such a literary reference would have flown over her father’s head like a bluebird, but Cornelia, despite being only fourteen, was probably more intelligent than he was. She must have inherited it from her mother, Beatrice Linton, who was a most formidable figure."
    show cornelia frown n
    c "Are you quoting poetry at me now, Emmy?"
    show emmy3 wink a
    em "Indeed. Did you know that my love is like the melody, sweetly played in tune?"
    show cornelia poutblush a
    c "D-Don’t be an idiot! If you wish to serenade me, you could at least write a poem of your own!"
    show emmy3 smirk a
    em "I know you appreciate it really, though!"
    show cornelia frown a
    c "I-In all honesty, I think you are being rather foolish, Emmy."
    show emmy3 smile n
    em "I cannot help myself, though. I really do love you, Cornelia! I love you so, sometimes I fear I may go mad!"
    show cornelia normal a
    c "What do you know of madness?"
    show emmy3 ehe n
    em "I know, when you are not by my side, I miss you horribly, and I find myself counting down the minutes — nay, the very {i}seconds{/i} — until we may be in one another’s company once more!"
    show cornelia sadblush n
    c "Ah... Well, um... I appreciate your feelings, Emmy. I, um..."
    c "I..."
    show cornelia smileblush n
    c "I love you, too."
    
    stop music fadeout 1.5
    stop ambience fadeout 1.5
    
    window hide dissolve
    scene black
    show image "grain" onlayer texture
    with wipe
    
    nvl show dissolve
    nvl clear
    
    nv "If only Emmeline and Cornelia could have always spent their time together in so sweet a manner, smiling and laughing, or else bickering pointlessly and making one another pout, yet always parting with words of love and kisses stolen beneath the warm summer sun."
    
    play music "music/sad.mp3" fadein 1.5
    
    nv "Unfortunately, such moments cannot last forever. The splendours of summer soon faded, and the leaves began to turn brown, and the wind gained a sharp edge that made Emmeline shiver."
    nv "It was also, during the autumn months, that Phillip Burns returned home for the first time in half a year."
    nv "This reunion, however, was not quite as happy as the previous ones had been."
    
    nvl clear
    
    nv "Phillip Burns had always been a small man, yet he seemed even smaller during that bitingly cold September. He stooped more than usual when he entered rooms — if he entered them at all, for he had now developed a habit of lingering, ghostlike, about the thresholds of his own home, as though afraid to step inside."
    nv "It was almost as though, during his six month sojourn in London, he had lost something crucial to his constitution — his sense of self, or else his soul."
    nv "Though Phillip’s feet were still planted firmly upon the earth, he was divorced from the world around him. He drifted about aimlessly, like a sleepwalker, yet was restless within his dream world, incapable of sitting still for more than five minutes at a time."
    
    nvl clear
    
    nv "He looked at things without seeing them, ate food without tasting it, held objects without touching them. Once, he tried to pick up his glass during dinner, and used so little force it slipped between his fingers, smashing into pieces against the floor."
    nv "Even when he spoke to Emmeline, it was without any real feeling to his voice, as though he were reciting words from a play script — and Phillip Burns had never been a very good actor."
    nv "He was not like Cornelia’s father, who had so much huff and puff he could have blown down even the brick home built by the most industrious of the three little pigs. Phillip Burns was far too honest, and that was the worst thing."
    
    nvl clear
    
    nv "It was because he was an honest man that Emmeline knew, though he tried to keep the truth from her."
    nv "Something was wrong. Something was terribly, terribly wrong."
    nv "But she did not know what."
    
    nvl clear
    nvl hide dissolve
    
    stop music fadeout 0.5
    stop ambience fadeout 0.5
    
    hide image "grain" onlayer texture
    scene bg lake
    show emmy2 frown n at left2_e
    show cornelia normal n at right2_c
    with tear
    window show dissolve
    
    play ambience "sfx/forest2.mp3" fadein 0.5
    
    c "Are you all right, Emmy?"
    show emmy2 huh a
    em "Hm?"
    "Emmeline blinked, brushing a few strands out of hair out of her face, and turned to survey Cornelia."
    show emmy2 frown n
    em "Why do you ask me that? Was my face contorted in a curious manner?"
    show cornelia sad n
    c "I suppose you could say that. You have been acting rather more despondent than usual, that is all."
    
    play music "music/lazy afternoon.mp3" fadein 1.5
    
    show emmy2 smirk a
    em "Heh."
    "A catlike smile crossed Emmeline’s lips. She leant forwards, until her nose was only inches apart from her companion’s, and said, in hushed tones:"
    em "Are you worried about me, Nellie?"
    show cornelia shockblush n
    c "I... I-I..."
    
    show cornelia angry2 a
    
    c "I {i}was{/i} worried about you, but I shall not worry any longer if you insist upon acting like that!"
    show emmy2 smile a
    "Emmeline only giggled, unmoved by Cornelia’s violent protestations (she was hardly strong enough to cause any lasting damage), and rearranged her hair."
    em "Seeing you blush always cheers me up, my dear Cornelia."
    show cornelia frown n
    c "So you admit you were feeling unhappy earlier?"
    show emmy2 frown n
    em "Just a touch. I cannot help myself. Not when Father has been acting in such a peculiar manner. He shambles about the house like an animated corpse — like the misunderstood creature from Mr. Shelley’s novel!"
    show cornelia frown a
    c "Mr. Shelley? I thought the author of {i}Frankenstein{/i} was Mrs. Shelley, not her husband."
    show emmy2 huh n
    em "Oh, I am unsure of the details, Nellie. Both Mother and dear old Ellie say a woman could not have written such a twisted tale, and I am unsure who to believe. In any event, it does not particularly matter."
    show cornelia normal n
    c "Probably not, no."
    
    stop music fadeout 1.0
    
    show emmy2 frown a
    "Emmeline sighed, running a hand through her auburn curls. She soon found her bonnet rather got in the way of this gesture, so she untied the ribbon beneath her chin and removed the offending garment."
    
    hide emmy2
    show emmy3 frown n at left2_e
    with dissolve
    
    "She let her bonnet sit in her lap, as a mother might with a newly born babe, and played with the light green ribbon, twisting it about the wrist of her right hand. The sensation of the soft, smooth material against her skin was comforting, like a caress."
    
    play music "music/sad.mp3" fadein 1.0
    
    show emmy3 sad n
    em "To be quite honest, I {i}have{/i} been rather concerned about father as of late. Just this morning, he missed a stair during his descent into the hallway, and sprained his ankle. Could have broken his leg."
    show cornelia sad n
    c "But he did not?"
    show emmy3 frown n
    em "No, he did not. He does look rather undignified now, though, limping everywhere like an invalid."
    show cornelia sad a
    c "Oh, Emmy..."
    "Cornelia shook her head, her eyes heavy with concern."
    show emmy3 sad n
    "Emmeline shifted, still playing with the ribbon of her bonnet. The look on Cornelia’s face was too sombre for a playful forest sprite such as herself, and it unsettled her."
    "She did not want to think about her father."
    "She had retreated to the Lintons’ estate, despite the protestations of Miss Warren (‘You have not finished with your history lesson, Emmeline! I doubt you could tell Queen Elizabeth apart from a hole in the ground!’), so she could avoid thoughts about her father."
    "This was rather new for Emmeline. She had always loved being with her father. Now, however, she found herself seeking any recourse available to her in order to avoid him."
    "Seeing him like this, so small and sad, shuffling about his home like a repentant sinner, was too painful."
    show cornelia sad n
    c "When you return home, would you give your father my regards? Mother is awfully concerned about him — and you too, Emmeline."
    show emmy3 pout n
    em "Hmph. Beatrice Linton {i}would{/i} be concerned. She has always loved poking her nose into other people’s business."
    show cornelia angry2 a
    c "S-She is not doing it because she enjoys idle gossip! You should know better than anyone that my mother deplores that kind of behaviour! She believes it to be most unladylike!"
    show cornelia sad a
    c "She could not help but be worrried, given what she has read in the papers lately! Your family has a great deal invested in the East Anglian Railways, do they not?"
    show emmy3 angry2 n
    em "Don’t talk to me about business, Nellie. I can’t understand it at all."
    show cornelia frown a
    c "I am sure you could if you tried. You have just been raised to believe that you should not bother."
    show emmy3 pout n
    em "Gosh, you sound more and more like your mother every day."
    show emmy3 sigh n
    "Emmeline exhaled, tightening the ribbon of her bonnet about her wrist so much so it started to hurt."
    show emmy3 frown n
    "Though the material was soft, intended for wear by young women with silken skin who had never worked a day in their privileged little lives, it chafed when she wound it as such about her wrist."
    "It was strange, Emmeline mused, how something as innocuous as a ribbon could cause harm when it was used with malicious intent."
    "This world was a more dangerous place than she had ever truly given it credit for. Even the lake, which she had often gazed upon with Cornelia, could be hiding some rather more sinister secrets."
    show emmy3 sad n
    em "I apologise, Nellie. I don’t mean to snap at you. I have been rather highly strung as of late. It must be because of the atmosphere at home."
    show cornelia normal n
    c "Do not fret, Emmy. I understand."
    show emmy3 sadshock n
    em "Y-You do?"
    show cornelia sad2 n
    c "Perhaps not entirely, but I will try to. I, um... I do care about you, after all."
    show emmy3 ehe n
    em "Ehehe. Thank you, Nellie."
    
    stop music fadeout 2.5
    
    show cornelia smileblush n
    "The two girls surveyed one another, both unusually shy, hesitant, their faces lightly flushed."
    show cornelia pout a
    "Then, with a tut, Cornelia leant forwards, brushing the tips of her fingers against Emmeline’s wrist."
    c "You should not do that."
    show emmy3 frown n
    em "What?"
    c "Fiddle with your bonnet like that."
    show emmy3 smile n
    em "Because it is unbecoming of a lady?"
    show cornelia frown a
    c "Because you are hurting yourself. Your poor hand has gone white. The blood cannot flow through your body properly if you impede it like that."
    show emmy3 smile a
    em "Ehehe~ And your hands, by contrast, still appear to be red, Nellie."
    
    play music "music/hikari.mp3" fadein 2.0
    
    "Emmeline giggled in that easy, light-hearted manner of hers, and began to unwind the ribbon from about her wrist."
    show emmy3 smirk a
    em "Are you still yet to master the scared art of the cross stitch?"
    show cornelia shockblush n
    c "T-That is neither here nor there! I am trying to comfort you, Emmeline!"
    show emmy3 smirk2 a
    em "And you have been doing a wonderful job. Gazing upon your myriad imperfections always cheers me!"
    show cornelia sadblush a
    c "You are so cruel, Emmeline... Sometimes, I feel like you do not truly love me — you just love toying me."
    show emmy3 smile n
    em "Now, now, where did you get a silly idea like that?"
    "Emmeline smiled, with a touch less sarcasm than before, and leant forwards. Then, moving quickly, as a kittiwake might pluck a fish out of the water, she pressed a chaste kiss against the corner of Cornelia’s lips."
    em "I love you more than ever, Nellie! Nothing could quell my feelings for you — not a raging storm, or a howling wind!"
    show cornelia shockblush a
    "Cornelia pressed one hand against her cheek gingerly. The spot where Emmeline had kissed her tingled. It felt much like being poked with a sewing needle (a sensation Cornelia was depressingly familiar with), yet it was not unpleasant."
    show emmy3 smile a
    em "Your blushes truly are beautiful, Cornelia! They would even outdo the roses in the very height of summer! It makes me wish I could kiss you every single second of the day, if it would always elicit such a lovely response!"
    show cornelia shockblush n at bounce
    c "I do not think my heart would be able to cope with such a constant slew of affection. You would kill me, Emmy!"
    show emmy3 huh a
    em "And what better way would there be to die, than to be kissed fervently by a girl you love?"
    show emmy3 smile n
    "And, with a light giggle, even breezier than that of the coastal air, Emmeline pressed another kiss against the side of Cornelia’s mouth."
    show cornelia sadblush n
    c "Y-You know, you should ask for my permission before you do such things. I am not quite as hungry for affection as you are."
    show emmy3 smirk a
    em "So you say, but you did not offer much resistance!"
    show cornelia frown n
    c "Hmm. That sounds like something Aubrey would say."
    show emmy3 shock n
    em "N-Never! You would not seek to compare me to that cur {i}again{/i}, would you, Nellie?!"
    show cornelia smirk a
    c "I am simply saying what I see. You claim you dislike Aubrey, but you grow more and more like him with every passing day."
    show emmy3 angry2 n
    em "T-That is a lie! Libel! Slander! Take it back!"
    show cornelia frown a
    c "No."
    play sound "sfx/thud.mp3"
    show emmy3 pout n at bounce
    em "Take it back, I said!"
    show cornelia normal a
    c "I refuse."
    show emmy3 angry n
    em "Well, I insist!"
    show cornelia smirk a
    c "If you wish for me to change my mind, you will have to insist harder than {i}that{/i}."
    show emmy3 smirk a
    em "All right then, how is this?"

    scene black with wipedown_fast
    play sound "sfx/thud.mp3"
    with vpunch
    
    "And with a devilish glint in her eyes, which would have been evidence enough in 17th century England to try her as a witch, Emmeline shifted forwards and began her merciless assault."
    "Not even William of Normandy, as he drove back the armies of Harold Godwinson during the Battle of Hastings, could have conceived of such brutality."
    
    show cg1 with eyeopen
    
    c "E-Emmy! Emmy, stop that!"
    "Cornelia kicked and squealed, pushed backwards against the ground by Emmeline’s sudden siege, but it was to no avail. Emmeline had the element of surprise on her side, and she had taken a clear advantage."
    "Cornelia blinked up at Emmeline, squirming like a hooked fish, as Emmeline sat astride her, skirts rucked up her thighs, her fingers trailing lines across Cornelia’s prone body — beneath her chin, under her arms, against her sides."
    "Was there any war tactic more devilish, more devious, than that of tickling? And this was not just any tickling, oh no. This was {i}extreme{/i} tickling, that would surely end in bloodshed."
    c "Emmy, stop! Get off me!"
    "Cornelia implored breathlessly, choking the words from between her pursed lips, but the indomitable Lady Emmeline remained unmoved."
    em "No, I will not! Not until you recant what you said!"
    c "That you are like Aubrey?"
    em "Indeed! Admit it to be nothing more than a lie, and I may spare your life!"
    c "N-No, never! I stand by my word...!"
    em "Then I will stand by my actions! I will not stop until you surrender, Nellie — and I warn you, I can be very persuasive when I want to be!"
    "And, her eyes hardening like the steel of a sword’s blade, Emmeline dipped her head and began to press kisses against Cornelia’s neck."
    "Cornelia’s dress had begun to slip down her shoulders, and there was a good deal of pale pink skin on show — more than would have been deemed socially acceptable."
    c "A-Aah! You rogue! You would attack a helpless young girl?!"
    em "Only because this helpless young girl is attempting to defile my honour!"
    c "S-So you would seek to defile {i}me{/i}?"
    em "Well, I wonder..."
    "Cornelia squealed as though she had been doused in water, and re-doubled her efforts to escape, but it was all in vain."
    
    scene bg lake with wipeup_slow
    
    "Both giggling, the two girls continued to bicker playfully, even as the warmth of the sun began to dissipate, and an autumnal chill set into the air."
    "At that moment, even as the day drew to a close, the two girls may truly have believed, with their rumpled clothes and disorderly hair and flustered cheeks, that this could last forever."
    
    stop music fadeout 1.0
    stop ambience fadeout 1.0
    
    window hide dissolve
    scene black
    show image "grain" onlayer texture
    with wipe
    nvl show dissolve
    
    nvl clear
    
    nv "Emmeline Burns was dreaming, though she was not sure of what, entirely. Her dreams were mostly comprised of vague shapes and distorted sounds, as though she were viewing her own fantasy lands from behind frozen glass or through a fine film of water."
    nv "Sometimes, however, she dreamt of Cornelia. She always knew when she had dreamt of Cornelia, though she rarely remembered the details of her dreams, because when she awoke it was with a silly smile on her face, and a soft flush across her cheeks and nose."
    nv "That was how she had realised she was in love. She was always thinking of Cornelia, even during the rare occasions when Cornelia was not beside her."
    
    nvl clear
    
    nv "Though Emmeline was only fourteen, and did not fully understand love, she did not need to. Why trouble herself over the intricacies of the four letter word when she could, instead, be doing things that made her happy? Those things being, chiefly, talking to Cornelia, braiding her hair, making her blush, and kissing her lips, her cheeks, her eyelids — Emmeline was not particularly picky."
    
    nvl clear
    
    play ambience "sfx/clock.mp3" fadein 2.5
    
    nv "On this particular night, however, Emmeline did not awake to find sunlight streaming in through her window, half-formed remembrances of her love flitting through her mind."
    nv "She did not awake during the morning at all."
    nv "It must have been late at night, because it was pitch black in her bedroom, and she could not hear the birds."
    nv "Earlier than five, then, she assumed, for she had no way of knowing if this was correct or not. It was so dark in her room she could not see the clock that hung on her wall, though she could hear its ticking."
    
    nvl clear
    
    nv "The first point she was aware of, other than the oppressive darkness, was that it was cold."
    nv "The chill of winter was well and truly setting in, especially during the night, and she could no longer sleep with bare arms and a light coverlet, as she had done before."
    nv "Her summer sleepwear had been packed away at the back of her wardrobe, and the maids now set her winter nightgowns on her bed before she went to sleep, complete with puffed sleeves and high collars."
    nv "The second thing Emmeline noticed, as her eyes slowly grew accustomed to the dark, was that she was not alone. There was somebody else in the room with her."
    nv "It was none other than her father, Phillip."
    
    nvl clear
    
    nvl hide dissolve
    
    stop ambience fadeout 1.0
    
    hide image "grain" onlayer texture
    scene bg room2
    show emmy shock n at cent_e
    show night
    with eyeopen
    window show dissolve
    
    play music "music/sad.mp3" fadein 1.0
    
    "Emmeline stared at her father with big eyes. He looked back at her, and Emmeline could tell, despite the dark, his countenance was just as surprised — if not more than — than her own was."
    "Had his face always looked so lined, his mouth so drawn? Perhaps it was the shadows playing tricks on her eyes, but he looked far older than his forty four years."
    "Emmeline swallowed. All of a sudden, her throat felt dry."
    show emmy sad n
    em "Father? Is something wrong?"
    p "Ah, um... N-Nothing’s wrong, Emmy. Nothing at all."
    "But he did not look at her face, and he stuttered when he spoke."
    "Why did he sound so frightened? Had something bad happened? Emmeline could not think of any other reason why he would be in her room at such an hour, looking so very tired — no, tired did not even begin to describe it."
    "He looked {i}haggard{/i}, as though on the brink of death, and his hands would not stop shaking, even when he clenched them into fists."
    "Emmeline sat up in bed, the covers falling about her body like a funeral shroud, and looked at her father with concern."
    show emmy sad2 n
    em "It isn’t Mother, is it? Is she sick?"
    p "Y-Your mother?"
    "Once more, Phillip’s voice faltered. He winced, as though assailed by a sudden, unpleasant memory, and turned his head away."
    p "Your mother is fine, Emmy. She should be sleeping now."
    show emmy frown n
    em "Oh."
    "A pause."
    show emmy sad n
    em "And why are you not asleep, Father? Could you not?"
    p "No, I... There is something I have to do."
    show emmy huh a
    em "At this hour?"
    p "Yes. It is of upmost importance. I don’t imagine you would understand, though."
    show emmy shock n
    "Emmeline flinched. Her father’s voice was strangely hard, despite the nervous stammer, and she was not used to him talking to her in such a way."
    show emmy sad n
    "Maybe other girls’ fathers spoke in such terse, clipped terms — Cornelia’s father sometimes did, when Beatrice wasn’t there to chastise him — but not her father. Not Phillip Burns."
    "There was no warmth to his voice, no tenderness. It was almost as though he were speaking to a stranger, rather than his dear daughter, his priceless jewel, his lovely little Emmeline."
    show emmy sad2 n
    em "I may not understand what is it you wish to do, Father, but I am sure I could help...?"
    p "No. You cannot help. Nobody can."
    show emmy shocksad n
    em "But—"
    p "I appreciate the offer, Emmy, but it... It is far too late."
    "Her father swallowed. Emmeline could hear it. It sounded painful, as though he were attempting to choke down a lead bullet, or a piece of steel shrapnel."
    show emmy sad2 n
    show emmy shocksad n
    em "I... I do not understand. If you do not believe I can help you, why did you come to my room at such an hour? What is it you wish to discuss with me, father?"
    p "There... I... Oh, God..."    
    "Phillip’s shoulders shook. It sounded like he was trying to stem a flow of oncoming tears, though he was not entirely successful. He bit down on his lower lip, but moisture still sparkled in the corners of his eyes, threatening to spill down his cheeks like April rain."
    "If Grandmother Patience were here, she surely would have mocked him. She always had done when Phillip was a child."
    "Perhaps that was why Phillip never visited Grandmother Patience. She made him feel like a young boy again — small, stupid, and utterly insignificant."
    "That was why Phillip had gone into banking, though he was not suited for such a cut-throat industry. He didn’t have the knack for it. Never had done. Grandmother Patience had said as much, but he was determined to prove her wrong. He wanted, for once in his life, to make her proud."
    "And look what that had cost him."
    "His wealth. His reputation. And now, worst of all... His family, too."
    "But there was no going back now. He had already come too far. It was bad luck that Emmeline had woken when she had (the girl had always been a light sleeper), but he could not abandon his plans now, half-finished. That would have been even crueller."
    show emmy shocksad2 n at bounce
    em "Father? Father, are you all right? What’s wrong?"
    p "Emmeline... Oh, my dear Emmy... I am sorry. I am so, so sorry."
    show emmy sad2 n
    "And with that, the tears finally began to escape from Phillip’s eyes, one after the other. They trickled down his cheeks slowly, sombrely, like a funeral procession, icy cold against his pale skin."
    p "I tried to be a good father, Emmy, I really {i}did{/i} try. I wanted to be kind. I wanted to be fair. I had no intention of treating you like my parents treated me, but I..."
    p "I was incapable of doing it. In the end, it all went wrong. I thought I knew what I was doing. I thought I was succeeding — and for a few moments, maybe it was. Now, I realise that was a foolish fantasy dreamt by a foolish man."
    p "My mother was right. I should have been drowned when I was younger. It would have saved you all so much trouble."
    p "It would have... made everything so much easier..."
    show emmy shocksad n
    em "F-Father?!"
    
    play sound "sfx/footsteps2.mp3"
    hide emmy
    show emmy shocksad n 2 at close behind night
    with dissolve
    
    "Emmeline got to her feet, her bare toes curling against the wooden floor, and took a few steps towards her father. Her nightgown fluttered about her thighs as she walked, her hair curling about her face."
    show emmy shocksad2 n 2
    em "Are you not feeling well? We can summon the physician if you would like, if only you would sit down! Why, look how much you are trembling!"
    p "No. No, no, no..."
    "Phillip shook his head mechanically, back and forth like a tin soldier, his words spoken in an almost frenzied fervour."
    p "The physician cannot help now. Nothing can help. We’re done for, Emmeline — you and I, and your mother, too. This is it. This is the end."
    show emmy shocksad n 2
    em "T-The end of what, exactly?"
    p "Our money is all gone, Emmeline! I made a terrible mistake, and now everything is gone! The bubble burst, and we lost it all. Every single thing!"
    show emmy shock n 2
    "Emmeline stared at her father, her lips pursed like those of the fish in the Lintons’ pond. She did not know what to do, what to say. What could she say?"
    show emmy sad n 2
    "She was only fourteen years old, and she had always been told by her mother that women had no place in the world of business — that they could not understand facts and figures, and tables of numbers."
    "Beatrice Linton was the exception, rather than the rule. Beatrice Linton could do anything. She probably could have wrestled a bear to death with her own two hands, if needs be. But Emmeline could not."
    "She was only a young girl, standing in her bedroom in her winter nightgown, shivering like a leaf, and she did not know what to do. What she could do."
    "She did not need to ponder this for much longer, however."
    p "I’m sorry, Emmy. I’m so, so sorry. I let you down. I let you down, and now... This is the only thing I can do to make amends."
    show emmy shocksad n 2
    em "F-Father? W-What are you—?"
    "But Emmeline was not able to finish her question."
    
    stop music
    scene black
    with vpunch
    
    "That is because, at that moment, Phillip Burns closed the distance between them, and held his hand around his daughter’s throat."
    
    play music "music/dark.mp3" fadein 1.0
    
    show cg4_2 with wipe:
        size (1280, 720) crop (540, 300, 640, 360)
        linear 13.0 crop (350, 150, 640, 360)

    "His fingers dug into her skin hard, as a child might grasp a favourite toy, and Emmeline could not breathe. First, it was the shock that drew the air out of her lungs, but then it was the pressure about her throat, choking her."
    "She could hardly believe it. How could her father, who had never raised a hand to her in his life — who had never raised so much as his voice — even {i}contemplate{/i} carrying out such a hideous action?"
    "But he was."
    "He really was going to kill her."
    
    hide cg4_2
    show cg4_2
    with wipe
    
    "Emmeline felt herself grow faint. She wondered, idly, if dark purple bruises would be left around her throat when Phillip let go — a garish ring about her neck, like a fairy’s circle made of mushrooms."
    "Her head swam. Her legs gave way beneath her, and she fell backwards onto her bed."
    
    play sound "sfx/bed.ogg"
    with vpunch
    
    "Still, Phillip’s fingers did not move. They remained upon her throat, fixated with the gruesome task they been charged with."
    "It was almost as though Phillip Burns had split in two. One half remained focused on the murder of his dear daughter, his beloved Emmy, while the other, appalled at his actions, looked away with self loathing and disgust."
    "Maybe he should have poisoned her nightly mug of hot cocoa instead. Then, he wouldn’t have to bear witness to the look on her face, as the life was slowly choked out of her tiny body."
    p "I’m sorry, Emmy... I’m so, so sorry..."
    "And he was, too. His cheeks were wet with tears, and more tears kept falling. Some of them splashed against Emmeline’s cheeks, but this offering of remorse made little difference to the situation at hand."
    "Emmeline was still dying."
    
    play sound "sfx/beat.mp3" fadein 1.0
    
    "She had been dying for around two minutes now, though it felt far longer, and her heart was already beginning to stammer inside her chest."
    
    stop sound fadeout 1.0
    
    p "I am doing it for you, Emmy. It’s for the greater good, I promise. I cannot stand the thought of my little girl to go to the workhouse. I just couldn’t, I... I..."
    "But Phillip did not know what else to say. He doubted it would have made much of a difference."
    
    stop music fadeout 2.0
    
    window hide dissolve
    scene black with eyeclose
    window show dissolve
    
    "Emmeline stared blankly up at the ceiling, her eyes a vast sea of white, her mouth hanging open. Her arms and legs were limp, and though her body was warm, it did not move. It could not."
    "Phillip removed his hands from Emmeline’s throat, his whole body trembling. Emmeline did not stir. Her eyes remained open, unfixed, misty with death."
    p "Emmy... Oh, my Emmy... My little Emmy..."
    
    play ambience "sfx/clock.mp3" fadein 0.5
    
    "And, with a choked sob, Phillip pulled his dear little girl — who was now a very dead little girl — into his arms, and wept."
    
    stop music fadeout 1.0
    window hide dissolve
    $ renpy.pause(3.0)
    stop ambience fadeout 0.5
    scene bg barrow
    show fog_bg
    show toma shock n at left2_t
    show emmy frown n at right2_e
    show emmy_bruises at right2_e
    show fog_fg
    with tear
    window show dissolve
    
    e "After that, Phillip Burns killed himself. He set the house ablaze, then slit his throat with a knife."
    e "Torching the house may seem like something of a waste, but if he had not, he would not have been buried with his wife and child. He had to make it look like an accident somehow."
    e "Of course, Emmeline was not there to witness that, but she found out within due course."
    show emmy sad n
    e "And that is the end of the sad story of Emmeline Burns."
    
    play music "music/sad.mp3" fadein 1.0
    
    show toma sad a
    t "I... I..."
    show toma sad3 a
    "I open and close my mouth, but no sound comes out. I don’t know what to say."
    show toma sad2 a
    "I had already suspected it, vague speculations about being an internet celebrity aside, but I have no doubts left in my mind after hearing Emily’s story."
    "This girl is no Emily. I knew she was no Emily from the moment she introduced herself. Now, I know who she really is."
    show toma sad n
    "Emmeline holds one hand to her throat, rubbing it gently, as though nursing a cold."
    show emmy frown a
    em "I wish he had not choked me. I imagine he did it because he thought it would be less violent than stabbing me, but it took so long to die. Three whole minutes."
    show emmy sad n
    em "Worst of all, I could still think during that time. I could grieve. I could suffer."
    show emmy frown a
    em "It gave me enough time to form regrets... and maybe that is why I could not die properly."
    show emmy frown n
    "Emmeline sighs, resting a hand against the top of her own gravestone. Unlike the ghosts in films, her hand doesn’t pass through it. Instead, her fingers make contact, firm and solid, and I even see her shiver when the coldness of the stone permeates her pale skin."
    em "Maybe Grandmother Patience was right in her assessment of Father’s character. He does not have the determination required to properly see things through until the end — not even murder."
    show emmy angry3 n
    em "I suppose I should congratulate him for trying, though. He really {i}did{/i} try. It hurt horribly."
    show toma shock n
    "I open my mouth once more, but I don’t know what to say. How can I reply to that?"
    
    window hide dissolve
    scene bg toma op with wipe
    
    w "What must it have felt like, being betrayed so deeply by your own dad?"
    w "I don’t know, because I don’t have a dad of my own."
    w "Of course, this isn’t true in the strictest sense of the word — I am {i}not{/i} a product of divine conception, and a human man did have a hand in my existence."
    w "I don’t feel like I have a dad, though. Mum never talks about him, and I never thought to ask."
    w "I know Mum doesn’t like thinking about Saul Andrews — or ‘that git’, as she calls him when she is in a charitable mood (she calls him far worse when she is not) — and I don’t like thinking about him, either."
    w "At any rate, I don’t have much to think about. I’ve never met him before, and I’ve only seen his face in photographs. Mum threw most of the memorabilia of her seven months spent with Saul Andrews away."
    w "I can’t say I blame her, given how he reacted to the news of my mum’s pregnancy. Apparently, he tried to coerce her into having an abortion, and when that didn’t work he turned tail and fled. Didn’t even leave a note."
    w "What a git."
    w "I always thought I should hate Saul, but I don’t even know him enough for that. Instead, all I feel is... an absence of feeling, really. Apathy."
    
    scene bg tomaemmy with wipe
    
    w "Now, I can’t help but wonder who has it worse, even though I know making such comparisons is fundamentally unfair."
    w "Is it Emmeline, whose dad loved her dearly — to such an extent it wrung the life right out of her lungs?"
    w "Or is it me, whose dad cared so little for my existence he didn’t even stick around to see me being born, and hasn’t made a single attempt in the last fourteen years to contact me?"
    w "They’re both bad in their own ways — and if my mum had bowed to Saul Andrews’ wishes, I would be dead, too."
    w "The fact remains, however, that I am not."
    w "Emmeline, meanwhile, is."
    
    window hide dissolve
    scene bg barrow
    show fog_bg
    show toma sad n at left2_t
    show emmy frown n at right2_e
    show emmy_bruises at right2_e
    show fog_fg
    with wipe
    window show dissolve

    t "Do you resent him?"
    show emmy sad a
    em "I... I do not know. I have had a lot of time to think about it, but I still can’t come to a decision. Trying to describe it with mere words would seem inadequate, somehow, but..."
    show emmy sad2 a
    em "I am... upset. I wish it had never happened."
    show emmy sad n
    em "I know Father thought he had to do it, and I am sure it took him a good deal of thought before he was able to even {i}consider{/i} killing me and my mother. He was not a violent person. I know it might sound cliché, but he did not even like killing moths or spiders. And yet..."
    em "A person like him — spineless, Grandmother Patience said — was still able to murder his wife and child, then slit his own throat."
    show emmy sad2 n
    em "Our financial situation must have been bad, if he thought this was the only way he could save us. I don’t profess to fully understand it myself, but there must have been a reason behind his actions."
    em "Men — not even the most hot-headed men — do not murder their wives and daughters on sudden whims, or whispers from fairies. He must have been in a difficult position, so perhaps I feel some sympathy, but..."
    
    stop music
    play sound "sfx/thud.mp3"
    show emmy angry4 n
    with vpunch
    
    em "At the same time, it just isn’t fair!"
    
    play music "music/dark.mp3" fadein 1.0
    
    show emmy angry2 n
    em "He never even asked me what I wanted — and I certainly did {i}not{/i} want to die!"
    em "I wanted to stay alive! There were so many more things I wanted to do! I don’t know what things I wanted to do, not exactly, but I was young, and I had a whole lifetime ahead of me! I thought I could think about it later. I thought I would have enough time..."
    show emmy sad2 n
    em "But I was naïve."
    show emmy shocksad2 n
    em "I just wanted to spend more time with Cornelia. Even though I was young, and I did not understand a great deal about the world around me, I..."
    show emmy sad3 n
    em "I know that I loved her. I loved her with all of my heart."
    show emmy sad2 n
    em "And then my father killed me, and was the end of that. At least, it {i}should{/i} have been. I should have stopped loving her the moment my heart stopped beating, but..."
    show emmy sad3 n
    em "Evidently, it did not pan out like that."
    show toma sad a
    t "And... Do you know what happened to Cornelia?"
    show emmy frown n
    em "Bits and pieces. She was upset after I died, I think. She cried a lot. Then she grew older, and was eventually able to put what happened behind her."
    em "She’ll be dead now. She must have been dead for a century or so."
    show emmy heh n
    "Emmeline smiles bitterly."
    em "Almost as long as me."
    show toma sad n
    t "You didn’t see her?"
    show emmy sad n
    em "I tried to talk to her, but she could not see me. I hung around her for a little while, but it all felt so pointless."
    em "I could see her face, but I could not dry her tears. I wanted to tell her I was all right, I was right there — as all right as a dead girl can be, anyway — but it was all in vain. There was nothing I could do."
    em "In the end, I decided to cut my losses and leave her alone. Following Cornelia did not make her happy, and it definitely did not make {i}me{/i} happy. It just made me feel even more alone."
    show emmy sad2 n
    em "I have not left this graveyard in almost a century. There was no reason to leave. I just stayed right here, by my grave, and slept. A century might seem like a long time, but it slipped by rather quickly. Nobody could see me, and so nobody bothered me."
    
    stop music fadeout 1.0
    
    show emmy frown n
    em "At least, until today."
    
    play music "music/sad.mp3" fadein 1.0
    
    show emmy normal n
    em "You are the first person I have met, during the last one hundred and fifty years, who can see me. It is most peculiar."
    show toma ehe a
    t "Well, I... I-I’m quite a peculiar person. I {i}have{/i} always liked graveyards."
    show emmy smile a
    em "Ah, yes. You told me that earlier. I remembered."
    show toma shockblush a
    t "You, um... You don’t think I’m weird, do you?"
    "I know the other girls at my school do, but it would be rather depressing if a being as improbable as the ghost of 19th century girl thought I was weird {i}too{/i}."
    show emmy ehe n
    em "Perhaps a little, but I am rather happy about it! If you were not ‘weird’, as you termed it, you might not be able to see me, and we would not be able to have this refreshing conversation!"
    show toma frown a
    t "It might not be because of me, though."
    show emmy huh a
    em "What do you mean? You are regarding me with your own two eyes, correct? You have not stolen anybody else’s, have you?"
    show toma shock n
    t "N-No, of course not!"
    "If I had taken somebody’s eyes, where would I be storing my own? The thought is so macabre it makes me shudder."
    show toma pout n
    t "My eyes belong to me, and only me."
    show emmy smile a
    em "Well, that is a relief. I may be dead already, but one cannot be too careful."
    show toma gneh3 n
    "Though this girl just spoke of a rather tragic story — one pertaining to her, no less — there’s a light smile flitting about her lips."
    "She really does like teasing people, doesn’t she? It must be a bad habit — one she has been unable to indulge in this last century or so."
    show toma closed a
    t "I am able to exist only because of the people who have come before me. Maybe these eyes were a gift from Rose Bradford."
    show emmy frown n
    em "Rose...?"
    show toma normal n
    t "She’s one of my ancestors. Apparently, she was a medium. That’s what Mother says, anyway."
    "Yet, if these eyes are a gift from Rose Bradford, the self-proclaimed ‘white witch’ of Beverly, they haven’t been of much use until now. I’ve certainly never seen a ghost before, despite the number of graveyards I’ve visited."
    "I have, however, always been strangely adept at the art of finding dead bodies, even when buried beneath the earth."
    "Does this mean something? Anything?"
    show toma frown n
    "Maybe the world is crawling with ghosts, thicker than the fog that creeps across the ground, and they simply never wanted to make my humble acquaintance."
    "Perhaps they were hiding from me, sitting amongst the branches of trees, or peeking out from behind the stained glass church windows, whispering amongst themselves."
    "Why would they approach me for help, anyway? I’m only a young girl. Only fourteen."
    show toma closed a
    "But Emmeline did."
    "Was there a reason for that?"
    "Now that I think about it..."
    show toma normal a
    t "The ‘her’ that you said I resembled..."
    show emmy sad n
    em "Oh, yes. Well..."
    show emmy sad2 n
    em "You really do look like Cornelia. It took me quite by surprise. For a few moments, I thought you might really be her... But that was folly, of course."
    show toma normal a
    show emmy ehe n
    em "You are not Cornelia. You are own person. Verity."
    show toma sad a
    t "No... My name isn’t Verity. We both know that. And I don’t know if I am my own person, either."
    "How could I be, given my hastily sewn together name? Toma, a diminutive from Thomas, picked because my real name was stolen two weeks before I was born. Andrews, a last name given to me by my dad, not as a gift, but as an afterthought, like a balled up pair of socks for Christmas."
    
    window hide dissolve
    scene black with dissolve
    nvl show dissolve
    
    nvl clear
    
    nv "My name was defined by men I’ve never met before — a dead grandfather, an absent father."
    nv "They don’t belong to me. Nothing belongs to me."
    nv "Even this name, bestowed upon me by Emmeline, isn’t mine. It’s hers. It’s something she invented."
    nv "What {i}does{/i} belong to me, then...? Who am I, really?"
    nv "At the moment, I am nothing more than a composite of old names, long-lost ancestors — Bradfords and Bowers and Kendalls and Lintons and—"
    
    stop music fadeout 0.5
    
    nv "Wait a minute. Linton?"
    
    nvl clear
    
    nvl hide dissolve
    play ambience "sfx/wind.ogg" fadein 1.5
    scene bg barrow
    show fog_bg
    show toma shock a at left2_t
    show emmy normal n at right2_e
    show emmy_bruises at right2_e
    show fog_fg
    with tear
    window show dissolve
    
    t "Emmeline, can I ask you a question?"
    show emmy frown n
    em "Of course. I welcome any and all questions! I haven’t had much of a chance to converse with others in the last one hundred and fifty years!"
    show toma frown n
    "I swallow. My lips feel cracked and dry, my fingers twitching by my sides."
    show toma normal n
    t "Cornelia’s last name... What was it?"
    show emmy huh n
    em "Why, it was Linton. It has been such a long time since I last saw her, but I would never forget that!"
    show toma shock n
    "Linton, was it?"
    "Cornelia Linton."
    show toma normal n
    show emmy normal n
    "It could just be a coincidence, of course — but I don’t know if I believe in coincidences. Not after everything that has happened to me today."
    "That was the reason why Emmeline approached me to begin with. She thought I was Cornelia Linton. Maybe, in a sense, I am — or, at least, a small part of me."
    show toma shock n
    "And it is, with this sudden realisation, that I feel a light dawn upon me. It is not a real light, that one can see with their own eyes — the sun remains firmly, stubbornly hidden behind the clouds — but it is a ‘light’ nonetheless."
    "It is sudden understanding."
    
    stop ambience fadeout 1.0
    
    window hide dissolve
    play sound "sfx/flash.mp3"
    scene bg lake_cg
    show image "grain" onlayer texture
    with spoopy
    window show dissolve
    
    "A whole wealth of memories, a treasure chest of moments shared by the Linton’s lake, of girlish laughter and raspberry lemonade and kisses that taste of carbonation, that I should have no knowledge of."
    
    play sound "sfx/flip.mp3"
    show cg1_sepia
    show image "grain" onlayer texture
    with wipe
    
    "These scenes should be sepia-tainted, like old photographs found in the back of a charity store, from years gone well and truly by."
    "At any rate, I’ve never been kissed before. How would I know what that feels like?"
    "But I can imagine it."
    
    play sound "sfx/flip.mp3"
    show cg2_sepia
    show image "grain" onlayer texture
    with wipe
    
    "In fact, I don’t need to imagine it."
    "I don’t need to imagine it, because it really did happen — not the current me, standing here right now, but to one of my relatives, in another time, in a place not so very far away."
    
    window hide dissolve

    hide image "grain" onlayer texture
    scene bg barrow
    show fog_bg
    show toma shock a at left2_t
    show emmy shock n at right2_e
    show emmy_bruises at right2_e
    show fog_fg
    with spoopy
    
    window show dissolve
    
    em "C-Cornelia...?"
    "Emmeline stares at me —  or is it really ‘me’? — with wide eyes, lashes trembling, hardly daring to believe."
    show toma normal n
    "I can’t entirely believe it, either."
    
    play sound "sfx/beat.mp3" fadein 0.5
    
    "My body is still mine, yet at the same time, it is not. I can sense another presence residing inside me, blown in by the cold autumn breeze. It lingers, hazy and ephemeral, shy to make itself known, yet desperate to speak nevertheless."
    "I feel my heart pounding, but the sensation is strangely unfamiliar. My fingers tremble — or are they hers’? I open my mouth to speak, and another person’s voice comes out."
    
    stop sound fadeout 1.0
    play music "music/lazy afternoon.mp3" fadein 1.8
    
    show toma frown a
    tw "E-Emmy? Emmy, is it really you?"
    show emmy shocksad2 n
    em "C-Cornelia! You, I..."
    "Emmeline presses a hand against her mouth, as though trying to stifle a gasp of disbelief she cannot rightly. How can a girl who is a ghost breathe? The air was choked out of her lungs a long time ago. "
    "And yet, more than one hundred years later, Emmeline now has a new reason to be breathless."
    show emmy sad2 n
    em "I thought... I-I thought you had already passed on. E-Even after you died, I was never able to find you. A-At any rate, your body wasn’t even buried here!"
    show toma normal n
    "I shake my head — or maybe she does. I can’t tell."
    c "No, I wasn’t. I was buried in Wiltshire. That’s where I died, after all. I was seventy-three."
    show emmy sad n
    em "And you... You died peacefully?"
    show toma sad n
    c "Mm. I’m not a ghost. I had no regrets, so I had no reason to come back."
    show emmy shocksad2 n
    em "And yet, right now, you... You..."
    show toma ehe n
    c "Yes, well, um... This was rather unexpected, to tell you the truth."
    "Cornelia turns my body this way and that and inspects it, patting down the skirt of my school uniform and running a hand through my hair."
    show toma normal n
    c "I had been resting peacefully, minding my own business, when — all of a sudden — I found myself here, inside this body. It must have been years since I looked so young. I must apologise to the young girl whose body I have hijacked, though. It is awfully rude, and it wasn’t intentional."
    show emmy smile n
    em "Don’t worry about it, Cornelia. I’m sure Verity won’t mind!"
    show toma skeptical a
    c "Verity? That’s strange. I did not think that was her name..."
    show toma normal n
    c "At any rate, I must thank Miss Verity for her kindness. Sharing one’s identity with somebody else is quite a gesture."
    "It might be to other people, but it isn’t to me — not in particular."
    "Though being unable to speak with my own voice, or move my own limbs, is somewhat disconcerting, I know full well what it feels like to share my identity with another’s. I’ve been living my whole in Amelia Miller’s shadow. Compared to that, a little light possession is nothing."
    show toma poutblush n
    show emmy normal n
    c "T-This outfit is hardly appropriate, though."
    "Cornelia flushes, tugging at the hem of my school skirt."
    c "There is rather too much leg on display, a-and what about the wind? I-I’m surprised the girls of today don’t all catch their deaths of cold!"
    show emmy smirk a
    em "Ehehe~ You sound like a crotchety old lady, Cornelia."
    show toma shockblush a
    c "I am an old lady, and you are, too! S-Stop trying to act all cute!"
    "Emmeline only giggles, peering up at Cornelia with that familiar, mischievous grin."
    "It’s the exact same grin she wore one hundred and fifty years hence, during the lazy summer days by the lake, when she would press kisses against Cornelia’s lips and recite snatches of misremembered poetry to her."
    show emmy wink a
    em "Aw, but you still blush like a fair maiden, Cornelia! You didn’t change at all!"
    show toma poutblush a
    c "And neither did you, Emmy, though I hoped that you might! That attitude of yours was always so unseemly. Mother agreed."
    show emmy pout n
    em "Beatrice Linton wouldn’t know what fun was if it smacked her across the face."
    show toma angryblush n
    c "M-My mother was a very commendable person! She may have been a little strict, but she was not without her good points. She was awfully upset when she heard what had happened to you, Emmy."
    show emmy sad2 n
    em "Yes... What happened to poor little Emmy."
    "Emmeline sighs, the humour gone from her voice. Her eyes are downcast, now, her face wan and pale."
    show emmy frown n
    em "And you, Cornelia... Did you miss me, too?"
    show toma sad a
    c "Do you really need to ask that question?"
    show emmy sad n
    em "I just want to make sure. I realise that you cried a good deal, and that upset me, but... I don’t know. I wanted you to move on and be happy, I really, truly, did, but... At the same time, I was also scared... and jealous, too."
    show emmy sad2 n
    em "You really were my first love, Cornelia. Given I died so young, I suppose you were my last love, too, and the loves that could possibly have come in-between."
    show emmy shocksad2 n
    em "I just don’t want you to have replaced me with somebody else, that’s all! Contemplating it hurts so deeply, I can hardly stand the thought...!"
    show toma sad n
    c "Emmy..."
    "Emmeline’s shoulders are shaking, and though her eyes are devoid of tears — perhaps, being a ghost, crying is a luxury not afforded to her — I am sure she would be weeping if she could."
    "She looks so fragile, a single push might shatter every single bone in her body."
    "Is that why she avoided Cornelia so stringently, even though she wanted nothing more than to see how she was? Was it because she was afraid?"
    "She can’t run away now, though. Not anymore."
    "Even over one hundred years, the truth has a way of finding us eventually. It seems not even death can release us from the burden that reality imposes."
    "Cornelia takes a few steps forwards, slow and stumbling in her unfamiliar body. When she finally reaches Emmeline, she links their hands, and squeezes gently."
    show emmy ehe n
    em "Ehehe..."
    "Emmeline giggles, wiping stray tears that never had a chance to fall from the corners of her eyes."
    em "Well, this is certainly new. You would never have been so bold in the past, Cornelia."
    show toma closed a
    c "Perhaps not, but I have grown up. I lived a long life."
    show emmy frown a
    em "Seventy-three years, was it?"
    show toma normal a
    c "That is correct."
    show emmy sad n
    em "Seventy-three years... I-It is an awfully long time to remain obsessed with a skinny young girl who snuck kisses from you in the summer, is it not?"
    show toma frown a
    c "Indeed. It is an awfully long time. And yet, despite that... I was never able to forget you, Emmy. It would be quite impossible, even if I wanted to."
    show emmy shock n
    em "C-Cornelia?"
    
    stop music fadeout 0.5
    
    "Cornelia bows her head, perhaps in an attempt to hide her threatening blush. Of course, it does no good. She always used to blush around Emmeline, and that hasn’t changed, even after more than a century."
    
    play music "music/sad.mp3" fadein 1.0
    
    window hide dissolve
    scene bg white with tear
    show cg6 with wipe:
        size (1280, 720) crop (220, 260, 640, 360)
        linear 15.0 crop (340, 80, 640, 360)
        
    window show dissolve
    
    c "I got married when I was eighteen. It was a match my mother arranged. She has always been so officious, so organised, so practical. I wonder why your father did not ask her for advice during the stock market crash. She could have helped."
    em "I think he would have felt too embarrassed. It was all Grandmother Patience’s fault. By all accounts, she was not a particularly nice woman."
    c "That really is sad. It could all have been avoided so easily..."
    em "That is what I think, too. Such thoughts do not do us much good now, though."
    c "No, I suppose they do not."
    
    hide cg6
    show cg6
    with wipe
    
    em "So, what about your beau?"
    "Emmeline attempts to smile, though it looks forced, slightly strained at the edges."
    em "Was he a good looker, Cornelia? Did he sweep you off your feet, just like a prince from a fairy tale?"
    "Cornelia laughs dryly."
    c "Of course not. He was a match my mother chose for me. Do you think she would pair her dear daughter with a feckless sot like that?"
    em "So he was sensible, was he?"
    c "Very sensible. He was twice my age, and he was already starting to lose his hair — but he was rich, and had land, and could afford to look after me. To my mother, that was the most important thing."
    em "And not your happiness?"
    c "According to my mother, money is the root of all happiness."
    em "I would like to disagree, but..."
    "Emmeline looks down at herself, smiling sadly."
    em "Given money can be blamed for the sorry state of affairs within my own family, perhaps there is a germ of truth to that."
    c "Perhaps. And I was happy with him, in a sense."
    em "You loved him?"
    c "No. I did not love him. He was too old, and we were too dissimilar. We did not have a single thing in common. Fortunately, he was not unkind, and that is more than can be said for some men, I suppose."
    em "Oh. I, um... I’m sorry, Cornelia."
    c "You do not need to be sorry. I may not have been happy, but I was not {i}un{/i}happy. My life was rather comfortable, all things considered."
    em "But you did not forget about me?"
    
    hide cg6
    show cg6:
        size (1280, 720) crop (320, 100, 640, 360)
    with wipe
    
    c "No, I did not. I couldn’t. You... You really did mean the world to me back then, Emmy — and I loved you with all my heart."
    em "Only back then?"
    c "Well, I..."
    
    stop music fadeout 1.0
    
    c "Even now, I still... I still care for you. I never stopped caring."
    
    window hide dissolve
    scene bg white with wipe
    scene bg barrow
    show fog_bg
    show toma ehe n at left2_t
    show emmy smile a at right2_e
    show emmy_bruises at right2_e
    show fog_fg
    with tear
    window show dissolve
    
    play music "music/hikari.mp3" fadein 0.5
    
    em "Oh, Cornelia... If my heart had not been stopped, I am sure it would have skipped a beat!"
    c "A-And my own heart is pounding rather uncomfortably, even though it does not truly belong to me. I-I hope I am not causing this young girl any undue strain..."
    show emmy smile n
    em "Ehehe~ You always did worry too much, Nellie. You used to be so scared that your mother would find out about us! You still let me kiss you, though."
    show toma sad a
    c "Yes. I-I was scared, but I... I am glad for the time we spent together. Had I known it would be cut short prematurely, I would have confessed to you sooner."
    show emmy smirk a
    em "Hey, Cornelia?"
    show toma shock n
    c "Yes? What is it?"
    show emmy wink a
    em "I am afraid I must ask, for curiosity compels me to do so! Was I a better kisser than your husband?"
    show toma shockblush n
    c "Ah, um... W-Well, I..."
    show emmy smirk a
    em "Ehehe~ If you are incapable of answering, it is quite all right. It {i}was{/i} quite some time since we last kissed one another. Perhaps you need me to refresh your memory~"
    show toma ehe a
    c "I, um... I-I do not think I would be... entirely adverse to that..."
    "And, after a brief pause, the two girls lean in closer."
    "Though Emmeline no longer has any air left in her lungs, I swear I can feel her breath ghost against my cheek. I shiver."
    
    stop music fadeout 1.0
    
    window hide dissolve
    scene black with eyeclose
    play sound "sfx/beat.mp3"
    window show dissolve
    
    "My heart pounds — or is it Cornelia’s?"
    "Perhaps it’s both of us."
    
    window hide dissolve
    show cg3 with wipe
    window show dissolve
    
    play music "music/little flower.ogg" fadein 1.5
    
    "Though she has been dead some one hundred and fifty years, Emmeline’s lips are soft and warm, sweet and gentle, and filled with a deep sense of yearning."
    "I wonder how long Emmeline has wanted to kiss Cornelia. How long has she been sleeping in this graveyard like a fairy tale princess, dreaming unfulfilled dreams of a time gone by, when she was young and happy and very much alive?"
    "Maybe she thought her dream would never come true. That was why she consigned herself to dreaming, and did not awake from her sleepy stupor — a ghostly girl isolated from the rest of the world."
    "But now, she has finally managed to make her dream come true."
    "Is there any reason for her to haunt this graveyard further? Surely, all of her regrets have been wiped away, like the spring sunshine melting the winter snow."
    "She may never understand her dad’s motivations for committing such a terrible crime, but I doubt that was the real regret that kept her body tied to this earth."
    "Instead, it was Cornelia."
    "For Emmeline, it was always Cornelia."
    
    window hide dissolve
    scene bg barrow
    show fog_bg
    show toma smileblush a at left2_t
    show emmy smile n at right2_e
    show emmy_bruises at right2_e
    show fog_fg
    with wipe
    window show dissolve
    
    c "Emmy..."
    "Cornelia breaks the kiss, their lips parting with a soft pop, and blinks up at Emmeline with lidded eyes."
    c "You will come back with me this time, won’t you, Emmy? I have been lonely without you."
    show emmy smirk a
    em "What? I would have thought you would have been enjoying the peace and quiet, Nellie! You always did say I was a nuisance."
    show toma sadblush a
    c "You may have bothered me, but I did not mind the attention. Though I enjoy the calm, it can be rather dull at times."
    show emmy smile a
    em "Then I must return with you, without delay! I would never want you to feel like you had been abandoned! That would be far too sad!"
    show toma smileblush a
    c "Y-Yes. I will be waiting. I have encroached upon this girl’s body for far too long, and I should give it back. It would be the proper thing to do."
    show emmy wink a
    em "Ehehe~ You always did care about the proper thing, Nellie."
    show toma poutblush a
    c "E-Evidently, not enough. Not when it comes to you. Mother will be so surprised when she learns..."
    show emmy smirk a
    em "I look forward to seeing the expression on her face! I don’t think I’ve ever seen Beatrice Linton surprised by anything before in my life!"
    show toma ehe a
    c "Yes, well... Let us see how it pans out, shall we?"
    show emmy smile2 n
    em "I would like that more than anything in the world."
    "Cornelia smiles, taking Emmeline’s hand in her own, and squeezes."
    show emmy smile n
    show toma closed a
    c "I will see you on the other side, Emmy. Please, do not tarry. It has already been far too long."
    "And with that, I feel myself gradually regaining control of my body. My fingertips twitch, my eyelids blink, and I inhale the cool autumnal air almost greedily, like a drowning maiden resurfacing from the inky black water."
    
    window hide dissolve
    play sound "sfx/flash.mp3"
    scene bg white with circleirisout
    
    w "My body belongs to me again, and only me. My identity, once subsumed amongst Cornelia’s ego, like a moon orbiting the earth, has finally been restored."
    w "I never realised it until now, but I really do have an identity of my own."
    w "I might be quiet, and I might be shy, and my other classmates might call be weird, but that doesn’t invalidate me as a person. Neither does the fact that Amelia Miller took my name — nor the fact that my dad left me when I was still an embryo in my mum’s womb."
    w "None of that matters. It’s all irrelevant."
    w "It doesn’t change the fact that I exist. I am alive."
    w "I am the product of all my ancestors before me, a whole string of successive relatives with their own stories to tell, which were born from their struggles; frantic attempts to live life, no matter what."
    w "It is their lives that gave me my own, and I should remember to be grateful."
    w "How could I throw my identity away? It may not fit me perfectly, but it’s the only one I have — and if I don’t like it, all I need to do is create another."
    w "I have that power."
    w "Why did I never realise it before, until it was snatched away from me by a restless memory of a girl long-since dead?"
    w "The old saying must be true. You never realise what you have until you lose it."
    
    scene bg barrow
    show fog_bg
    show toma smile a at left2_t
    show emmy smile n at right2_e
    show emmy_bruises at right2_e
    show fog_fg
    with circleirisin
    window show dissolve
    
    em "Verity..."
    show emmy smile2 n
    em "Thank you for helping me. You have no idea how much it means to me. I really am glad that I met you, even though I was never able to learn your name."
    show toma frown n
    t "My name, is it? A name that truly belongs to me..."
    "I straighten my back, inhale a lungful of air, and declare:"
    show toma smile n
    t "My name is Toma Andrews. It’s a pleasure to meet you, Emmeline Burns."
    show emmy shock a
    em "Toma? What a cute name!"
    show toma shockblush n
    t "C-Cute?"
    show emmy smile a
    em "Ehehe, well, maybe I shouldn’t say that. Nellie will get jealous. But it’s a charming title nonetheless. Why did you not wish to share it with me?"
    show toma ehe a
    t "I... I’m not entirely sure. I suppose I was a little embarrassed..."
    show emmy huh a
    em "Embarrassed by your name?"
    show toma normal n
    t "T-That’s right. But, over the past few hours, I think I realised something. I don’t want to be embarrassed by who I am anymore."
    show emmy smile a
    em "Well, maybe I was able to teach you something, too! That may be another one of my dreams~"
    show toma frown n
    t "Your dreams?"
    show emmy smile n
    em "Yes. I did so love English literature, and would have enjoyed being a tutor. That might have been somewhat difficult, given the period I lived in, but it seems times are starting to change!"
    "Emmeline looks down at my school skirt, and I feel myself flushing. Why is my skirt such a point of public interest? It isn’t even that short."
    "If Emmeline and Cornelia are scandalised by this, they should see Emily Hargreaves’ skirt. That would probably knock them unconscious."
    show emmy smile2 a
    em "I hope you have a pleasant life, dear Toma. When the time comes, you will have to tell me all about it! I would very much like to know what you plan on doing with yourself in the future!"
    show toma smile n
    t "D-Don’t worry, I will. I-I’ll go on all kinds of adventures, and I’ll get some stories — real stories — that will really get your blood pumping!"
    show emmy wink a
    em "Ehehe~ I can’t wait~ It seems like the next century is going to be very interesting indeed~"
    "And, with a cheerful giggle, Emmeline Burns’ body slowly begins to disappear from this world."
    
    hide emmy
    hide emmy_bruises
    with tear2
    
    "I watch as she fades away, until she becomes nothing more than an imprint burnt onto my retinas. Then, when I blink, the illusion is broken, and the imprint scatters into the air."
    
    show toma normal n at cent_t with move
    
    "I pinch my arm. It hurts. It guess this wasn’t a dream after all."
    "I really did meet a ghost called Emmeline Burns, and I really did meet my long-lost ancestor, Cornelia Linton."
    "My mum would be so jealous."
    
    window hide dissolve
    scene bg toma op2 with wipe
    
    w "A silly smile rises to my face despite myself, and I can’t help but giggle. I don’t know if my body has ever felt so light before."
    w "I need to keep going forwards, no matter what happens. I should try to be more like Emmeline, who didn’t give up on her dreams even after she died. I could use some willpower like that."
    w "It’s probably because of that strength of will that Cornelia fell in love with her. Who wouldn’t?"
    w "Despite her sad story, Emmeline Burns really is beautiful."
    w "I hope that I, Toma Andrews, a recovering victim of identity theft, can some day be as beautiful as her."
    
    $ persistent.ending = "done"
    
    stop music fadeout 1.5    
    $ renpy.pause(2.0)
    scene bg white with wipe
    
    play music "music/her song.mp3" fadein 1.0
    show credut at right_left with slow_dissolve
    $ renpy.pause(3.8)
    hide credut with wipe
    $ renpy.pause(0.8)
    scene bg desk
    show credit1
    show cred1 at cree
    with wipe
    $ renpy.pause(5.0)
    hide credit1
    hide cred1
    show credit_2
    show cred2 at cree
    with wipe
    $ renpy.pause(5.0)
    hide cred2
    hide credit_2
    show credit__3
    show cred3 at cree
    with wipe
    $ renpy.pause(5.0)
    hide cred3
    hide credit__3
    show credit___4
    show cred4 at cree
    with wipe
    $ renpy.pause(5.0)
    hide cred4
    hide credit___4
    show credit____5
    show cred5 at cree
    with wipe
    $ renpy.pause(5.0)
    scene bg white with wipe
    $ renpy.pause(1.0)
    show thanku at truecenter
    with tear
    $ renpy.pause(6.0)
    hide thanku with dissolve
    $ renpy.pause(1.0)
    stop music fadeout 1.0
    play sound "sfx/fire.mp3"
    scene black with tear2
    stop sound fadeout 0.5
    return

    
label Extra:
    
    stop music fadeout 0.5
    stop sound fadeout 0.5
    play sound "sfx/fire.mp3" fadein 0.4
    scene black
    with tear
    
    $ renpy.pause(0.5)
    scene bg room1
    with wipe
    stop sound fadeout 0.5
    window show dissolve
    
    play music "music/lazy afternoon.mp3" fadein 1.5
    
    "Sunlight streamed in through the open window, illuminating stray particles of dust as they danced through the air. The gilt-edged mirror on Emmeline’s wall shimmered, the surface sparkling like the edge of a cut jewel."
    "Emmeline lay on her bed, stretched out on her stomach, cat-like, kicking her legs idly back and forth in the air."
    "Cornelia sat beside her, arms round her legs, knees under her chin, taking up rather less space than Emmeline was."
    "Cornelia was attempting to read a book, but Emmeline kept tutting and sighing and making such a fuss Cornelia could not help but be distracted."
    
    show emmy3 frown n at left2_e
    show cornelia frown n at right2_c
    with wipeup_slow
    
    c "What are you doing, Emmy?"
    show emmy3 pout n
    em "Oh, I am supposed to be reading this—"
    "Emmeline gestured to a thick volume on poetry lying on the bed before her, hefty enough to knock a man’s teeth out."
    show emmy3 angry n
    em "— But it is so tediously, unspeakably dull, I fear I will go quite mad!"
    show cornelia frown a
    c "Did Miss Warren tell you to read these?"
    show emmy3 frown n
    em "You mean Ellie?"
    show cornelia shock n
    c "You {i}still{/i} call her Ellie?"
    show emmy3 pout n
    em "I can call her what I please. She is under the employment of my father, and should therefore accept whatever name I see fit to give her."
    show cornelia frown a
    "Cornelia tutted in a manner that was eerily reminiscent of her mother, and set her book to one side."
    c "You, my dear Emmeline, are quite the piece of work. I feel terribly sorry for Miss Warren."
    show emmy3 angry2 n
    em "Do not feel sorry for her, feel sorry for {i}me{/i}! {i}I{/i} am the one who has been tasked to read this drivel, though it is so boring I would rather drive a rusty spike through my head!"
    show cornelia sad n
    "Cornelia shifted slightly on the bed, squeamish, and held one hand to her chest. Cornelia’s complexion was always pale, yet it looked even paler now, like a cadaver’s."
    c "Must you be so gruesome?"
    show emmy3 huh a
    em "I cannot help myself. The gothic is very vogue right now!"
    show cornelia frown n
    c "I believe that was back in in the late 1790s. You’re half a century too late to engage in this particular fashion trend, Emmy."
    show emmy3 angry n
    em "Well, I wish I was reading Radcliffe rather than this nonsense! Why should I care about a leech-gatherer, of all people?"
    em  "The very notion that some people are so poor they must gather leeches to making a living is depressing enough, without reflecting upon it in verse form!"
    show cornelia normal n
    c "Aah."
    "Cornelia nodded, realisation dawning."
    c "Wordsworth, is it?"
    show emmy3 angry2 n
    em "Wordsworth indeed, and he uses rather too many words! I cannot understand why Ellie — nay, why all of England — is so besotted with him! I wandered lonely as a cloud, indeed!"
    show cornelia frown n
    c "I do not understand why you dislike him so. I thought you liked poetry, Emmy."
    show emmy3 pout n
    em "I {i}do{/i} like poetry, but this is not the sort of poetry I like!"
    show cornelia frown a
    c "Could you not try to focus on the elements of his poetry you enjoy, rather than lingering on those which you despise?"
    show emmy3 angry2 n
    em "There is nothing about his poetry I enjoy, Nellie! I cannot stand all the moralising about poor people! I wonder how often our genial friend Mr. Wordsworth mingled with leech-gatherers and country pastors. Ha!"
    play sound "sfx/thud.mp3"
    "Emmeline snorted, in a manner that was not entirely dissimilar to a horse, and slammed her collected works of William Wordsworth shut. She slammed it with such force she very nearly sliced off her fingers, and was only able to withdraw her vulnerable digits at the very last second."
    show emmy3 frown n
    em "I cannot be doing with all of this nonsense — not on such a lovely day. I would much rather experience nature with my own senses, than read it within these dusty pages written by a dusty old man."
    c "But what of Miss Warren? She will scold you if you do not finish your reading."
    show emmy3 angry n
    em "Why should I care what that old spinster thinks? She likes William Wordsworth."
    show cornelia normal n
    c "A lot of people like William Wordsworth. He {i}was{/i} the poet laureate."
    show emmy3 angry2 n
    em "A lot of people are awfully stupid, then!"
    show cornelia frown n
    c "You should not speak ill of him like that, Cornelia. He was a great man, and he died only one year hence. It is rather too soon to insult him. You have not even given his body a chance to cool yet!"
    em "Cold or not, I doubt he will care very much about what I think now, Cornelia. Being dead has a tendency to cease one’s ability to care about such things!"
    show cornelia frown a
    c "Say what you will, but I still do not think it is appropriate."
    show emmy3 smirk a
    em "You do not think anything is appropriate, Nellie! It is a wonder you let me kiss you as I do!"
    "And, with a mischievous giggle, Emmeline sat herself up, and pressed an unexpected kiss against Cornelia’s neck."
    
    play music "music/hikari.mp3" fadein 1.5
    
    show cornelia shock n at bounce
    c "Ah...!"
    "Cornelia twitched, her eyelashes fluttering."
    show cornelia shockblush a
    c "A-Are you a vampire, Emmy?"
    show emmy3 wink a
    em "Perhaps~ I feel I get along far better with Lord Byron’s verses than Mr. Wordsworth’s, at any rate."
    show cornelia sadblush n
    c "If only Wordsworth had written of vampires. Then, you might pay attention."
    show emmy3 smile a
    em "Indeed! It would be more interesting, at any rate. Not as interesting as this, however."
    show cornelia shockblush n
    c "E-Emmy, you will leave bruises if you kiss me like that that!"
    "And yet, despite Cornelia’s feeble protestations, she found herself inclining her head, giving Emmeline further access to the white landscape of skin that made up her neck, her collarbone, and the parts of her chest that were not obscured by the light pink fabric of her dress."
    show emmy3 wink a
    "Emmeline giggled devilishly, pressing yet another kiss against Cornelia’s neck — lower down, this time."
    em "You say that, but I know you do not truly mind~"
    show cornelia sadblush a
    c "I may not mind, but my mother..."
    show emmy3 pout n
    em "Ah, yes. How I could I forget the venerable Mrs. Linton?"
    "Emmeline sighed. Her breath brushed across Cornelia’s skin, damp with saliva, which made the other girl tremble."
    "Cornelia was so slight, Emmeline mused, just like one of the dolls with which she had played as a child. How she wanted to hold Cornelia in her arms, and run her hands through her hair, and kiss her light pink lips..."
    show emmy3 frown n
    em "If your mother caught you with bruises upon your fair neck, Nellie, she may grow rather suspicious."
    show cornelia sadblush n
    c "T-That is what I was thinking..."
    "Though Emmeline was no longer kissing Cornelia, Cornelia’s voice escaped from her lips in soft gasps, lighter than usual, the syllables strung together with stutters. Her heart was pounding far too fast, dyeing her cheeks dark crimson."
    "Inwardly, Cornelia scolded herself. She was just like those silly, swooning girl-women in books penned by men — {i}Pamela{/i}, in particular, sprung to mind — who fell to pieces at the sight of their ‘Lords’."
    "Her mother had not raised her to be like this. Setting the fact that Emmeline was another girl aside — which {i}was{/i} a rather important fact, but one Cornelia did not care to examine – Cornelia knew her own conduct was nothing short of shameful."
    "She could hardly breathe, and her heart felt as though it were beating inside her mouth, and no matter how she tried she could not gather her composure."
    "Emmeline had a most curious effect upon her, much like a drug. Cornelia was little better than a helpless opium addict, hardly able to function without Emmeline’s kisses and caresses."
    "Yet, Cornelia would not have changed her relationship with Emmeline for the world."
    show emmy3 smirk a
    em "Your mother might even suspect you have been engaging in... {i}dalliances{/i}... with that awful Wedgewood boy!"
    show cornelia shockblush n
    c "N-Not Aubrey Wedgewood!"
    show emmy3 wink a
    em "The one and the same~ Unless you thought I was refering to his father?"
    c "E-Emmeline! Mr. Wedgewood is in his fifties! T-The idea is preposterous!"
    show emmy3 smile a
    em "It is not so very preposterous~ We are nearing the age where we ourselves should get married, you know. It is not uncommon for girls our age to marry gentlemen in their twilight years."
    c "I-I would rather not! Not to Aubrey Wedgewood, and certainly not to his father! I would rather die!"
    show emmy3 smile n
    em "Ahaha~ I am so glad to hear you say that! The feeling is quite mutual."
    show cornelia poutblush a
    c "I do not know why you had to ask to begin with. Should my feelings not be obvious?"
    show emmy3 frown n
    em "What do you mean?"
    show cornelia sadblush n
    c "I mean, I... Um... Well."
    
    stop music fadeout 1.0
    
    "Cornelia looked down at her lap, linking her fingers together."
    c "Even though this may make me less of a woman — or, at least, not the woman my parents wish me to be — I cannot bring myself to care."
    
    play music "music/little flower.ogg" fadein 1.5
    
    show cornelia smileblush n
    c "You are the one that I love, Emmy — your virulent hatred of Mr. Wordsworth aside. I do not want to think about getting married to a man. I do not even want to contemplate it."
    show emmy3 shock n
    em "Ah..."
    "Emmeline blinked for a few moments, momentarily surprised by Cornelia’s sudden burst of honesty. This surprise soon wore away, however, to be replaced with a gentle smile."
    show emmy3 smile n
    em "Ehe~ I feel quite the same. I do not even care if I become an old spinster like poor Ellie. I just want to be with you, no matter what."
    
    stop music fadeout 1.0
    
    window hide dissolve
    scene black with wipe
    $ renpy.pause(0.3)
    show text3:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with wipe
    with Pause(2.0)
    scene black with wipe
    $ renpy.pause(0.3)
    scene bg room1
    show emmy3 smile a at left2_e
    show cornelia frown n at right2_c
    with wipe
    
    window show dissolve
    
    play music "music/hikari.mp3" fadein 1.5
    
    c "What are you doing, Emmy?"
    em "Drawing."
    show cornelia frown a
    c "Drawing? I thought you were supposed to be reading more of Mr. Wordsworth’s poetry."
    show emmy3 smile n
    em "I attempted to do so, but it was so very dull! And that was when I had this excellent idea!"
    c "Yes...?"
    "Cornelia’s frown deepened, and she folded her arms. Though she did not want to question Emmeline, she did wonder — as she always did when Emmeline claimed to have struck upon an ‘excellent idea’ — just how ‘excellent’ this idea really was."
    "The last time Emmeline had been bestowed with an ‘excellent’ idea, she had hidden a slug in the pocket of the long-suffering Miss Warren’s overcoat, and the poor woman had shrieked loudly enough upon its discovery to rouse even William Wordsworth from his grave in Grasmere."
    show emmy3 wink a
    em "You see, I simply remembered what you told me earlier, my dear Nellie!"
    show cornelia frown n
    c "And what was that?"
    show emmy3 smile2 a
    "Emmeline smiled brightly, her face radiant with her own self-proclaimed genius, as she set her pencil down on her bed."
    em "You told me to try and find something in Mr. Wordsworth’s poems that I found interesting!"
    show cornelia frown n
    c "And did you?"
    show emmy3 frown n
    em "Of course not. I already told you, I cannot stand his works."
    show emmy3 smile n
    em "There is one thing in this world, however, that I cherish above all else!"
    c "And what is that?"
    show emmy3 wink a
    em "Why, it is beautiful women, of course!"
    show cornelia frown a
    "Cornelia blinked. Just where was this going, exactly? Though she had been close companions with Emmeline throughout the last fourteen (almost fifteen) years, she could not profess to possess full understanding of the inner workings of the other girl’s mind."
    "Perhaps not even Emmeline herself understood such things, given she always seemed to flit from fancy to fancy, restless like a bumblebee in the spring."
    show cornelia frown a
    c "I am well aware that you like beautiful women, but I fail to see how that relates to the esteemed Mr. Wordsworth..."
    show emmy3 smile a
    em "Why, Nellie, you are being awfully dense today! It is simple! Self-explanatory, really!"
    show cornelia normal n
    c "It is?"
    show emmy3 smile2 a
    em "Yes! I see now, in order to truly appreciate Mr. Wordsworth’s works, I should reimagine him — the poet himself — into a form more suited to my desires!"
    em "That is, I should imagine his body of poetry came, not from the hands of a pompous and self-obsessed old git with a big nose, but from a young and beautiful woman! Look, look!"
    
    window hide dissolve
    play sound "sfx/flip.mp3"
    scene bg lillycg with wipe:
        size (1280, 720) crop (0, 500, 1280, 720)
        linear 20.0 crop (0, 0, 1280, 720)
    window show dissolve
    
    "And with that, Emmeline — beatific in her excitement — showed Cornelia one of the quick sketches she had been working on."
    "Cornelia took the sketch, the furrow in her brow deepening as she did so."
    "There, displayed on the white page, was a young and beautiful woman. Her hair fell about her shoulders in a manner any young Romantic would surely have appreciated, and she wore a loose dress that was rather..."
    
    scene bg room1
    show emmy3 smile a at left2_e
    show cornelia frown n at right2_c
    with wipe
    
    c "Why is it so short?"
    show emmy3 smirk a
    em "Oh, Cornelia, it is just a fantasy! Do not trouble yourself too much with the details! And I made more sketches, too!"
    show cornelia shock n
    c "{i}More{/i}?"
    em "Of course! After I re-designed Mr. Wordsworth, I realised that the current landscape of British poetry could use a touch more feminine charm, and I took it upon myself to beautify all of the Romantic poets that our country cares for so greatly!"
    show emmy3 smile a
    em "Apart from Keats, of course. He did not live long enough to warrant a new design, as far as I am concerned."
    show cornelia frown n
    c "Of course."
    "Cornelia flipped through Emmeline’s array of worrying sketches, and as she did so, her left eye began to twitch."
    "Cornelia often wondered this, but now she was unable to keep her comments to herself."
    show cornelia frown a
    c "... Emmeline, you really do have a one track mind."
    
    stop music fadeout 0.5
    window hide dissolve
    
    scene black with wipe
    $ renpy.pause(0.5)
    

    return
