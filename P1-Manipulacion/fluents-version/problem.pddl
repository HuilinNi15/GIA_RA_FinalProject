(define (problem chess_8x8)

(:domain chess)

(:objects
    a1 a2 a3 a4 a5 a6 a7 a8
    b1 b2 b3 b4 b5 b6 b7 b8
    c1 c2 c3 c4 c5 c6 c7 c8
    d1 d2 d3 d4 d5 d6 d7 d8
    e1 e2 e3 e4 e5 e6 e7 e8
    f1 f2 f3 f4 f5 f6 f7 f8
    g1 g2 g3 g4 g5 g6 g7 g8
    h1 h2 h3 h4 h5 h6 h7 h8 - square
    
    peon_blanco1 peon_blanco2 peon_negro1 peon_negro2 - pawn
    rey_blanco rey_negro - king
    caballo_blanco caballo_negro - knight 
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
    
    ; Casillas Vacías Iniciales
    (empty a1) (empty a2) (empty a3) (empty a4)            (empty a6) (empty a7) (empty a8)
    (empty b1)            (empty b3)            (empty b5) (empty b6) (empty b7) (empty b8)
    (empty c1) (empty c2) (empty c3) (empty c4) (empty c5) (empty c6) (empty c7) (empty c8)
    (empty d1) (empty d2) (empty d3) (empty d4) (empty d5) (empty d6) (empty d7) (empty d8)
    (empty e1) (empty e2) (empty e3) (empty e4) (empty e5) (empty e6)            (empty e8)
    (empty f1) (empty f2)                       (empty f5) (empty f6) (empty f7) (empty f8)
    (empty g1) (empty g2)            (empty g4) (empty g5) (empty g6)            (empty g8)
    (empty h1) (empty h2) (empty h3) (empty h4) (empty h5) (empty h6) (empty h7) (empty h8)
    
    ; Turno inicial
    (turnWhite)
    ; (turnBlack)

    (= (movements) 0)

    ; Define coordinates for all casillas
    (= (x a1) 1) (= (y a1) 1)
    (= (x a2) 1) (= (y a2) 2)
    (= (x a3) 1) (= (y a3) 3)
    (= (x a4) 1) (= (y a4) 4)
    (= (x a5) 1) (= (y a5) 5)
    (= (x a6) 1) (= (y a6) 6)
    (= (x a7) 1) (= (y a7) 7)
    (= (x a8) 1) (= (y a8) 8)

    (= (x b1) 2) (= (y b1) 1)
    (= (x b2) 2) (= (y b2) 2)
    (= (x b3) 2) (= (y b3) 3)
    (= (x b4) 2) (= (y b4) 4)
    (= (x b5) 2) (= (y b5) 5)
    (= (x b6) 2) (= (y b6) 6)
    (= (x b7) 2) (= (y b7) 7)
    (= (x b8) 2) (= (y b8) 8)

    (= (x c1) 3) (= (y c1) 1)
    (= (x c2) 3) (= (y c2) 2)
    (= (x c3) 3) (= (y c3) 3)
    (= (x c4) 3) (= (y c4) 4)
    (= (x c5) 3) (= (y c5) 5)
    (= (x c6) 3) (= (y c6) 6)
    (= (x c7) 3) (= (y c7) 7)
    (= (x c8) 3) (= (y c8) 8)

    (= (x d1) 4) (= (y d1) 1)
    (= (x d2) 4) (= (y d2) 2)
    (= (x d3) 4) (= (y d3) 3)
    (= (x d4) 4) (= (y d4) 4)
    (= (x d5) 4) (= (y d5) 5)
    (= (x d6) 4) (= (y d6) 6)
    (= (x d7) 4) (= (y d7) 7)
    (= (x d8) 4) (= (y d8) 8)

    (= (x e1) 5) (= (y e1) 1)
    (= (x e2) 5) (= (y e2) 2)
    (= (x e3) 5) (= (y e3) 3)
    (= (x e4) 5) (= (y e4) 4)
    (= (x e5) 5) (= (y e5) 5)
    (= (x e6) 5) (= (y e6) 6)
    (= (x e7) 5) (= (y e7) 7)
    (= (x e8) 5) (= (y e8) 8)

    (= (x f1) 6) (= (y f1) 1)
    (= (x f2) 6) (= (y f2) 2)
    (= (x f3) 6) (= (y f3) 3)
    (= (x f4) 6) (= (y f4) 4)
    (= (x f5) 6) (= (y f5) 5)
    (= (x f6) 6) (= (y f6) 6)
    (= (x f7) 6) (= (y f7) 7)
    (= (x f8) 6) (= (y f8) 8)

    (= (x g1) 7) (= (y g1) 1)
    (= (x g2) 7) (= (y g2) 2)
    (= (x g3) 7) (= (y g3) 3)
    (= (x g4) 7) (= (y g4) 4)
    (= (x g5) 7) (= (y g5) 5)
    (= (x g6) 7) (= (y g6) 6)
    (= (x g7) 7) (= (y g7) 7)
    (= (x g8) 7) (= (y g8) 8)

    (= (x h1) 8) (= (y h1) 1)
    (= (x h2) 8) (= (y h2) 2)
    (= (x h3) 8) (= (y h3) 3)
    (= (x h4) 8) (= (y h4) 4)
    (= (x h5) 8) (= (y h5) 5)
    (= (x h6) 8) (= (y h6) 6)
    (= (x h7) 8) (= (y h7) 7)
    (= (x h8) 8) (= (y h8) 8)
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

        ; Pos Final Robot
        (on ur3a a1)
    )
)

(:metric minimize 
    (movements)
)
)