# tiny-chess-01

Compact chess engine in a single Python file (4,077 bytes, stdlib only).

- Board as a dict, FEN parsing, full legal move generation (castling,
  en passant, promotion to queen)
- Material plus pawn-advance evaluation
- Alpha-beta search with quiescence (captures only at depth 0) and
  iterative deepening within a 10,000 node budget
- Speaks the kit env protocol: POST /game and /move, 10 s per move

Verified: perft(1)=20, perft(2)=400, perft(3)=8902 from the start position.
