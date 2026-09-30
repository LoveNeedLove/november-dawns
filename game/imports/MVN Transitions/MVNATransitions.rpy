# Few notes for the below transforms!
# I overshoot the progress here to make sure the transition completely clears before we shift away.
# This can mess with how long it feels like the transition is happening, so be aware.
# I like to make the new_widget's softness to be lower than the old one. If they're close to the same
# or if the softness is higher on the new widget, you can expose some transparency mid-transition.

# If you need some of the included map file locations quickly, scroll down to see the massive
# list of defines!

transform ShineDissolve(duration=3.0, *, new_widget=None, old_widget=None, shape=Image("/MVN Transitions/maps/FateBlinds/MVNFateBlinds1.png")):

    delay duration
    events False
    mesh True

    contains:
        old_widget
        mesh True
        shader 'MakeVisualNovels.SoftDissolveHide'
        u_map shape
        u_progress 0.0
        u_softness 0.15
        linear duration u_progress 1.25

    contains:
        new_widget
        events True
        mesh True
        shader 'MakeVisualNovels.SoftDissolveShow'
        u_map shape
        u_progress 0.0
        u_softness 0.10
        linear duration u_progress 1.25

transform BurnDissolve(duration=3.0, *, new_widget=None, old_widget=None, shape=Image("/MVN Transitions/maps/Spiral/MVNSpiral07.png")):
    delay duration
    events False
    mesh True

    contains:
        old_widget
        mesh True
        shader 'MakeVisualNovels.BurnDissolveHide'
        u_map shape
        u_progress 0.0
        u_softness 0.15
        u_low_color (0.08, 0.02, 0.02)
        u_mid_color (1.0, 0.9, 0.4)
        u_high_color (0.8,0.2,0.0)
        u_max_color (1.0, 0.3, 0.0)
        linear duration u_progress 1.25 

    contains:
        new_widget
        events True
        mesh True
        shader 'MakeVisualNovels.BurnDissolveShow'
        u_map shape
        u_progress 0.0
        u_softness 0.10
        u_low_color (0.08, 0.02, 0.02)
        u_mid_color (1.0, 0.9, 0.4)
        u_high_color (0.8,0.2,0.0)
        u_max_color (1.0, 0.3, 0.0)
        linear duration u_progress 1.25

transform VividDissolve(duration=3.0, *, new_widget=None, old_widget=None, shape=Image("/MVN Transitions/maps/Spiral/MVNSpiral07.png")):
    delay duration
    events False
    mesh True

    contains:
        old_widget
        mesh True
        shader 'MakeVisualNovels.BurnDissolveHide'
        u_map shape
        u_progress 0.0
        u_softness 0.15
        u_low_color (1.0,0.0,0.0)
        u_mid_color (0.0,1.0, 0.0)
        u_high_color (0.0,0.3,1.0)
        u_max_color (1.0,0.3,0.5)
        linear duration u_progress 1.25 

    contains:
        new_widget
        events True
        mesh True
        shader 'MakeVisualNovels.BurnDissolveShow'
        u_map shape
        u_progress 0.0
        u_softness 0.10
        u_low_color (1.0,0.0,0.0)
        u_mid_color (0.0,1.0, 0.0)
        u_high_color (0.0,0.3,1.0)
        u_max_color (1.0,0.3,0.5)
        linear duration u_progress 1.25


## Here there be monsters(ous amount of defines)
## You can browse this list.  The "MVN Transitions" blah blah blah line is the path you can use
## in the u_map parts of the above transitions.


