(define (problem chess)

(:domain chessmanipulation)

(:objects
    pos11 pos12 pos21 pos22 pos31 pos32 posR - location
    peon1 - peon
    rey1 - rey
    caballo1 - caballo
    ur3a - robot
)

(:init
    (at robot posR)
    (in peon1 pos11)
    (in rey1 pos21)
    (in caballo1 pos31)
    (handEmpty ur3a)
    (not (dummyCalled ur3a d1 d2))
)

(:goal
    (and (in peon1 pos12)
         (in rey1 pos22)
         (in caballo1 pos32))
)
)
