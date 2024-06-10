(define (problem chess)

(:domain chessmanipulation)

(:objects
    a1 a2 a3 a4 a5 a6 a7 a8
    b1 b2 b3 b4 b5 b6 b7 b8
    c1 c2 c3 c4 c5 c6 c7 c8
    d1 d2 d3 d4 d5 d6 d7 d8
    e1 e2 e3 e4 e5 e6 e7 e8
    f1 f2 f3 f4 f5 f6 f7 f8
    g1 g2 g3 g4 g5 g6 g7 g8
    h1 h2 h3 h4 h5 h6 h7 h8 - square

    ; blancas negras - color
    
    pos11 pos12 pos21 pos22 pos31 pos32 posR - location
    peon1 - peon
    rey1 - rey
    caballo1 - caballo
    ur3a - robot
)

(:init
    ; Pos Inicial

    (at ur3a posR)
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