## Abstract
define MVNAbstract01 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract01.png"), 1.0, 4.0)
define MVNAbstract02 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract02.png"), 1.0, 4.0)
define MVNAbstract03 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract03.png"), 1.0, 4.0)
define MVNAbstract04 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract04.png"), 1.0, 4.0)
define MVNAbstract05 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract05.png"), 1.0, 4.0)
define MVNAbstract06 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract06.png"), 1.0, 4.0)
define MVNAbstract07 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract07.png"), 1.0, 4.0)
define MVNAbstract08 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract08.png"), 1.0, 4.0)
define MVNAbstract09 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract09.png"), 1.0, 4.0)
define MVNAbstract10 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract10.png"), 1.0, 4.0)
define MVNAbstract100 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract100.png"), 1.0, 4.0)
define MVNAbstract11 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract11.png"), 1.0, 4.0)
define MVNAbstract12 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract12.png"), 1.0, 4.0)
define MVNAbstract13 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract13.png"), 1.0, 4.0)
define MVNAbstract14 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract14.png"), 1.0, 4.0)
define MVNAbstract15 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract15.png"), 1.0, 4.0)
define MVNAbstract16 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract16.png"), 1.0, 4.0)
define MVNAbstract17 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract17.png"), 1.0, 4.0)
define MVNAbstract18 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract18.png"), 1.0, 4.0)
define MVNAbstract19 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract19.png"), 1.0, 4.0)
define MVNAbstract20 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract20.png"), 1.0, 4.0)
define MVNAbstract21 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract21.png"), 1.0, 4.0)
define MVNAbstract22 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract22.png"), 1.0, 4.0)
define MVNAbstract23 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract23.png"), 1.0, 4.0)
define MVNAbstract24 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract24.png"), 1.0, 4.0)
define MVNAbstract25 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract25.png"), 1.0, 4.0)
define MVNAbstract26 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract26.png"), 1.0, 4.0)
define MVNAbstract27 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract27.png"), 1.0, 4.0)
define MVNAbstract28 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract28.png"), 1.0, 4.0)
define MVNAbstract29 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract29.png"), 1.0, 4.0)
define MVNAbstract30 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract30.png"), 1.0, 4.0)
define MVNAbstract31 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract31.png"), 1.0, 4.0)
define MVNAbstract32 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract32.png"), 1.0, 4.0)
define MVNAbstract33 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract33.png"), 1.0, 4.0)
define MVNAbstract34 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract34.png"), 1.0, 4.0)
define MVNAbstract35 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract35.png"), 1.0, 4.0)
define MVNAbstract36 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract36.png"), 1.0, 4.0)
define MVNAbstract37 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract37.png"), 1.0, 4.0)
define MVNAbstract38 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract38.png"), 1.0, 4.0)
define MVNAbstract39 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract39.png"), 1.0, 4.0)
define MVNAbstract40 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract40.png"), 1.0, 4.0)
define MVNAbstract41 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract41.png"), 1.0, 4.0)
define MVNAbstract42 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract42.png"), 1.0, 4.0)
define MVNAbstract43 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract43.png"), 1.0, 4.0)
define MVNAbstract44 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract44.png"), 1.0, 4.0)
define MVNAbstract45 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract45.png"), 1.0, 4.0)
define MVNAbstract46 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract46.png"), 1.0, 4.0)
define MVNAbstract47 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract47.png"), 1.0, 4.0)
define MVNAbstract48 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract48.png"), 1.0, 4.0)
define MVNAbstract49 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract49.png"), 1.0, 4.0)
define MVNAbstract50 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract50.png"), 1.0, 4.0)
define MVNAbstract51 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract51.png"), 1.0, 4.0)
define MVNAbstract52 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract52.png"), 1.0, 4.0)
define MVNAbstract53 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract53.png"), 1.0, 4.0)
define MVNAbstract54 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract54.png"), 1.0, 4.0)
define MVNAbstract55 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract55.png"), 1.0, 4.0)
define MVNAbstract56 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract56.png"), 1.0, 4.0)
define MVNAbstract57 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract57.png"), 1.0, 4.0)
define MVNAbstract58 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract58.png"), 1.0, 4.0)
define MVNAbstract59 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract59.png"), 1.0, 4.0)
define MVNAbstract60 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract60.png"), 1.0, 4.0)
define MVNAbstract61 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract61.png"), 1.0, 4.0)
define MVNAbstract62 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract62.png"), 1.0, 4.0)
define MVNAbstract63 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract63.png"), 1.0, 4.0)
define MVNAbstract64 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract64.png"), 1.0, 4.0)
define MVNAbstract65 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract65.png"), 1.0, 4.0)
define MVNAbstract66 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract66.png"), 1.0, 4.0)
define MVNAbstract67 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract67.png"), 1.0, 4.0)
define MVNAbstract68 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract68.png"), 1.0, 4.0)
define MVNAbstract69 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract69.png"), 1.0, 4.0)
define MVNAbstract70 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract70.png"), 1.0, 4.0)
define MVNAbstract71 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract71.png"), 1.0, 4.0)
define MVNAbstract72 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract72.png"), 1.0, 4.0)
define MVNAbstract73 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract73.png"), 1.0, 4.0)
define MVNAbstract74 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract74.png"), 1.0, 4.0)
define MVNAbstract75 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract75.png"), 1.0, 4.0)
define MVNAbstract76 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract76.png"), 1.0, 4.0)
define MVNAbstract77 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract77.png"), 1.0, 4.0)
define MVNAbstract78 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract78.png"), 1.0, 4.0)
define MVNAbstract79 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract79.png"), 1.0, 4.0)
define MVNAbstract80 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract80.png"), 1.0, 4.0)
define MVNAbstract81 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract81.png"), 1.0, 4.0)
define MVNAbstract82 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract82.png"), 1.0, 4.0)
define MVNAbstract83 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract83.png"), 1.0, 4.0)
define MVNAbstract84 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract84.png"), 1.0, 4.0)
define MVNAbstract85 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract85.png"), 1.0, 4.0)
define MVNAbstract86 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract86.png"), 1.0, 4.0)
define MVNAbstract87 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract87.png"), 1.0, 4.0)
define MVNAbstract88 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract88.png"), 1.0, 4.0)
define MVNAbstract89 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract89.png"), 1.0, 4.0)
define MVNAbstract90 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract90.png"), 1.0, 4.0)
define MVNAbstract91 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract91.png"), 1.0, 4.0)
define MVNAbstract92 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract92.png"), 1.0, 4.0)
define MVNAbstract93 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract93.png"), 1.0, 4.0)
define MVNAbstract94 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract94.png"), 1.0, 4.0)
define MVNAbstract95 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract95.png"), 1.0, 4.0)
define MVNAbstract96 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract96.png"), 1.0, 4.0)
define MVNAbstract97 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract97.png"), 1.0, 4.0)
define MVNAbstract98 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract98.png"), 1.0, 4.0)
define MVNAbstract99 = ImageDissolve(Image("MVN Transitions/maps/Abstract/MVNAbstract99.png"), 1.0, 4.0)

## Basic
define MVNBasic01 = ImageDissolve(Image("MVN Transitions/maps/Basic/MVNBasic01.png"), 1.0, 4.0)
define MVNBasic02 = ImageDissolve(Image("MVN Transitions/maps/Basic/MVNBasic02.png"), 1.0, 4.0)
define MVNBasic03 = ImageDissolve(Image("MVN Transitions/maps/Basic/MVNBasic03.png"), 1.0, 4.0)
define MVNBasic04 = ImageDissolve(Image("MVN Transitions/maps/Basic/MVNBasic04.png"), 1.0, 4.0)
define MVNBasic05 = ImageDissolve(Image("MVN Transitions/maps/Basic/MVNBasic05.png"), 1.0, 4.0)
define MVNBasic06 = ImageDissolve(Image("MVN Transitions/maps/Basic/MVNBasic06.png"), 1.0, 4.0)
define MVNBasic07 = ImageDissolve(Image("MVN Transitions/maps/Basic/MVNBasic07.png"), 1.0, 4.0)
define MVNBasic08 = ImageDissolve(Image("MVN Transitions/maps/Basic/MVNBasic08.png"), 1.0, 4.0)

## CatPaws
define MVNCatPaws1 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws1.png"), 1.0, 4.0)
define MVNCatPaws10 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws10.png"), 1.0, 4.0)
define MVNCatPaws11 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws11.png"), 1.0, 4.0)
define MVNCatPaws2 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws2.png"), 1.0, 4.0)
define MVNCatPaws3 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws3.png"), 1.0, 4.0)
define MVNCatPaws4 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws4.png"), 1.0, 4.0)
define MVNCatPaws5 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws5.png"), 1.0, 4.0)
define MVNCatPaws6 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws6.png"), 1.0, 4.0)
define MVNCatPaws7 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws7.png"), 1.0, 4.0)
define MVNCatPaws8 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws8.png"), 1.0, 4.0)
define MVNCatPaws9 = ImageDissolve(Image("MVN Transitions/maps/CatPaws/MVNCatPaws9.png"), 1.0, 4.0)

