# tiny-chess-01

Compact chess engine in a single Python file (4,083 bytes, stdlib only, plain code).

- Board as a dict, FEN parsing, full legal move generation (castling,
  en passant, promotion to queen)
- Evaluation: piece-square tables for all six pieces plus a king endgame
  table, bishop-pair bonus, king pawn-shield in the middlegame, king
  centralisation in the endgame
- Search: iterative deepening alpha-beta, MVV-LVA capture ordering with
  promotion priority, check extensions (max 2 per line), mate scores by
  distance from root, within a 12,000 node budget; no wall clock, no
  randomness, deterministic
- Speaks the kit env protocol: POST /game and /move, 10 s per move

Verified: perft(1)=20, perft(2)=400, perft(3)=8902 from the start position;
Kiwipete 48/2039/97862, en-passant position 14/191/2812. Test games at
10,000 nodes/move: 0 wins / 4 draws / 0 losses vs the previous engine,
4 wins / 0 draws / 0 losses vs a greedy capturer, no crashes, no illegal
moves. Average 0.9 s per move.
