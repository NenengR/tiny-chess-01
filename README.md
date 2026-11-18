[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/NenengR/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/NenengR/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

# tiny-chess-01

Compact chess engine in a single Python file (4,083 bytes, stdlib only, plain code). Built for the [make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01): build the strongest chess engine in 4 KB of Python, $500 in USDC.

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

Run: `MAKEFUN_ENV_URL=<env url> python3 main.py`

Verified: perft(1)=20, perft(2)=400, perft(3)=8902 from the start position;
Kiwipete 48/2039/97862, en-passant position 14/191/2812. Test games at
10,000 nodes/move: 0 wins / 4 draws / 0 losses vs the previous engine,
4 wins / 0 draws / 0 losses vs a greedy capturer, no crashes, no illegal
moves. Average 0.9 s per move.