## Circular
define MVNCircular01 = ImageDissolve(Image("MVN Transitions/maps/Circular/MVNCircular01.png"), 1.0, 4.0)
define MVNCircular02 = ImageDissolve(Image("MVN Transitions/maps/Circular/MVNCircular02.png"), 1.0, 4.0)
define MVNCircular03 = ImageDissolve(Image("MVN Transitions/maps/Circular/MVNCircular03.png"), 1.0, 4.0)
define MVNCircular04 = ImageDissolve(Image("MVN Transitions/maps/Circular/MVNCircular04.png"), 1.0, 4.0)
define MVNCircular05 = ImageDissolve(Image("MVN Transitions/maps/Circular/MVNCircular05.png"), 1.0, 4.0)
define MVNCircular06 = ImageDissolve(Image("MVN Transitions/maps/Circular/MVNCircular06.png"), 1.0, 4.0)
define MVNCircular07 = ImageDissolve(Image("MVN Transitions/maps/Circular/MVNCircular07.png"), 1.0, 4.0)
define MVNCircular08 = ImageDissolve(Image("MVN Transitions/maps/Circular/MVNCircular08.png"), 1.0, 4.0)
define MVNCircular09 = ImageDissolve(Image("MVN Transitions/maps/Circular/MVNCircular09.png"), 1.0, 4.0)
define MVNCircular10 = ImageDissolve(Image("MVN Transitions/maps/Circular/MVNCircular10.png"), 1.0, 4.0)

## Corner
define MVNCorner01 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner01.png"), 1.0, 4.0)
define MVNCorner02 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner02.png"), 1.0, 4.0)
define MVNCorner03 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner03.png"), 1.0, 4.0)
define MVNCorner04 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner04.png"), 1.0, 4.0)
define MVNCorner05 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner05.png"), 1.0, 4.0)
define MVNCorner06 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner06.png"), 1.0, 4.0)
define MVNCorner07 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner07.png"), 1.0, 4.0)
define MVNCorner08 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner08.png"), 1.0, 4.0)
define MVNCorner09 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner09.png"), 1.0, 4.0)
define MVNCorner10 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner10.png"), 1.0, 4.0)
define MVNCorner11 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner11.png"), 1.0, 4.0)
define MVNCorner12 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner12.png"), 1.0, 4.0)
define MVNCorner13 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner13.png"), 1.0, 4.0)
define MVNCorner14 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner14.png"), 1.0, 4.0)
define MVNCorner15 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner15.png"), 1.0, 4.0)
define MVNCorner16 = ImageDissolve(Image("MVN Transitions/maps/Corner/MVNCorner16.png"), 1.0, 4.0)

## Cracks
define MVNCracks01 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks01.png"), 1.0, 4.0)
define MVNCracks02 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks02.png"), 1.0, 4.0)
define MVNCracks03 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks03.png"), 1.0, 4.0)
define MVNCracks04 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks04.png"), 1.0, 4.0)
define MVNCracks05 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks05.png"), 1.0, 4.0)
define MVNCracks06 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks06.png"), 1.0, 4.0)
define MVNCracks07 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks07.png"), 1.0, 4.0)
define MVNCracks08 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks08.png"), 1.0, 4.0)
define MVNCracks09 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks09.png"), 1.0, 4.0)
define MVNCracks10 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks10.png"), 1.0, 4.0)
define MVNCracks11 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks11.png"), 1.0, 4.0)
define MVNCracks12 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks12.png"), 1.0, 4.0)
define MVNCracks13 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks13.png"), 1.0, 4.0)
define MVNCracks14 = ImageDissolve(Image("MVN Transitions/maps/Cracks/MVNCracks14.png"), 1.0, 4.0)

## Craters
define MVNCraters01 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters01.png"), 1.0, 4.0)
define MVNCraters02 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters02.png"), 1.0, 4.0)
define MVNCraters03 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters03.png"), 1.0, 4.0)
define MVNCraters04 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters04.png"), 1.0, 4.0)
define MVNCraters05 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters05.png"), 1.0, 4.0)
define MVNCraters06 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters06.png"), 1.0, 4.0)
define MVNCraters07 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters07.png"), 1.0, 4.0)
define MVNCraters08 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters08.png"), 1.0, 4.0)
define MVNCraters09 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters09.png"), 1.0, 4.0)
define MVNCraters10 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters10.png"), 1.0, 4.0)
define MVNCraters11 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters11.png"), 1.0, 4.0)
define MVNCraters12 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters12.png"), 1.0, 4.0)
define MVNCraters13 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters13.png"), 1.0, 4.0)
define MVNCraters14 = ImageDissolve(Image("MVN Transitions/maps/Craters/MVNCraters14.png"), 1.0, 4.0)

## FateBlinds
define MVNFateBlinds1 = ImageDissolve(Image("MVN Transitions/maps/FateBlinds/MVNFateBlinds1.png"), 1.0, 4.0)
define MVNFateBlinds2 = ImageDissolve(Image("MVN Transitions/maps/FateBlinds/MVNFateBlinds2.png"), 1.0, 4.0)

## Gabor
define MVNGabor01 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor01.png"), 1.0, 4.0)
define MVNGabor02 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor02.png"), 1.0, 4.0)
define MVNGabor03 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor03.png"), 1.0, 4.0)
define MVNGabor04 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor04.png"), 1.0, 4.0)
define MVNGabor05 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor05.png"), 1.0, 4.0)
define MVNGabor06 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor06.png"), 1.0, 4.0)
define MVNGabor07 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor07.png"), 1.0, 4.0)
define MVNGabor08 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor08.png"), 1.0, 4.0)
define MVNGabor09 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor09.png"), 1.0, 4.0)
define MVNGabor10 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor10.png"), 1.0, 4.0)
define MVNGabor11 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor11.png"), 1.0, 4.0)
define MVNGabor12 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor12.png"), 1.0, 4.0)
define MVNGabor13 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor13.png"), 1.0, 4.0)
define MVNGabor14 = ImageDissolve(Image("MVN Transitions/maps/Gabor/MVNGabor14.png"), 1.0, 4.0)

