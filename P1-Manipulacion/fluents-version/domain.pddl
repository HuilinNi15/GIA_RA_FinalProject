(define (domain chess)

(:requirements :adl :typing :fluents)

(:types 
    pawn king knight - piece
    square color robot
)

(:predicates 
    (handEmpty ?rob - robot)
    (holding ?rob - robot ?p - piece)
    (in ?p - piece ?s - square)
    (empty ?s - square)
    (turnWhite)
    (turnBlack)
    (color ?p - piece ?color - color)
    (on ?rob - robot ?s - square)
    (moved)
)

(:functions
       (x ?s - square)
       (y ?s - square)
       (movements)
)

(:action Move_King
    :parameters (?rob - robot ?p - king ?from - square ?to - square)
    :precondition (and 
                     (or 
                           (and (or (= (- (x ?from) (x ?to)) 1) 
                                    (= (- (x ?to) (x ?from)) 1))
                                (or (= (- (y ?from) (y ?to)) 1) 
                                    (= (- (y ?to) (y ?from)) 1)))
                           (and (or (= (- (x ?from) (x ?to)) 1) 
                                    (= (- (x ?to) (x ?from)) 1))
                                (= (y ?from) (y ?to)))
                           (and (= (x ?from) (x ?to))
                                (or (= (- (y ?from) (y ?to)) 1) 
                                    (= (- (y ?to) (y ?from)) 1)))
                           )
                        (not (= ?from ?to))
                        (holding ?rob ?p)
                        (empty ?to) (on ?rob ?from)
                        (not (moved)))
    :effect (and (on ?rob ?to) 
                 (not (on ?rob ?from))
                 (moved)
                 (increase (movements) 1)
                 )
)

(:action Move_Knight
    :parameters (?rob - robot ?p - knight ?from - square ?to - square)
    :precondition (and (or (and (or (= (- (x ?from) (x ?to)) 2) 
                                    (= (- (x ?to) (x ?from)) 2))
                                (or (= (- (y ?from) (y ?to)) 1) 
                                    (= (- (y ?to) (y ?from)) 1)))
                           (and (or (= (- (x ?from) (x ?to)) 1) 
                                    (= (- (x ?to) (x ?from)) 1))
                                (or (= (- (y ?from) (y ?to)) 2) 
                                    (= (- (y ?to) (y ?from)) 2))))
                       (not (= ?from ?to))
                       (holding ?rob ?p)
                       (empty ?to) (on ?rob ?from)
                       (not (moved)))
    :effect (and (on ?rob ?to) 
                 (not (on ?rob ?from))
                 (moved)
                 (increase (movements) 1)
                 )
)

(:action Move_Pawn
    :parameters (?rob - robot ?p - pawn ?from - square ?to - square)
    :precondition (and (not (= ?from ?to))            ; Different squares
                       (holding ?rob ?p)
                       (empty ?to) 
                       (on ?rob ?from) 
                       (= (x ?from) (x ?to))          ; Same column
                       (or (and (color ?p white) (= (- (y ?to) (y ?from)) 1))   ; Move up for white
                           (and (color ?p black) (= (- (y ?from) (y ?to)) 1)))  ; Move down for black
                       (not (moved)))
    :effect (and (on ?rob ?to) 
                 (not (on ?rob ?from))
                 (moved)
                 (increase (movements) 1)
                 )
)

(:action Move_Empty
    :parameters (?rob - robot ?from - square ?to - square)
    :precondition (and (handEmpty ?rob) (not (= ?from ?to))
                       (on ?rob ?from) (not (on ?rob ?to)))
    :effect (and (on ?rob ?to) (not (on ?rob ?from)) 
                 (moved)
                 (increase (movements) 1)
                 )
)

(:action pick
    :parameters (?rob - robot ?p - piece ?s - square)
    :precondition (and (handEmpty ?rob) (in ?p ?c) 
                       (on ?rob ?c) (moved)
                       (or (and (turnWhite) (color ?p white))
                           (and (turnBlack) (color ?p black))))
    :effect (and (holding ?rob ?p)
                 (not (handEmpty ?rob)) 
                 (not (in ?p ?c)) 
                 (empty ?c) (not (moved))
                 (increase (movements) 1)
                 )
)

(:action place
    :parameters (?rob - robot ?p - piece ?s - square)
    :precondition (and (on ?rob ?c) (empty ?c)
                       (holding ?rob ?p) (moved))
    :effect (and (handEmpty ?rob)
                 (not (holding ?rob ?p)) 
                 (in ?p ?c) (not (empty ?c))
                 (not (moved))
                 (not (turnWhite)) (not (turnBlack))
                 (when (color ?p white) (turnBlack))
                 (when (color ?p black) (turnWhite))
                 (increase (movements) 1)
                 )
)
)