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
    
    peon_blanco1 peon_blanco2 rey_blanco caballo_blanco - pieza
    peon_negro1 peon_negro2 rey_negro caballo_negro - pieza 
    ur3a - robot
    
    white black - color
)

(:init

    ; Pos Inicial Robot 
    (on ur3a a1)

    ; Pos Inicial Blancas
    (in peon_blanco1 f4)
    (in peon_blanco2 g3)
    (in rey_blanco b2)
    (in caballo_blanco f3)

    (color peon_blanco1 white)
    (color peon_blanco2 white)
    (color rey_blanco white)
    (color caballo_blanco white)

    ; Pos Inicial Negras
    (in peon_negro1 a5)
    (in peon_negro2 b4)
    (in rey_negro g7)
    (in caballo_negro e7)

    (color peon_negro1 black)
    (color peon_negro2 black)
    (color rey_negro black)
    (color caballo_negro black)
    
    ;; Casillas Vacías Iniciales
    (empty a1) (empty a2) (empty a3) (empty a4) (empty a6) (empty a7) (empty a8)
    (empty b1) (empty b3) (empty b5) (empty b6) (empty b7) (empty b8)
    (empty c1) (empty c2) (empty c3) (empty c4) (empty c5) (empty c6) (empty c7) (empty c8)
    (empty d1) (empty d2) (empty d3) (empty d4) (empty d5) (empty d6) (empty d7) (empty d8)
    (empty e1) (empty e2) (empty e3) (empty e4) (empty e5) (empty e6) (empty e8)
    (empty f1) (empty f2) (empty f5) (empty f6) (empty f7) (empty f8)
    (empty g1) (empty g2) (empty g4) (empty g5) (empty g6) (empty g8)
    (empty h1) (empty h2) (empty h3) (empty h4) (empty h5) (empty h6) (empty h7) (empty h8)
    
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
