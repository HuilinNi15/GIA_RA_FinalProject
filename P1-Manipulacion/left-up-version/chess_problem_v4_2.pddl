(define (problem chess)

(:domain chessmanipulation)

(:objects
    a1 a2 a3 a4
    b1 b2 b3 b4
    c1 c2 c3 c4
    d1 d2 d3 d4 - casilla

    peon_blanco caballo_negro nothing - pieza 
    ur3a - robot
    
    white black - color
)

(:init
    ; Pos Inicial Robot
    (on ur3a a3)
    ;;(handEmpty ur3a)
    (he)
    (nada nothing)

    ; Declarar tipo pieza
    (caballo caballo_negro)
    (peon peon_blanco)

    ; Pos Inicial
    (in caballo_negro b1)
    (in peon_blanco c1)

    (colorPieza peon_blanco white)
    (colorPieza caballo_negro black)

    
    ;; Casillas Vacías Iniciales
    (empty a1) (empty a2) (empty a3) (empty a4)
    (empty b2) (empty b3) (empty b4)
    (empty c2) (empty c3) (empty c4) 
    (empty d1) (empty d2) (empty d3) (empty d4)

    ;; Posicion relativa Casillas 

    ;; left
    (left a1 b1) (left b1 c1) (left c1 d1) 
    (left a2 b2) (left b2 c2) (left c2 d2) 
    (left a3 b3) (left b3 c3) (left c3 d3)
    (left a4 b4) (left b4 c4) (left c4 d4) 

    ;; up
    (up a4 a3) (up a3 a2) (up a2 a1)
    (up b4 b3) (up b3 b2) (up b2 b1)
    (up c4 c3) (up c3 c2) (up c2 c1)
    (up d4 d3) (up d3 d2) (up d2 d1)

    ;; Turno inicial
    (turnWhite)
)

(:goal
    (and
        ; Pos Final Blancas
        (in peon_blanco c2) 
        (in caballo_negro a3)

        (on ur3a d3)
        
    )
)
)
