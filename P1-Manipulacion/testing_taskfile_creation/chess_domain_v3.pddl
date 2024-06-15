(define (domain chessmanipulation)

(:requirements :adl :typing)

(:types 
       ;;; peon rey caballo - pieza  ;; com no podem unificar per type posem un predicat pel type
    pieza casilla color robot
)

(:predicates 
       (handEmpty ?rob - robot)
       (holding ?rob - robot ?p - pieza)
       (in ?p - pieza ?c - casilla)
       (empty ?c - casilla)
       (turnWhite)
       (turnBlack)
       (colorPieza ?p - pieza ?color - color)
       (on ?rob - robot ?c - casilla)
       (left ?p1 - casilla ?p2 - casilla)  ;; la de la izquierda va primero tipo (left a1 b1)
       (up ?p1 - casilla ?p2 - casilla)  ;; la de arriba va primero
       (moved)
       (caballo ?p - pieza)
       (rey ?p - pieza)
       (peon ?p - pieza)
)

(:action move
        :parameters (?rob - robot ?from - casilla ?to - casilla ?c1 - casilla ?c2 - casilla ?p - pieza)
        :precondition (and (on ?rob ?from)
                          ;; (holding ?rob ?p) (empty ?to)  ;; per move_Empty no es cert 
                          (not (moved))
                            (or
                            (and (caballo ?p) (up ?from ?c1) (up ?c1 ?c2) (left ?c2 ?to))  ;; up up left
                            (and (caballo ?p) (up ?from ?c1) (up ?c1 ?c2) (left ?to ?c2)) ;; up up right
                            (and (caballo ?p) (left ?c1 ?from) (left ?c2 ?c1) (up ?c2 ?to)) ;; right right up
                            (and (caballo ?p) (left ?c1 ?from) (left ?c2 ?c1) (up ?to ?c2)) ;; right right down
                            (and (caballo ?p) (up ?c1 ?from) (up ?c2 ?c1) (left ?to ?c2)) ;; down down right
                            (and (caballo ?p) (up ?c1 ?from) (up ?c2 ?c1) (left ?c2 ?to)) ;; down down left
                            (and (caballo ?p) (left ?from ?c1) (left ?c1 ?c2) (up ?to ?c2)) ;; left left down
                            (and (caballo ?p) (left ?from ?c1) (left ?c1 ?c2) (up ?c2 ?to)) ;; left left up

                            (and (rey ?p) (left ?from ?to))
                            (and (rey ?p) (left ?to ?from))
                            (and (rey ?p) (up ?from ?to))
                            (and (rey ?p) (up ?to ?from))
                            (and (rey ?p) (left ?from ?c1) (up ?c1 ?to))
                            (and (rey ?p) (left ?c1 ?from) (up ?c1 ?to))
                            (and (rey ?p) (left ?from ?c1) (up ?to ?c1))
                            (and (rey ?p) (left ?c1 ?from) (up ?to ?c1))

                            (or 
                                (and (turnWhite) (up ?from ?to) (peon ?p)) 
                                (and (turnBlack) (up ?from ?to) (peon ?p))
                            )
                            )


        )
        :effect (and (on ?rob ?to) (not (on ?rob ?from)) (moved))
)

(:action pick
       :parameters (?rob - robot ?p - pieza ?c - casilla)
       :precondition (and (handEmpty ?rob) (in ?p ?c) (on ?rob ?c) (moved)
                          (or (and (turnWhite) (colorPieza ?p white))
                              (and (turnBlack) (colorPieza ?p black))))
       :effect (and (holding ?rob ?p)
              (not (handEmpty ?rob)) 
              (not (in ?p ?c)) 
              (empty ?c)
              (not (moved)))
)

(:action place
       :parameters (?rob - robot ?p - pieza ?c - casilla)
       :precondition (and (on ?rob ?c) (holding ?rob ?p) (empty ?c) (moved))
       :effect (and (handEmpty ?rob)
              (not (holding ?rob ?p)) 
              (in ?p ?c) (not (empty ?c))
              (not (turnWhite)) (not (turnBlack))
              (when (colorPieza ?p white) (turnBlack))
              (when (colorPieza ?p black) (turnWhite))
              (not (moved))
              )
)

)