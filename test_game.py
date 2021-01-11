import chess
import chess.pgn
import chess.engine

engine_w = chess.engine.SimpleEngine.popen_uci("./uci.py")
engine_b = chess.engine.SimpleEngine.popen_uci("./../sunfish-nnue-2/uci.py")

n = 50

for i in range(1, n):
    game = chess.pgn.Game()
    game.headers["Event"] = "Sunfish NNUE Self-play"
    node = game
    board = chess.Board()
    while not board.is_game_over():
        result = engine_w.play(board, chess.engine.Limit(time=100))
        node = node.add_variation(result.move)
        board.push(result.move)
        result = engine_b.play(board, chess.engine.Limit(time=100))
        node = node.add_variation(result.move)
        board.push(result.move)

    print(game)
    i += 1
engine_w.quit()
engine_b.quit()