## Grainy
define MVNGrainy01 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy01.png"), 1.0, 4.0)
define MVNGrainy02 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy02.png"), 1.0, 4.0)
define MVNGrainy03 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy03.png"), 1.0, 4.0)
define MVNGrainy04 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy04.png"), 1.0, 4.0)
define MVNGrainy05 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy05.png"), 1.0, 4.0)
define MVNGrainy06 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy06.png"), 1.0, 4.0)
define MVNGrainy07 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy07.png"), 1.0, 4.0)
define MVNGrainy08 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy08.png"), 1.0, 4.0)
define MVNGrainy09 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy09.png"), 1.0, 4.0)
define MVNGrainy10 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy10.png"), 1.0, 4.0)
define MVNGrainy11 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy11.png"), 1.0, 4.0)
define MVNGrainy12 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy12.png"), 1.0, 4.0)
define MVNGrainy13 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy13.png"), 1.0, 4.0)
define MVNGrainy14 = ImageDissolve(Image("MVN Transitions/maps/Grainy/MVNGrainy14.png"), 1.0, 4.0)

## Halftone
define MVNHalftone01 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone01.png"), 1.0, 4.0)
define MVNHalftone02 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone02.png"), 1.0, 4.0)
define MVNHalftone03 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone03.png"), 1.0, 4.0)
define MVNHalftone04 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone04.png"), 1.0, 4.0)
define MVNHalftone05 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone05.png"), 1.0, 4.0)
define MVNHalftone06 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone06.png"), 1.0, 4.0)
define MVNHalftone07 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone07.png"), 1.0, 4.0)
define MVNHalftone08 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone08.png"), 1.0, 4.0)
define MVNHalftone09 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone09.png"), 1.0, 4.0)
define MVNHalftone10 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone10.png"), 1.0, 4.0)
define MVNHalftone11 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone11.png"), 1.0, 4.0)
define MVNHalftone12 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone12.png"), 1.0, 4.0)
define MVNHalftone13 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone13.png"), 1.0, 4.0)
define MVNHalftone14 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone14.png"), 1.0, 4.0)
define MVNHalftone15 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone15.png"), 1.0, 4.0)
define MVNHalftone16 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone16.png"), 1.0, 4.0)
define MVNHalftone17 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone17.png"), 1.0, 4.0)
define MVNHalftone18 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone18.png"), 1.0, 4.0)
define MVNHalftone19 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone19.png"), 1.0, 4.0)
define MVNHalftone20 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone20.png"), 1.0, 4.0)
define MVNHalftone21 = ImageDissolve(Image("MVN Transitions/maps/Halftone/MVNHalftone21.png"), 1.0, 4.0)

## Lines
define MVNLines1 = ImageDissolve(Image("MVN Transitions/maps/Lines/MVNLines1.png"), 1.0, 4.0)
define MVNLines2 = ImageDissolve(Image("MVN Transitions/maps/Lines/MVNLines2.png"), 1.0, 4.0)
define MVNLines3 = ImageDissolve(Image("MVN Transitions/maps/Lines/MVNLines3.png"), 1.0, 4.0)
define MVNLines4 = ImageDissolve(Image("MVN Transitions/maps/Lines/MVNLines4.png"), 1.0, 4.0)
define MVNLines5 = ImageDissolve(Image("MVN Transitions/maps/Lines/MVNLines5.png"), 1.0, 4.0)
define MVNLines6 = ImageDissolve(Image("MVN Transitions/maps/Lines/MVNLines6.png"), 1.0, 4.0)

## Manifold
define MVNManifold01 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold01.png"), 1.0, 4.0)
define MVNManifold02 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold02.png"), 1.0, 4.0)
define MVNManifold03 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold03.png"), 1.0, 4.0)
define MVNManifold04 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold04.png"), 1.0, 4.0)
define MVNManifold05 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold05.png"), 1.0, 4.0)
define MVNManifold06 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold06.png"), 1.0, 4.0)
define MVNManifold07 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold07.png"), 1.0, 4.0)
define MVNManifold08 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold08.png"), 1.0, 4.0)
define MVNManifold09 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold09.png"), 1.0, 4.0)
define MVNManifold10 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold10.png"), 1.0, 4.0)
define MVNManifold11 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold11.png"), 1.0, 4.0)
define MVNManifold12 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold12.png"), 1.0, 4.0)
define MVNManifold13 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold13.png"), 1.0, 4.0)
define MVNManifold14 = ImageDissolve(Image("MVN Transitions/maps/Manifold/MVNManifold14.png"), 1.0, 4.0)

## Marble
define MVNMarble01 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble01.png"), 1.0, 4.0)
define MVNMarble02 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble02.png"), 1.0, 4.0)
define MVNMarble03 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble03.png"), 1.0, 4.0)
define MVNMarble04 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble04.png"), 1.0, 4.0)
define MVNMarble05 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble05.png"), 1.0, 4.0)
define MVNMarble06 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble06.png"), 1.0, 4.0)
define MVNMarble07 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble07.png"), 1.0, 4.0)
define MVNMarble08 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble08.png"), 1.0, 4.0)
define MVNMarble09 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble09.png"), 1.0, 4.0)
define MVNMarble10 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble10.png"), 1.0, 4.0)
define MVNMarble11 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble11.png"), 1.0, 4.0)
define MVNMarble12 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble12.png"), 1.0, 4.0)
define MVNMarble13 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble13.png"), 1.0, 4.0)
define MVNMarble14 = ImageDissolve(Image("MVN Transitions/maps/Marble/MVNMarble14.png"), 1.0, 4.0)

