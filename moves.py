from pieces import Pieces


class Moves:
    def __init__(self, target_pos, new_pos, name, color, data):
        self.catch_color = None
        self.data = data
        self.name = name
        self.color = color
        self.suicide = False
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
        match color:
            case 'black':
                if ((target_pos[0] == new_pos[0] and (target_pos[1] // 72) in range(8))
                    or target_pos[0] // 100 in range(9) and target_pos[1] == new_pos[1]) \
                        and self.catch_color != 'black':
                    return True

            case 'white':
                if ((target_pos[0] == new_pos[0] and (target_pos[1] // 72) in range(8))
                    or target_pos[0] // 100 in range(9) and target_pos[1] == new_pos[1]) \
                        and self.catch_color != 'white':
                    return True

    # KNIGHT
    def knight(self, target_pos, new_pos, color):
        catch = self.catch(new_pos, color)
        # L normal
        if (new_pos[0] + 100 == target_pos[0] or new_pos[0] - 100 == target_pos[0]) \
                and (new_pos[1] - 144 == target_pos[1] or new_pos[1] + 144 == target_pos[1]) and self.suicide is not True:

            return True
        # L reversed
        if (new_pos[0] + 200 == target_pos[0] or new_pos[0] - 200 == target_pos[0]) \
                and (new_pos[1] - 72 == target_pos[1] or new_pos[1] + 72 == target_pos[1]) and self.suicide is not True:
            return True

