(define (domain chessmanipulation)

(:requirements :adl)

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
       (turno ?color - color)
       (piecePlaced)
)

(:constants
       blancas negras - color
)

(:action move
       :parameters (?p - pieza ?from - casilla ?to - casilla)
       :precondition (in ?p ?from)
       :effect (and (in ?p ?to) (not (in ?p ?from)))
)

(:action pick
       :parameters (?rob - robot ?p - pieza ?c - casilla)
       :precondition (and (handEmpty ?rob) (in ?p ?c))
       :effect (and (holding ?rob ?p) (not (handEmpty ?rob)) (not (in ?p ?c)) (empty ?c))
)

(:action place
       :parameters (?rob - robot ?p - pieza ?c - casilla ?color - color)
       :precondition (and (holding ?rob ?p) (empty ?c)) ; (not (piecePlaced))
       :effect (and (handEmpty ?rob) (not (holding ?rob ?p)) 
              (in ?p ?c) (not (empty ?c)) 
              ; (piecePlaced)
       )
)

; (:action switch-turn
;        :parameters ()
;        :precondition (or (turno blancas) (turno negras) (piecePlaced))
;        :effect (and 
;        (when (turno blancas) (and (not (turno blancas)) (turno negras)))
;        (when (turno negras) (and (not (turno negras)) (turno blancas)))
;        (not (piecePlaced)))
; )
)