## Melt
define MVNMelt01 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt01.png"), 1.0, 4.0)
define MVNMelt02 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt02.png"), 1.0, 4.0)
define MVNMelt03 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt03.png"), 1.0, 4.0)
define MVNMelt04 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt04.png"), 1.0, 4.0)
define MVNMelt05 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt05.png"), 1.0, 4.0)
define MVNMelt06 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt06.png"), 1.0, 4.0)
define MVNMelt07 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt07.png"), 1.0, 4.0)
define MVNMelt08 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt08.png"), 1.0, 4.0)
define MVNMelt09 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt09.png"), 1.0, 4.0)
define MVNMelt10 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt10.png"), 1.0, 4.0)
define MVNMelt11 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt11.png"), 1.0, 4.0)
define MVNMelt12 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt12.png"), 1.0, 4.0)
define MVNMelt13 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt13.png"), 1.0, 4.0)
define MVNMelt14 = ImageDissolve(Image("MVN Transitions/maps/Melt/MVNMelt14.png"), 1.0, 4.0)

## Milky
define MVNMilky01 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky01.png"), 1.0, 4.0)
define MVNMilky02 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky02.png"), 1.0, 4.0)
define MVNMilky03 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky03.png"), 1.0, 4.0)
define MVNMilky04 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky04.png"), 1.0, 4.0)
define MVNMilky05 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky05.png"), 1.0, 4.0)
define MVNMilky06 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky06.png"), 1.0, 4.0)
define MVNMilky07 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky07.png"), 1.0, 4.0)
define MVNMilky08 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky08.png"), 1.0, 4.0)
define MVNMilky09 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky09.png"), 1.0, 4.0)
define MVNMilky10 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky10.png"), 1.0, 4.0)
define MVNMilky11 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky11.png"), 1.0, 4.0)
define MVNMilky12 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky12.png"), 1.0, 4.0)
define MVNMilky13 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky13.png"), 1.0, 4.0)
define MVNMilky14 = ImageDissolve(Image("MVN Transitions/maps/Milky/MVNMilky14.png"), 1.0, 4.0)

## Perlin
define MVNPerlin01 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin01.png"), 1.0, 4.0)
define MVNPerlin02 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin02.png"), 1.0, 4.0)
define MVNPerlin03 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin03.png"), 1.0, 4.0)
define MVNPerlin04 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin04.png"), 1.0, 4.0)
define MVNPerlin05 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin05.png"), 1.0, 4.0)
define MVNPerlin06 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin06.png"), 1.0, 4.0)
define MVNPerlin07 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin07.png"), 1.0, 4.0)
define MVNPerlin08 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin08.png"), 1.0, 4.0)
define MVNPerlin09 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin09.png"), 1.0, 4.0)
define MVNPerlin10 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin10.png"), 1.0, 4.0)
define MVNPerlin11 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin11.png"), 1.0, 4.0)
define MVNPerlin12 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin12.png"), 1.0, 4.0)
define MVNPerlin13 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin13.png"), 1.0, 4.0)
define MVNPerlin14 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin14.png"), 1.0, 4.0)
define MVNPerlin15 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin15.png"), 1.0, 4.0)
define MVNPerlin16 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin16.png"), 1.0, 4.0)
define MVNPerlin17 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin17.png"), 1.0, 4.0)
define MVNPerlin18 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin18.png"), 1.0, 4.0)
define MVNPerlin19 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin19.png"), 1.0, 4.0)
define MVNPerlin20 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin20.png"), 1.0, 4.0)
define MVNPerlin21 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin21.png"), 1.0, 4.0)
define MVNPerlin22 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin22.png"), 1.0, 4.0)
define MVNPerlin23 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin23.png"), 1.0, 4.0)
define MVNPerlin24 = ImageDissolve(Image("MVN Transitions/maps/Perlin/MVNPerlin24.png"), 1.0, 4.0)

## PuppyPaws
define MVNPuppyPaws1 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws1.png"), 1.0, 4.0)
define MVNPuppyPaws10 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws10.png"), 1.0, 4.0)
define MVNPuppyPaws11 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws11.png"), 1.0, 4.0)
define MVNPuppyPaws12 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws12.png"), 1.0, 4.0)
define MVNPuppyPaws13 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws13.png"), 1.0, 4.0)
define MVNPuppyPaws14 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws14.png"), 1.0, 4.0)
define MVNPuppyPaws2 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws2.png"), 1.0, 4.0)
define MVNPuppyPaws3 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws3.png"), 1.0, 4.0)
define MVNPuppyPaws4 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws4.png"), 1.0, 4.0)
define MVNPuppyPaws5 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws5.png"), 1.0, 4.0)
define MVNPuppyPaws6 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws6.png"), 1.0, 4.0)
define MVNPuppyPaws7 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws7.png"), 1.0, 4.0)
define MVNPuppyPaws8 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws8.png"), 1.0, 4.0)
define MVNPuppyPaws9 = ImageDissolve(Image("MVN Transitions/maps/PuppyPaws/MVNPuppyPaws9.png"), 1.0, 4.0)

## Radial
define MVNRadial01 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial01.png"), 1.0, 4.0)
define MVNRadial02 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial02.png"), 1.0, 4.0)
define MVNRadial03 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial03.png"), 1.0, 4.0)
define MVNRadial04 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial04.png"), 1.0, 4.0)
define MVNRadial05 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial05.png"), 1.0, 4.0)
define MVNRadial06 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial06.png"), 1.0, 4.0)
define MVNRadial07 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial07.png"), 1.0, 4.0)
define MVNRadial08 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial08.png"), 1.0, 4.0)
define MVNRadial09 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial09.png"), 1.0, 4.0)
define MVNRadial10 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial10.png"), 1.0, 4.0)
define MVNRadial11 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial11.png"), 1.0, 4.0)
define MVNRadial12 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial12.png"), 1.0, 4.0)
define MVNRadial13 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial13.png"), 1.0, 4.0)
define MVNRadial14 = ImageDissolve(Image("MVN Transitions/maps/Radial/MVNRadial14.png"), 1.0, 4.0)

## Ripple
define MVNRipple01 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple01.png"), 1.0, 4.0)
define MVNRipple02 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple02.png"), 1.0, 4.0)
define MVNRipple03 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple03.png"), 1.0, 4.0)
define MVNRipple04 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple04.png"), 1.0, 4.0)
define MVNRipple05 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple05.png"), 1.0, 4.0)
define MVNRipple06 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple06.png"), 1.0, 4.0)
define MVNRipple07 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple07.png"), 1.0, 4.0)
define MVNRipple08 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple08.png"), 1.0, 4.0)
define MVNRipple09 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple09.png"), 1.0, 4.0)
define MVNRipple10 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple10.png"), 1.0, 4.0)
define MVNRipple11 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple11.png"), 1.0, 4.0)
define MVNRipple12 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple12.png"), 1.0, 4.0)
define MVNRipple13 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple13.png"), 1.0, 4.0)
define MVNRipple14 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple14.png"), 1.0, 4.0)
define MVNRipple15 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple15.png"), 1.0, 4.0)
define MVNRipple16 = ImageDissolve(Image("MVN Transitions/maps/Ripple/MVNRipple16.png"), 1.0, 4.0)

