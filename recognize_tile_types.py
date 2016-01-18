__author__ = 'PiotrB'


class TileCheckResult:
    def __init__(self):
        pass

    NO_RESULT = 0
    NON_NEGATIVE = 1
    ARE_FIXED = 2
    FIXED_NON_ORIGINAL = 4
    VARIED_NON_ORIGINAL = 8
    PARAMETRIC = 16


def check_dependencies_non_negative():
    pass


def check_target_tiles_are_fixed():
    pass


def check_target_tiles_are_fixed_non_original():
    pass


def check_target_tiles_are_varied_non_original():
    pass


def recognize_tile_types():
    check_result = TileCheckResult.NO_RESULT
    if check_dependencies_non_negative():
        print('All target tiles are fixed and the same as original ones because all elements of each distance vector '
              'are non-negative')
        return TileCheckResult.NON_NEGATIVE
    if check_target_tiles_are_fixed():
        print('All target tiles are fixed and the same as original ones because all iterations within each original '
              'tile are valid')
        return TileCheckResult.ARE_FIXED
    if check_target_tiles_are_fixed_non_original():
        print('There exist fixed tiles different from original ones')
        check_result = TileCheckResult.FIXED_NON_ORIGINAL
    if check_target_tiles_are_varied_non_original():
        print('There exist varied tiles different from original ones')
        check_result += TileCheckResult.VARIED_NON_ORIGINAL
    if check_target_tiles_are_fixed():
        print('There exist fixed parametric tiles')
        check_result += TileCheckResult.PARAMETRIC
    return check_result
