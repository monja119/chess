from board import Board

class Moves:
    def __init__(self, target_pos, new_pos, name, color, data, target_index):
        self.catch_color = None
        self.data = data
        self.name = name
        self.color = color
        self.suicide = False
        self.match = False
        self.moving = False
        self.target_pos, self.target_index = target_pos, target_index
        movement = {
            'pawn': 'self.pawn(target_pos, new_pos, color)',
            'round': 'self.round(target_pos, new_pos, color)',
            'knight': 'self.knight(target_pos, new_pos, color)',
            'mad': 'self.mad(target_pos, new_pos, color)',
            'queen': 'self.queen(target_pos, new_pos, color)',
            'king': 'self.king(target_pos, new_pos, color)',
        }

        # accepting
        self.accept = eval(movement[name])

    def catch(self, new_pos):
        for k in range(len(self.data)):
            if self.data[k]['pos'] == new_pos:
                self.catch_color = self.data[k]['src'].split('/')[2]
                self.catch_name = self.data[k]['src'].split('/')[-1].split('.')[0]
                self.match = True
                if self.catch_color == self.color and self.data[k]['pos'] is not None:
                    self.suicide = True
                    break
                if self.moving == True:
                    # changing indexing
                    self.data[self.data.index(self.data[k])] = self.data[self.target_index]
                    self.data[self.target_index]['pos'] = None
                    break

                return True
                break

    # allowing user to pass
    def allow_pass_y(self, new_pos, target_pos):
        passing = True
        index_x, index_y = self.index(new_pos, target_pos)
        if index_y < 0:
            signe_y = '-'
        else:
            signe_y = '+'
        for i in range(abs(index_y)):
            target_y = eval('{} {} {}'.format(self.target_pos[1], signe_y, (72 * (i + 1))))
            for k in range(len(self.data)):
                if (new_pos[0], target_y) == self.data[k]['pos']:
                    passing = False
                    break
        return passing

    def index(self, new_pos, target_pos):
        index_x = ((new_pos[0] - 15) - (target_pos[0] - 15)) // 100
        index_y = (new_pos[1] - target_pos[1]) // 72

        return (index_x, index_y)

    def blocked(self, new_pos, index):
        blocked_x, blocked_y, blocked_xy = False, False, False
        # x y path
        lis_x, lis_y = [], []
        x, y = index[0], index[1]

        if x < 0:
            signe_x = '-'
        else:
            signe_x = '+'

        if y < 0:
            signe_y = '-'
        else:
            signe_y = '+'

        for i in range(abs(x)):
            target_x = eval('{} {} {}'.format(self.target_pos[0], signe_x, (100 * (i + 1))))
            lis_x.append(target_x)
        for j in range(abs(y)):
            target_y = eval('{} {} {}'.format(self.target_pos[1], signe_y, (72 * (j + 1))))
            lis_y.append(target_y)

        # blocked vertical
        path_xy = []
        for i in range(len(lis_y)):
            for k in range(len(self.data)):
                if (new_pos[0], lis_y[i]) == self.data[k]['pos']:
                    target_color = self.data[k]['src'].split('/')[2]
                    if self.color == target_color:
                        blocked_y = True


        # blocked horizontal
        for i in range(len(lis_x)):
            for k in range(len(self.data)):
                if (lis_x[i], new_pos[1]) == self.data[k]['pos']:
                    target_color = self.data[k]['src'].split('/')[2]
                    if self.color == target_color:
                        blocked_x = True

        # blocked xy
        if abs(index[0]) == abs(index[1]):
            for k in range(len(lis_x)):
                pos = (lis_x[k], lis_y[k])
                for i in range(len(self.data)):
                    if pos == self.data[i]['pos']:
                        target_color = self.data[k]['src'].split('/')[2]
                        if self.color == target_color:
                            blocked_xy = True
        else:
            blocked_xy = True

        return (blocked_x, blocked_y, blocked_xy)

    def pawn(self, target_pos, new_pos, color):
        catch = self.catch(new_pos)
        index_x, index_y = self.index(new_pos, target_pos)
        passing = self.allow_pass_y(new_pos, target_pos)
        # vertical move
        if self.suicide is not True and new_pos[0] == target_pos[0] and abs(index_y) <= 2 and passing is True:
            allowed = False
            for k in range(len(self.data)):
                if target_pos == self.data[k]['pos']:
                    # trying if the pawn was already moved
                    try:
                        if self.data[k]['moved'] is True and abs(index_y) == 1:
                            match color:
                                case 'black':
                                    if index_y < 0:
                                        allowed = True
                                case 'white':
                                    if index_y > 0:
                                        allowed = True
                        else:
                            allowed = False
                    except KeyError:
                        self.data[k]['moved'] = True
                        allowed = True
                    break
            if allowed:
                return True

        # axis movement
        elif self.suicide is not True and abs(index_x) == 1 and catch is True:
            if self.color == 'white' and index_y == 1:

                self.moving = True
                self.catch(new_pos)
                return True
            elif self.color == 'black' and index_y == -1:
                self.moving = True
                self.catch(new_pos)
                return True

    # ROUND
    def round(self, target_pos, new_pos, color):
        catch = self.catch(new_pos)
        block = self.blocked(new_pos, self.index(new_pos, target_pos))
        index_x, index_y = self.index(new_pos, target_pos)
        if block[1] is False and abs(index_x) == 0:
            self.moving = True
            self.catch(new_pos)
            return True
        elif block[0] is False and abs(index_y) == 0:
            self.moving = True
            self.catch(new_pos)
            return True

    # KNIGHT
    def knight(self, target_pos, new_pos, color):
        catch = self.catch(new_pos)
        # L normal

        if (new_pos[0] + 100 == target_pos[0] or new_pos[0] - 100 == target_pos[0]) \
                and (
                new_pos[1] - 144 == target_pos[1] or new_pos[1] + 144 == target_pos[1]) and self.suicide is not True:
            # passing horizontal
            self.moving = True
            self.catch(new_pos)
            return True
        # L reversed
        if (new_pos[0] + 200 == target_pos[0] or new_pos[0] - 200 == target_pos[0]) \
                and (new_pos[1] - 72 == target_pos[1] or new_pos[1] + 72 == target_pos[1]) and self.suicide is not True:
            self.moving = True
            self.catch(new_pos)
            return True

    # MAD
    def mad(self, target_pos, new_pos, color):
        catch = self.catch(new_pos)
        block = self.blocked(new_pos, self.index(new_pos, target_pos))
        if block[2] is False:
            self.moving = True
            self.catch(new_pos)
            return True

    def queen(self, target_pos, new_pos, color):
        catch = self.catch(new_pos)
        mad = self.mad(target_pos, new_pos, color)
        round = self.round(target_pos, new_pos, color)

        if mad is True or round is True:
            self.moving = True
            self.catch(new_pos)
            return True

    def king(self, target_pos, new_pos, color):
        catch = self.catch(new_pos, color)
        x = target_pos[0]
        y = target_pos[1]
        allowed_xy = []
        allowed_x = [
            x,
            x + 100,
            x - 100
        ]
        allowed_y = [
            y,
            y + 72,
            y - 72
        ]

        for i in range(6):
            counter = i % 3
            if i < 3:
                for j in range(3):
                    allowed_xy.append((allowed_x[counter], allowed_y[j]))
            else:
                for j in range(3):
                    allowed_xy.append((allowed_x[j], allowed_y[counter]))

        for k in range(len(allowed_xy)):
            if allowed_xy[k] == new_pos and self.suicide is False:
                self.moving = True
                self.catch(new_pos)
                return True
                break
