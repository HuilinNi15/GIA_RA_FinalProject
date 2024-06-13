(define (problem chess_4x4)

(:domain chess)

(:objects
    a1 a2 a3 a4 
    b1 b2 b3 b4 
    c1 c2 c3 c4 
    d1 d2 d3 d4 - square
    
    ; peon_blanco1 peon_blanco2 peon_negro1 peon_negro2 - pawn
    ; rey_blanco rey_negro - king
    caballo_blanco caballo_negro - knight 
    ur3a - robot
    
    white black - color
)

(:init
    
    ; Pos Inicial Robot 
    (on ur3a a1)
    (handEmpty ur3a)

    ; Pos Inicial Blancas
    ; (in peon_blanco1 f4)
    ; (in peon_blanco2 g3)
    ; (in rey_blanco d1)
    (in caballo_blanco a1)

    ; (color peon_blanco1 white)
    ; (color peon_blanco2 white)
    ; (color rey_blanco white)
    (color caballo_blanco white)

    ; Pos Inicial Negras
    ; (in peon_negro1 a5)
    ; (in peon_negro2 b4)
    ; (in rey_negro b3)
    (in caballo_negro b3)
    
    ; (color peon_negro1 black)
    ; (color peon_negro2 black)
    ; (color rey_negro black)
    (color caballo_negro black)
    
    ; Initial Empty Squares
               (empty a2) (empty a3) (empty a4) 
    (empty b1) (empty b2)            (empty b4)
    (empty c1) (empty c2) (empty c3) (empty c4) 
    (empty d1) (empty d2) (empty d3) (empty d4) 
    
    ; Who starts
    ; (turnWhite)
    (turnBlack)

    (= (movements) 0)

    ; Define coordinates for all casillas
    (= (x a1) 1) (= (y a1) 1)
    (= (x a2) 1) (= (y a2) 2)
    (= (x a3) 1) (= (y a3) 3)
    (= (x a4) 1) (= (y a4) 4)

    (= (x b1) 2) (= (y b1) 1)
    (= (x b2) 2) (= (y b2) 2)
    (= (x b3) 2) (= (y b3) 3)
    (= (x b4) 2) (= (y b4) 4)

    (= (x c1) 3) (= (y c1) 1)
    (= (x c2) 3) (= (y c2) 2)
    (= (x c3) 3) (= (y c3) 3)
    (= (x c4) 3) (= (y c4) 4)

    (= (x d1) 4) (= (y d1) 1)
    (= (x d2) 4) (= (y d2) 2)
    (= (x d3) 4) (= (y d3) 3)
    (= (x d4) 4) (= (y d4) 4)
)

(:goal
    (and
        ; Pos Final Blancas
        ; (in peon_blanco1 f4)
        ; (in peon_blanco2 g4)
        ; (in rey_blanco d3)
        (in caballo_blanco c4)

        ; Pos Final Negras
        ; (in peon_negro1 a5)
        ; (in peon_negro2 b4)
        ; (in rey_negro a1)
        (in caballo_negro a1)


        ; ; Pos Final Blancas
        ; (in peon_blanco1 f4)
        ; (in peon_blanco2 g3)
        ; (in rey_blanco a2)
        ; (in caballo_blanco e5)

        ; ; Pos Final Negras
        ; (in peon_negro1 a4)
        ; (in peon_negro2 b4)
        ; (in rey_negro h6)
        ; (in caballo_negro e7)

        ; Pos Final Robot
        (on ur3a a1)
    )
)

(:metric minimize
    (movements)
        )
)