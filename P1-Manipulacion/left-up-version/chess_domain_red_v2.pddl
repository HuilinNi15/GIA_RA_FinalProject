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
       (colorPieza ?p - pieza ?color - color)
       (on ?rob - robot ?c - casilla)
       (left ?p1 - casilla ?p2 - casilla)  ;; la de la izquierda va primero tipo (left a1 b1)
       (up ?p1 - casilla ?p2 - casilla)  ;; la de arriba va primero
       (moved)
)



(:action move_knight
       :parameters (?rob - robot ?p - caballo ?from - casilla ?to - casilla ?c1 - casilla ?c2 - casilla)
       :precondition (and   (holding ?rob ?p) 
                            (empty ?to) 
                            (on ?rob ?from) 
                            ; (not (on ?rob ?to))
                            (not (moved))
                            (or
                            (and (up ?from ?c1) (up ?c1 ?c2) (left ?c2 ?to))  ;; up up left
                            (and (up ?from ?c1) (up ?c1 ?c2) (left ?to ?c2)) ;; up up right
                            (and (left ?c1 ?from) (left ?c2 ?c1) (up ?c2 ?to)) ;; right right up
                            (and (left ?c1 ?from) (left ?c2 ?c1) (up ?to ?c2)) ;; right right down
                            (and (up ?c1 ?from) (up ?c2 ?c1) (left ?to ?c2)) ;; down down right
                            (and (up ?c1 ?from) (up ?c2 ?c1) (left ?c2 ?to)) ;; down down left
                            (and (left ?from ?c1) (left ?c1 ?c2) (up ?to ?c2)) ;; left left down
                            (and (left ?from ?c1) (left ?c1 ?c2) (up ?c2 ?to)) ;; left left up
                            )
                     )
       :effect (and (on ?rob ?to) (not (on ?rob ?from)) (moved))
)

(:action move_pawn
       :parameters (?rob - robot ?p - peon ?from - casilla ?to - casilla)
       :precondition (and   (holding ?rob ?p)
                            (empty ?to)
                            (not (moved))
                            (on ?rob ?from)
                            ; (not (on ?rob ?to))
                            (or 
                                (and (turnWhite) (up ?from ?to)) 
                                (and (turnBlack) (up ?from ?to))
                            )

                     )
       :effect (and (on ?rob ?to) (not (on ?rob ?from)) (moved))
)



(:action pick
       :parameters (?rob - robot ?p - pieza ?from - casilla ?to - casilla)
       :precondition (and (handEmpty ?rob) (in ?p ?from) (on ?rob ?from) (moved)
                          (or (and (turnWhite) (colorPieza ?p white))
                              (and (turnBlack) (colorPieza ?p black))))
       :effect (and (holding ?rob ?p)
              (not (handEmpty ?rob)) 
              (not (in ?p ?from))
              (empty ?from)
              (on ?rob ?to)
              (not (on ?rob ?from)))
)

(:action move_king
       :parameters (?rob - robot ?p - rey ?from - casilla ?to - casilla ?c1 - casilla)
       :precondition (and (holding ?rob ?p)
                            (empty ?to) 
                          (on ?rob ?from)
                     ;      (not (on ?rob ?to))
                          (not (moved))
                          (or (left ?from ?to) (left ?to ?from) (up ?from ?to)(up ?to ?from)
                          (and (left ?from ?c1) (up ?c1 ?to))
                          (and (left ?c1 ?from) (up ?c1 ?to))
                          (and (left ?from ?c1) (up ?to ?c1))
                          (and (left ?c1 ?from) (up ?to ?c1))
                          )
                     )
       :effect (and (on ?rob ?to) (not (on ?rob ?from)) (moved))
)

(:action place_king
       :parameters (?rob - robot ?p - pieza ?from - casilla ?to - casilla ?c1 - casilla)
       :precondition (and (on ?rob ?from) (holding ?rob ?p) (empty ?to) (moved)
                            (or (left ?from ?to) (left ?to ?from) (up ?from ?to)(up ?to ?from)
                                                (and (left ?from ?c1) (up ?c1 ?to))
                                                (and (left ?c1 ?from) (up ?c1 ?to))
                                                (and (left ?from ?c1) (up ?to ?c1))
                                                (and (left ?c1 ?from) (up ?to ?c1))
                                                )
       )
       :effect (and (handEmpty ?rob)
              (not (holding ?rob ?p)) 
              (in ?p ?to) (not (empty ?to))
              (not (turnWhite)) (not (turnBlack))
              (when (colorPieza ?p white) (turnBlack))
              (when (colorPieza ?p black) (turnWhite))
              (not (moved))
              )
)



)