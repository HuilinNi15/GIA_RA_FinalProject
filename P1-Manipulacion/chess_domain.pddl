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
)

(:action move_Empty
       :parameters (?rob - robot ?from - casilla ?to - casilla)
       :precondition (and (handEmpty ?rob) (on ?rob ?from) (not (on ?rob ?to)))
       :effect (and (on ?rob ?to) (not (on ?rob ?from)))
)

(:action move_NonEmpty
       :parameters (?rob - robot ?p - pieza ?from - casilla ?to - casilla)
       :precondition (and (holding ?rob ?p) (empty ?to) 
                          (on ?rob ?from) (not (on ?rob ?to)))
       :effect (and (on ?rob ?to) (not (on ?rob ?from)))
)

(:action pick
       :parameters (?rob - robot ?p - pieza ?c - casilla)
       :precondition (and (handEmpty ?rob) (in ?p ?c) (on ?rob ?c)
                          (or (and (turnWhite) (color ?p white))
                              (and (turnBlack) (color ?p black))))
       :effect (and (holding ?rob ?p)
              (not (handEmpty ?rob)) 
              (not (in ?p ?c)) 
              (empty ?c))
)

(:action place
       :parameters (?rob - robot ?p - pieza ?c - casilla)
       :precondition (and (on ?rob ?c) (holding ?rob ?p) (empty ?c))
                     ;      (or (and (turnWhite) (color ?p white))
                     ;          (and (turnBlack) (color ?p black))))
       :effect (and (handEmpty ?rob)
              (not (holding ?rob ?p)) 
              (in ?p ?c) (not (empty ?c))
              (not (turnWhite)) (not (turnBlack))
              (when (color ?p white) (turnBlack))
              (when (color ?p black) (turnWhite)))
)
)