## Shapes
define MVNShapes01 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes01.png"), 1.0, 4.0)
define MVNShapes02 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes02.png"), 1.0, 4.0)
define MVNShapes03 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes03.png"), 1.0, 4.0)
define MVNShapes04 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes04.png"), 1.0, 4.0)
define MVNShapes05 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes05.png"), 1.0, 4.0)
define MVNShapes06 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes06.png"), 1.0, 4.0)
define MVNShapes07 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes07.png"), 1.0, 4.0)
define MVNShapes08 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes08.png"), 1.0, 4.0)
define MVNShapes09 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes09.png"), 1.0, 4.0)
define MVNShapes10 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes10.png"), 1.0, 4.0)
define MVNShapes11 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes11.png"), 1.0, 4.0)
define MVNShapes12 = ImageDissolve(Image("MVN Transitions/maps/Shapes/MVNShapes12.png"), 1.0, 4.0)

## SlashAway
define MVNSlashAway1 = ImageDissolve(Image("MVN Transitions/maps/SlashAway/MVNSlashAway1.png"), 1.0, 4.0)
define MVNSlashAway2 = ImageDissolve(Image("MVN Transitions/maps/SlashAway/MVNSlashAway2.png"), 1.0, 4.0)
define MVNSlashAway3 = ImageDissolve(Image("MVN Transitions/maps/SlashAway/MVNSlashAway3.png"), 1.0, 4.0)
define MVNSlashAway4 = ImageDissolve(Image("MVN Transitions/maps/SlashAway/MVNSlashAway4.png"), 1.0, 4.0)

## Slashtone
define MVNSlashtone01 = ImageDissolve(Image("MVN Transitions/maps/Slashtone/MVNSlashtone01.png"), 1.0, 4.0)
define MVNSlashtone02 = ImageDissolve(Image("MVN Transitions/maps/Slashtone/MVNSlashtone02.png"), 1.0, 4.0)
define MVNSlashtone03 = ImageDissolve(Image("MVN Transitions/maps/Slashtone/MVNSlashtone03.png"), 1.0, 4.0)

## Special
define MVNSpecial01 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial01.png"), 1.0, 4.0)
define MVNSpecial02 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial02.png"), 1.0, 4.0)
define MVNSpecial03 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial03.png"), 1.0, 4.0)
define MVNSpecial10 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial10.png"), 1.0, 4.0)
define MVNSpecial11 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial11.png"), 1.0, 4.0)
define MVNSpecial4 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial4.png"), 1.0, 4.0)
define MVNSpecial5 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial5.png"), 1.0, 4.0)
define MVNSpecial6 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial6.png"), 1.0, 4.0)
define MVNSpecial7 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial7.png"), 1.0, 4.0)
define MVNSpecial8 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial8.png"), 1.0, 4.0)
define MVNSpecial9 = ImageDissolve(Image("MVN Transitions/maps/Special/MVNSpecial9.png"), 1.0, 4.0)

## Spherical
define MVNSpherical01 = ImageDissolve(Image("MVN Transitions/maps/Spherical/MVNSpherical01.png"), 1.0, 4.0)
define MVNSpherical02 = ImageDissolve(Image("MVN Transitions/maps/Spherical/MVNSpherical02.png"), 1.0, 4.0)
define MVNSpherical03 = ImageDissolve(Image("MVN Transitions/maps/Spherical/MVNSpherical03.png"), 1.0, 4.0)
define MVNSpherical04 = ImageDissolve(Image("MVN Transitions/maps/Spherical/MVNSpherical04.png"), 1.0, 4.0)
define MVNSpherical05 = ImageDissolve(Image("MVN Transitions/maps/Spherical/MVNSpherical05.png"), 1.0, 4.0)
define MVNSpherical06 = ImageDissolve(Image("MVN Transitions/maps/Spherical/MVNSpherical06.png"), 1.0, 4.0)

## Spiral
define MVNSpiral01 = ImageDissolve(Image("MVN Transitions/maps/Spiral/MVNSpiral01.png"), 1.0, 4.0)
define MVNSpiral02 = ImageDissolve(Image("MVN Transitions/maps/Spiral/MVNSpiral02.png"), 1.0, 4.0)
define MVNSpiral03 = ImageDissolve(Image("MVN Transitions/maps/Spiral/MVNSpiral03.png"), 1.0, 4.0)
define MVNSpiral04 = ImageDissolve(Image("MVN Transitions/maps/Spiral/MVNSpiral04.png"), 1.0, 4.0)
define MVNSpiral05 = ImageDissolve(Image("MVN Transitions/maps/Spiral/MVNSpiral05.png"), 1.0, 4.0)
define MVNSpiral06 = ImageDissolve(Image("MVN Transitions/maps/Spiral/MVNSpiral06.png"), 1.0, 4.0)
define MVNSpiral07 = ImageDissolve(Image("MVN Transitions/maps/Spiral/MVNSpiral07.png"), 1.0, 4.0)

