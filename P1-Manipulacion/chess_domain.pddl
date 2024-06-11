(define (domain chessmanipulation)

(:requirements :adl :typing)

(:types 
       peon rey caballo - pieza
       casilla color robot
)

(:predicates 
       (handEmpty ?rob - robot)
       (holding ?rob - robot ?p - pieza)
       (in ?p - pieza ?c - casilla)
       (empty ?c - casilla)
       (turnWhite)
       (turnBlack)
       (color ?p - pieza ?color - color)
       (on ?rob - robot ?c - casilla)
       (left ?p1 - casilla ?p2 - casilla)  ;; la de la izquierda va primero tipo (left a1 b1)
       (up ?p1 - casilla ?p2 - casilla)  ;; la de arriba va primero
       (moved)
)

(:action move_Empty
       :parameters (?rob - robot ?from - casilla ?to - casilla)
       :precondition (and 
                     (handEmpty ?rob)
                     (on ?rob ?from)
                     (not (on ?rob ?to)))
       :effect (and (on ?rob ?to) (not (on ?rob ?from)))
)

(:action move_knight
       :parameters (?rob - robot ?p - caballo ?from - casilla ?to - casilla ?c1 - casilla ?c2 - casilla)
       :precondition (and (on ?rob ?from)
                            (holding ?rob ?p)   
                            (not (on ?rob ?to))
                            (empty ?to)
                            (not (moved))
                            ; (or
                            ; (and (up ?from ?c1) (up ?c1 ?c2) (left ?c2 ?to))  ;; up up left
                            ; (and (up ?from ?c1) (up ?c1 ?c2) (left ?to ?c2)) ;; up up right
                            ; (and (left ?c1 ?from) (left ?c2 ?c1) (up ?c2 ?to)) ;; right right up
                            ; (and (left ?c1 ?from) (left ?c2 ?c1) (up ?to ?c2)) ;; right right down
                            ; (and (up ?c1 ?from) (up ?c2 ?c1) (left ?to ?c2)) ;; down down right
                            ; (and (up ?c1 ?from) (up ?c2 ?c1) (left ?c2 ?to)) ;; down down left
                            ; (and (left ?from ?c1) (left ?c1 ?c2) (up ?to ?c2)) ;; left left down
                            ; (and (left ?from ?c1) (left ?c1 ?c2) (up ?c2 ?to)) ;; left left up
                            ; )
                     )
       :effect (and (on ?rob ?to) (not (on ?rob ?from)) (moved))
)

(:action move_pawn
       :parameters (?rob - robot ?p - peon ?from - casilla ?to - casilla)
       :precondition (and (on ?rob ?from) 
                            (holding ?rob ?p)
                            (not (moved))
                            (empty ?to)
                            (not (on ?rob ?to))
                            (or (and (color ?p white) (up ?from ?to)) (and (color ?p black) (up ?to ?from)))                 
                     )
       :effect (and (on ?rob ?to) (not (on ?rob ?from)) (moved))
)

(:action move_king
       :parameters (?rob - robot ?p - rey ?from - casilla ?to - casilla)
       :precondition (and (on ?rob ?from)
                            (holding ?rob ?p)
                            (empty ?to) 
                          (not (on ?rob ?to))
                          (not (moved))
                          (or (left ?from ?to) (left ?to ?from)(up ?from ?to)(up ?to ?from)
                          (and (left ?from ?to) (up ?from ?to))
                          (and (left ?to ?from) (up ?from ?to))
                          (and (left ?from ?to) (up ?to ?from))
                          (and (left ?to ?from) (up ?to ?from))
                          )
                     )
       :effect (and (on ?rob ?to) (not (on ?rob ?from)) (moved))
)




(:action pick
       :parameters (?rob - robot ?p - pieza ?c - casilla)
       :precondition (and (handEmpty ?rob) (in ?p ?c) (on ?rob ?c)
                          (or (and (turnWhite) (color ?p white))
                              (and (turnBlack) (color ?p black))))
       :effect (and (holding ?rob ?p)
              (not (handEmpty ?rob)) 
              (not (in ?p ?c)) 
              (empty ?c)
              (not (moved)))
)

(:action place
       :parameters (?rob - robot ?p - pieza ?c - casilla)
       :precondition (and (on ?rob ?c) (holding ?rob ?p) (empty ?c))
       :effect (and (handEmpty ?rob)
              (not (holding ?rob ?p)) 
              (in ?p ?c) (not (empty ?c))
              (not (turnWhite)) (not (turnBlack))
              (when (color ?p white) (turnBlack))
              (when (color ?p black) (turnWhite))
              (not (moved))
              )
)

)