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
    h1 h2 h3 h4 h5 h6 h7 h8 - casilla
    
    peon_blanco1 peon_blanco2 peon_negro1 peon_negro2 - peon
    rey_blanco rey_negro - rey 
    caballo_blanco caballo_negro - caballo 
    ur3a - robot
    
    white black - color
)

(:init

    ; Pos Inicial Robot
    (on ur3a a1)
    (handEmpty ur3a)

    ; Pos Inicial Blancas
    (in peon_blanco1 f4)
    (in peon_blanco2 g3)
    (in rey_blanco b2)
    (in caballo_blanco f3)

    (colorPieza peon_blanco1 white)
    (colorPieza peon_blanco2 white)
    (colorPieza rey_blanco white)
    (colorPieza caballo_blanco white)

    ; Pos Inicial Negras
    (in peon_negro1 a5)
    (in peon_negro2 b4)
    (in rey_negro g7)
    (in caballo_negro e7)

    (colorPieza peon_negro1 black)
    (colorPieza peon_negro2 black)
    (colorPieza rey_negro black)
    (colorPieza caballo_negro black)
    
    ;; Casillas Vacías Iniciales
    (empty a1) (empty a2) (empty a3) (empty a4) (empty a6) (empty a7) (empty a8)
    (empty b1) (empty b3) (empty b5) (empty b6) (empty b7) (empty b8)
    (empty c1) (empty c2) (empty c3) (empty c4) (empty c5) (empty c6) (empty c7) (empty c8)
    (empty d1) (empty d2) (empty d3) (empty d4) (empty d5) (empty d6) (empty d7) (empty d8)
    (empty e1) (empty e2) (empty e3) (empty e4) (empty e5) (empty e6) (empty e8)
    (empty f1) (empty f2) (empty f5) (empty f6) (empty f7) (empty f8)
    (empty g1) (empty g2) (empty g4) (empty g5) (empty g6) (empty g8)
    (empty h1) (empty h2) (empty h3) (empty h4) (empty h5) (empty h6) (empty h7) (empty h8)

    ;; Posicion relativa Casillas 

    ;; left
    (left a1 b1) (left b1 c1) (left c1 d1) (left d1 e1) (left e1 f1) (left f1 g1) (left g1 h1)
    (left a2 b2) (left b2 c2) (left c2 d2) (left d2 e2) (left e2 f2) (left f2 g2) (left g2 h2)
    (left a3 b3) (left b3 c3) (left c3 d3) (left d3 e3) (left e3 f3) (left f3 g3) (left g3 h3)
    (left a4 b4) (left b4 c4) (left c4 d4) (left d4 e4) (left e4 f4) (left f4 g4) (left g4 h4)
    (left a5 b5) (left b5 c5) (left c5 d5) (left d5 e5) (left e5 f5) (left f5 g5) (left g5 h5)
    (left a6 b6) (left b6 c6) (left c6 d6) (left d6 e6) (left e6 f6) (left f6 g6) (left g6 h6)
    (left a7 b7) (left b7 c7) (left c7 d7) (left d7 e7) (left e7 f7) (left f7 g7) (left g7 h7)
    (left a8 b8) (left b8 c8) (left c8 d8) (left d8 e8) (left e8 f8) (left f8 g8) (left g8 h8)

    ;; up
    (up a8 a7) (up a7 a6) (up a6 a5) (up a5 a4) (up a4 a3) (up a3 a2) (up a2 a1)
    (up b8 b7) (up b7 b6) (up b6 b5) (up b5 b4) (up b4 b3) (up b3 b2) (up b2 b1)
    (up c8 c7) (up c7 c6) (up c6 c5) (up c5 c4) (up c4 c3) (up c3 c2) (up c2 c1)
    (up d8 d7) (up d7 d6) (up d6 d5) (up d5 d4) (up d4 d3) (up d3 d2) (up d2 d1)
    (up e8 e7) (up e7 e6) (up e6 e5) (up e5 e4) (up e4 e3) (up e3 e2) (up e2 e1)
    (up f8 f7) (up f7 f6) (up f6 f5) (up f5 f4) (up f4 f3) (up f3 f2) (up f2 f1)
    (up g8 g7) (up g7 g6) (up g6 g5) (up g5 g4) (up g4 g3) (up g3 g2) (up g2 g1)
    (up h8 h7) (up h7 h6) (up h6 h5) (up h5 h4) (up h4 h3) (up h3 h2) (up h2 h1)



    ;; Turno inicial
    (turnWhite)
)

(:goal
    (and
        ; Pos Final Blancas
        (in peon_blanco1 f4)
        (in peon_blanco2 g3)
        (in rey_blanco a2) 
        (in caballo_blanco e5)

        ; Pos Final Negras
        (in peon_negro1 a4)
        (in peon_negro2 b4)
        (in rey_negro h6)
        (in caballo_negro e7)
    )
)
)
