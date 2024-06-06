(define (domain chessmanipulation)

(:types peon rey caballo - objects 
	robot location)

(:predicates 
       (at ?rob ?from)
       (handEmpty ?rob)
       (holding ?rob ?obs)
       (in ?obs ?from))

(:action move
:parameters (?rob - robot ?from - location ?to - location)
:precondition (and (at ?rob ?from))
:effect (and (at ?rob ?to) (not (at ?rob ?from)))
)

(:action pick
:parameters (?rob - robot ?obs - objects ?from - location)
:precondition (and (handEmpty ?rob) (in ?obs ?from) (at ?rob ?from))
:effect (and (holding ?rob ?obs) (not (handEmpty ?rob)) ))

(:action place
:parameters (?rob - robot ?obs - objects ?from - location)
:precondition (and (holding ?rob ?obs) (at ?rob ?from))
:effect (and (handEmpty ?rob) (not (holding ?rob ?obs))))

)
