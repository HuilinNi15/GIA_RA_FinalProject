(define (domain aaa)

(:requirements :adl :typing)

(:types 
       peon rey caballo - pieza
       casilla color - objects
       robot
)

(:predicates 
       (handEmpty ?rob - robot)
       (holding ?rob - robot ?p - pieza)
       (in ?p - pieza ?c - casilla)
       (empty ?c - casilla)
       (turnWhite)
       (turnBlack)
       (color ?p - pieza ?color - color)
)

(:action move
       :parameters (?p - pieza ?from - casilla ?to - casilla ?color - color)
       :precondition (and (in ?p ?from) (color ?p ?color)
                          (or (and (turnWhite) (color ?p white))
                              (and (turnBlack) (color ?p black))))
       :effect (and (in ?p ?to) (not (in ?p ?from))
                    (not (turnWhite)) (not (turnBlack))
                    (when (color ?p white) (turnBlack))
                    (when (color ?p black) (turnWhite)))
)

(:action pick
       :parameters (?rob - robot ?p - pieza ?c - casilla ?color - color)
       :precondition (and (handEmpty ?rob) (in ?p ?c) (color ?p ?color)
                          (or (and (turnWhite) (color ?p white))
                              (and (turnBlack) (color ?p black))))
       :effect (and (holding ?rob ?p) (not (handEmpty ?rob)) (not (in ?p ?c)) (empty ?c))
)

(:action place
       :parameters (?rob - robot ?p - pieza ?c - casilla ?color - color)
       :precondition (and (holding ?rob ?p) (empty ?c) (color ?p ?color)
                          (or (and (turnWhite) (color ?p white))
                              (and (turnBlack) (color ?p black))))
       :effect (and (handEmpty ?rob) (not (holding ?rob ?p)) 
              (in ?p ?c) (not (empty ?c))
              (not (turnWhite)) (not (turnBlack))
              (when (color ?p white) (turnBlack))
              (when (color ?p black) (turnWhite)))
)

)