## Spokes
define MVNSpokes01 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes01.png"), 1.0, 4.0)
define MVNSpokes02 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes02.png"), 1.0, 4.0)
define MVNSpokes03 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes03.png"), 1.0, 4.0)
define MVNSpokes04 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes04.png"), 1.0, 4.0)
define MVNSpokes05 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes05.png"), 1.0, 4.0)
define MVNSpokes06 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes06.png"), 1.0, 4.0)
define MVNSpokes07 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes07.png"), 1.0, 4.0)
define MVNSpokes08 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes08.png"), 1.0, 4.0)
define MVNSpokes09 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes09.png"), 1.0, 4.0)
define MVNSpokes10 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes10.png"), 1.0, 4.0)
define MVNSpokes11 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes11.png"), 1.0, 4.0)
define MVNSpokes12 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes12.png"), 1.0, 4.0)
define MVNSpokes13 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes13.png"), 1.0, 4.0)
define MVNSpokes14 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes14.png"), 1.0, 4.0)
define MVNSpokes15 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes15.png"), 1.0, 4.0)
define MVNSpokes16 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes16.png"), 1.0, 4.0)
define MVNSpokes17 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes17.png"), 1.0, 4.0)
define MVNSpokes18 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes18.png"), 1.0, 4.0)
define MVNSpokes19 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes19.png"), 1.0, 4.0)
define MVNSpokes20 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes20.png"), 1.0, 4.0)
define MVNSpokes21 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes21.png"), 1.0, 4.0)
define MVNSpokes22 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes22.png"), 1.0, 4.0)
define MVNSpokes23 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes23.png"), 1.0, 4.0)
define MVNSpokes24 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes24.png"), 1.0, 4.0)
define MVNSpokes25 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes25.png"), 1.0, 4.0)
define MVNSpokes26 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes26.png"), 1.0, 4.0)
define MVNSpokes27 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes27.png"), 1.0, 4.0)
define MVNSpokes28 = ImageDissolve(Image("MVN Transitions/maps/Spokes/MVNSpokes28.png"), 1.0, 4.0)

## StainedGlass
define MVNStainedGlass01 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass01.png"), 1.0, 4.0)
define MVNStainedGlass02 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass02.png"), 1.0, 4.0)
define MVNStainedGlass03 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass03.png"), 1.0, 4.0)
define MVNStainedGlass04 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass04.png"), 1.0, 4.0)
define MVNStainedGlass05 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass05.png"), 1.0, 4.0)
define MVNStainedGlass06 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass06.png"), 1.0, 4.0)
define MVNStainedGlass07 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass07.png"), 1.0, 4.0)
define MVNStainedGlass08 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass08.png"), 1.0, 4.0)
define MVNStainedGlass09 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass09.png"), 1.0, 4.0)
define MVNStainedGlass10 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass10.png"), 1.0, 4.0)
define MVNStainedGlass11 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass11.png"), 1.0, 4.0)
define MVNStainedGlass12 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass12.png"), 1.0, 4.0)
define MVNStainedGlass13 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass13.png"), 1.0, 4.0)
define MVNStainedGlass14 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass14.png"), 1.0, 4.0)
define MVNStainedGlass15 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass15.png"), 1.0, 4.0)
define MVNStainedGlass16 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass16.png"), 1.0, 4.0)
define MVNStainedGlass17 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass17.png"), 1.0, 4.0)
define MVNStainedGlass18 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass18.png"), 1.0, 4.0)
define MVNStainedGlass19 = ImageDissolve(Image("MVN Transitions/maps/StainedGlass/MVNStainedGlass19.png"), 1.0, 4.0)

## Streak
define MVNStreak01 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak01.png"), 1.0, 4.0)
define MVNStreak02 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak02.png"), 1.0, 4.0)
define MVNStreak03 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak03.png"), 1.0, 4.0)
define MVNStreak04 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak04.png"), 1.0, 4.0)
define MVNStreak05 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak05.png"), 1.0, 4.0)
define MVNStreak06 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak06.png"), 1.0, 4.0)
define MVNStreak07 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak07.png"), 1.0, 4.0)
define MVNStreak08 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak08.png"), 1.0, 4.0)
define MVNStreak09 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak09.png"), 1.0, 4.0)
define MVNStreak10 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak10.png"), 1.0, 4.0)
define MVNStreak11 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak11.png"), 1.0, 4.0)
define MVNStreak12 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak12.png"), 1.0, 4.0)
define MVNStreak13 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak13.png"), 1.0, 4.0)
define MVNStreak14 = ImageDissolve(Image("MVN Transitions/maps/Streak/MVNStreak14.png"), 1.0, 4.0)

## SuperNoise
define MVNSuperNoise01 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise01.png"), 1.0, 4.0)
define MVNSuperNoise02 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise02.png"), 1.0, 4.0)
define MVNSuperNoise03 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise03.png"), 1.0, 4.0)
define MVNSuperNoise04 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise04.png"), 1.0, 4.0)
define MVNSuperNoise05 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise05.png"), 1.0, 4.0)
define MVNSuperNoise06 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise06.png"), 1.0, 4.0)
define MVNSuperNoise07 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise07.png"), 1.0, 4.0)
define MVNSuperNoise08 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise08.png"), 1.0, 4.0)
define MVNSuperNoise09 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise09.png"), 1.0, 4.0)
define MVNSuperNoise10 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise10.png"), 1.0, 4.0)
define MVNSuperNoise11 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise11.png"), 1.0, 4.0)
define MVNSuperNoise12 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise12.png"), 1.0, 4.0)
define MVNSuperNoise13 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise13.png"), 1.0, 4.0)
define MVNSuperNoise14 = ImageDissolve(Image("MVN Transitions/maps/Super Noise/MVNSuperNoise14.png"), 1.0, 4.0)

## SuperPerlin
define MVNSuperPerlin01 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin01.png"), 1.0, 4.0)
define MVNSuperPerlin02 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin02.png"), 1.0, 4.0)
define MVNSuperPerlin03 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin03.png"), 1.0, 4.0)
define MVNSuperPerlin04 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin04.png"), 1.0, 4.0)
define MVNSuperPerlin05 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin05.png"), 1.0, 4.0)
define MVNSuperPerlin06 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin06.png"), 1.0, 4.0)
define MVNSuperPerlin07 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin07.png"), 1.0, 4.0)
define MVNSuperPerlin08 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin08.png"), 1.0, 4.0)
define MVNSuperPerlin09 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin09.png"), 1.0, 4.0)
define MVNSuperPerlin10 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin10.png"), 1.0, 4.0)
define MVNSuperPerlin11 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin11.png"), 1.0, 4.0)
define MVNSuperPerlin12 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin12.png"), 1.0, 4.0)
define MVNSuperPerlin13 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin13.png"), 1.0, 4.0)
define MVNSuperPerlin14 = ImageDissolve(Image("MVN Transitions/maps/Super Perlin/MVNSuperPerlin14.png"), 1.0, 4.0)

