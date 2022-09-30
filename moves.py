from pieces import Pieces


class Moves:
    def __init__(self, target_pos, new_pos, name, color, data):
        self.catch_color = None
        self.data = data
        self.name = name
        self.color = color
        self.suicide = False
        self.target_pos = target_pos
        movement = {
            'pawn': 'self.pawn(target_pos, new_pos, color)',
            'round': 'self.round(target_pos, new_pos, color)',
            'knight': 'self.knight(target_pos, new_pos, color)',
            'mad': 'self.mad(target_pos, new_pos, color)',
        }

        # accepting
        self.accept = eval(movement[name])

    def catch(self, new_pos, color):
        for k in range(len(self.data)):
            if self.data[k]['pos'] == new_pos:
                self.catch_color = self.data[k]['src'].split('/')[2]
                self.catch_name = self.data[k]['src'].split('/')[-1].split('.')[0]

                if self.catch_color == self.color:
                    self.suicide = True
                print('{} {} catched by {} {}'.format(self.catch_color, self.catch_name, self.color, self.name))

                return True
                break

    def index(self, new_pos, target_pos):
        index_x = ((new_pos[0] - 15) - (target_pos[0] - 15)) // 100
        index_y = (new_pos[1] - target_pos[1]) // 72

        return (index_x, index_y)

    def blocked(self, new_pos, index):
        # blocked vertical
        blocked_x, blocked_y, blocked_xy = False, False, False
        index_y = index[1]
        index_x = index[0]
        path_y = []
        path_x = []
        if index_y < 0:
            for y in range(abs(index_y)):
                target_y = self.target_pos[1] - (72 * (y + 1))
                path_y.append(target_y)
        elif index_y > 0:
            for y in range(abs(index_y)):
                target_y = self.target_pos[1] + (72 * (y + 1))
                path_y.append(target_y)

        for i in range(len(path_y)):
            for k in range(len(self.data)):
                if (new_pos[0], path_y[i]) == self.data[k]['pos']:
                    blocked_y = True

        # blocked horizontal
        if index_x < 0:
            for x in range(abs(index_x)):
                target_x = self.target_pos[0] - (100 * (x + 1))
                path_x.append(target_x)
        elif index_x > 0:
            for x in range(abs(index_x)):
                target_x = self.target_pos[0] + (100 * (x + 1))
                path_x.append(target_x)

        for i in range(len(path_x)):
            for k in range(len(self.data)):
                if (path_x[i], new_pos[1]) == self.data[k]['pos']:
                    blocked_x = True

        # blocked xy
        if abs(index[0]) == abs(index[1]):
            blocked_xy = False
        else:
            blocked_xy = True
        print(abs(index[0]), abs(index[1]), blocked_xy)

        return  (blocked_x, blocked_y, blocked_xy)

    def pawn(self, target_pos, new_pos, color):
        catch = self.catch(new_pos, color)

        match color:
            # black pawn
            case 'black':
                if target_pos[0] == new_pos[0] and (
                        target_pos[1] - 144 == new_pos[1] or target_pos[1] - 72 == new_pos[1]) \
                        and catch is None:
                    return True
                # catching
                elif (target_pos[0] + 100 == new_pos[0] or target_pos[0] - 100 == new_pos[0]) \
                        and target_pos[1] - 72 == new_pos[1] and catch:
                    return True
            # white pawn
            case 'white':
                if target_pos[0] == new_pos[0] and (
                        target_pos[1] + 144 == new_pos[1] or target_pos[1] + 72 == new_pos[1]) \
                        and catch is None:
                    return True
                elif (target_pos[0] + 100 == new_pos[0] or target_pos[0] - 100 == new_pos[0]) \
                        and target_pos[1] + 72 == new_pos[1] and catch:
                    return True

    # ROUND
    def round(self, target_pos, new_pos, color):
        catch = self.catch(new_pos, color)
        index = self.index(new_pos, target_pos)
        blocked = self.blocked(new_pos, index)

        match color:
            case 'black':
                if ((target_pos[0] == new_pos[0] and (target_pos[1] // 72) in range(8))
                    or target_pos[0] // 100 in range(9) and target_pos[1] == new_pos[1]) \
                        and self.catch_color != 'black' and blocked[1] is False:
                    return True

            case 'white':
                if ((target_pos[0] == new_pos[0] and (target_pos[1] // 72) in range(8))
                    or target_pos[0] // 100 in range(9) and target_pos[1] == new_pos[1]) \
                        and self.catch_color != 'white' and blocked[1] is False:
                    return True

    # KNIGHT
    def knight(self, target_pos, new_pos, color):
        catch = self.catch(new_pos, color)
        # L normal

        if (new_pos[0] + 100 == target_pos[0] or new_pos[0] - 100 == target_pos[0]) \
                and (
                new_pos[1] - 144 == target_pos[1] or new_pos[1] + 144 == target_pos[1]) and self.suicide is not True:
            # passing horizontal

            return True
        # L reversed
        if (new_pos[0] + 200 == target_pos[0] or new_pos[0] - 200 == target_pos[0]) \
                and (new_pos[1] - 72 == target_pos[1] or new_pos[1] + 72 == target_pos[1]) and self.suicide is not True:
            return True

    # MAD
    def mad(self, target_pos, new_pos, color):
        catch = self.catch(new_pos, color)
        block = self.blocked(new_pos, self.index(new_pos, target_pos))
        if self.suicide is not True and block[2] is False:
            return True
