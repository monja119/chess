if target_pos == chess.data[k]['pos'] and target_pos != new_pos:
    # updating position
    chess.data[k]['pos'] = new_pos  # pos
    # updating rectangle
    chess.data[k]['rect'] = pygame.Rect(new_pos[0] - 15, new_pos[1], 100, 72)
    # pushing new data
    new_data = chess.data
    chess = Pieces(new_data)
    # updating moves
    moves += 1
    turn = piece_color[moves % 2]
    break