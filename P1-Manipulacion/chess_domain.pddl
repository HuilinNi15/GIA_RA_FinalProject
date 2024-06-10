(define (domain chessmanipulation)

(:requirements :adl)

(:types 
       peon rey caballo - pieza
       casilla color - objects
	robot
       ; location
)

(:predicates 
       (handEmpty ?rob - robot)
       (holding ?rob - robot ?p - pieza)
       (in ?p - pieza ?c - casilla)
       (empty ?c - casilla)
       (turno ?color - color)
)

(:action move
       :parameters (?p - pieza ?from - casilla ?to - casilla)
       :precondition (in ?p ?from)
       :effect (and (in ?p ?to) (not (in ?p ?from)))
)

(:action pick
       :parameters (?rob - robot ?p - pieza ?c - casilla)
       :precondition (and (handEmpty ?rob) (in ?p ?c))
       :effect (and (holding ?rob ?p) (not (handEmpty ?rob)) (empty ?c))
)

(:action place
       :parameters (?rob - robot ?p - pieza ?c - casilla ?color - color)
       :precondition (and (holding ?rob ?p) (empty ?c))
       :effect (and (handEmpty ?rob) (not (holding ?rob ?p)) (in ?p ?c))
              ;(turno ?color)
)

; (:action switch-turn-to-black
;        :parameters ()
;        :precondition (turno blancas)
;        :effect (and (not (turno blancas)) (turno negras))
; )
  
; (:action switch-turn-to-white
;        :parameters ()
;        :precondition (turno negras)
;        :effect (and (not (turno negras)) (turno blancas))
; )
)