## Swirl
define MVNSwirl01 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl01.png"), 1.0, 4.0)
define MVNSwirl02 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl02.png"), 1.0, 4.0)
define MVNSwirl03 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl03.png"), 1.0, 4.0)
define MVNSwirl04 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl04.png"), 1.0, 4.0)
define MVNSwirl05 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl05.png"), 1.0, 4.0)
define MVNSwirl06 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl06.png"), 1.0, 4.0)
define MVNSwirl07 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl07.png"), 1.0, 4.0)
define MVNSwirl08 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl08.png"), 1.0, 4.0)
define MVNSwirl09 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl09.png"), 1.0, 4.0)
define MVNSwirl10 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl10.png"), 1.0, 4.0)
define MVNSwirl11 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl11.png"), 1.0, 4.0)
define MVNSwirl12 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl12.png"), 1.0, 4.0)
define MVNSwirl13 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl13.png"), 1.0, 4.0)
define MVNSwirl14 = ImageDissolve(Image("MVN Transitions/maps/Swirl/MVNSwirl14.png"), 1.0, 4.0)

## Techno
define MVNTechno01 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno01.png"), 1.0, 4.0)
define MVNTechno02 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno02.png"), 1.0, 4.0)
define MVNTechno03 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno03.png"), 1.0, 4.0)
define MVNTechno04 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno04.png"), 1.0, 4.0)
define MVNTechno05 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno05.png"), 1.0, 4.0)
define MVNTechno06 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno06.png"), 1.0, 4.0)
define MVNTechno07 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno07.png"), 1.0, 4.0)
define MVNTechno08 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno08.png"), 1.0, 4.0)
define MVNTechno09 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno09.png"), 1.0, 4.0)
define MVNTechno10 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno10.png"), 1.0, 4.0)
define MVNTechno11 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno11.png"), 1.0, 4.0)
define MVNTechno12 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno12.png"), 1.0, 4.0)
define MVNTechno13 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno13.png"), 1.0, 4.0)
define MVNTechno14 = ImageDissolve(Image("MVN Transitions/maps/Techno/MVNTechno14.png"), 1.0, 4.0)

## Tiled
define MVNTiled01 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled01.png"), 1.0, 4.0)
define MVNTiled02 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled02.png"), 1.0, 4.0)
define MVNTiled03 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled03.png"), 1.0, 4.0)
define MVNTiled04 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled04.png"), 1.0, 4.0)
define MVNTiled05 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled05.png"), 1.0, 4.0)
define MVNTiled06 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled06.png"), 1.0, 4.0)
define MVNTiled07 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled07.png"), 1.0, 4.0)
define MVNTiled08 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled08.png"), 1.0, 4.0)
define MVNTiled09 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled09.png"), 1.0, 4.0)
define MVNTiled10 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled10.png"), 1.0, 4.0)
define MVNTiled11 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled11.png"), 1.0, 4.0)
define MVNTiled12 = ImageDissolve(Image("MVN Transitions/maps/Tiled/MVNTiled12.png"), 1.0, 4.0)

## Turbulence
define MVNTurbulence01 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence01.png"), 1.0, 4.0)
define MVNTurbulence02 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence02.png"), 1.0, 4.0)
define MVNTurbulence03 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence03.png"), 1.0, 4.0)
define MVNTurbulence04 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence04.png"), 1.0, 4.0)
define MVNTurbulence05 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence05.png"), 1.0, 4.0)
define MVNTurbulence06 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence06.png"), 1.0, 4.0)
define MVNTurbulence07 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence07.png"), 1.0, 4.0)
define MVNTurbulence08 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence08.png"), 1.0, 4.0)
define MVNTurbulence09 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence09.png"), 1.0, 4.0)
define MVNTurbulence10 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence10.png"), 1.0, 4.0)
define MVNTurbulence11 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence11.png"), 1.0, 4.0)
define MVNTurbulence12 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence12.png"), 1.0, 4.0)
define MVNTurbulence13 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence13.png"), 1.0, 4.0)
define MVNTurbulence14 = ImageDissolve(Image("MVN Transitions/maps/Turbulence/MVNTurbulence14.png"), 1.0, 4.0)

## Vein
define MVNVein01 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein01.png"), 1.0, 4.0)
define MVNVein02 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein02.png"), 1.0, 4.0)
define MVNVein03 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein03.png"), 1.0, 4.0)
define MVNVein04 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein04.png"), 1.0, 4.0)
define MVNVein05 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein05.png"), 1.0, 4.0)
define MVNVein06 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein06.png"), 1.0, 4.0)
define MVNVein07 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein07.png"), 1.0, 4.0)
define MVNVein08 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein08.png"), 1.0, 4.0)
define MVNVein09 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein09.png"), 1.0, 4.0)
define MVNVein10 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein10.png"), 1.0, 4.0)
define MVNVein11 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein11.png"), 1.0, 4.0)
define MVNVein12 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein12.png"), 1.0, 4.0)
define MVNVein13 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein13.png"), 1.0, 4.0)
define MVNVein14 = ImageDissolve(Image("MVN Transitions/maps/Vein/MVNVein14.png"), 1.0, 4.0)

## Voronoi
define MVNVoronoi01 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi01.png"), 1.0, 4.0)
define MVNVoronoi02 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi02.png"), 1.0, 4.0)
define MVNVoronoi03 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi03.png"), 1.0, 4.0)
define MVNVoronoi04 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi04.png"), 1.0, 4.0)
define MVNVoronoi05 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi05.png"), 1.0, 4.0)
define MVNVoronoi06 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi06.png"), 1.0, 4.0)
define MVNVoronoi07 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi07.png"), 1.0, 4.0)
define MVNVoronoi08 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi08.png"), 1.0, 4.0)
define MVNVoronoi09 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi09.png"), 1.0, 4.0)
define MVNVoronoi10 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi10.png"), 1.0, 4.0)
define MVNVoronoi11 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi11.png"), 1.0, 4.0)
define MVNVoronoi12 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi12.png"), 1.0, 4.0)
define MVNVoronoi13 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi13.png"), 1.0, 4.0)
define MVNVoronoi14 = ImageDissolve(Image("MVN Transitions/maps/Voronoi/MVNVoronoi14.png"), 1.0, 4.0)


