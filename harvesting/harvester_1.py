from coordinate_handling import Coord

class Direction(Enum):
    UP = -1
    DOWN = 1
    LEFT = -1
    RIGHT = 1


def remove_empty_scan_results(scan_data) -> dict:
    cleaned_scan_results = {}
    for each_scan_result in scan_data:
        record = scan_data[each_scan_result]
        if record.status != "empty":
            cleaned_scan_results[each_scan_result] = record
    return cleaned_scan_results



def move(cardinal,current_pos):
    ''' Takes in a coordinate string
        splits it into workable parts
        moves the bot
        returns updated position
    '''
    row = current_pos.get_row()
    col = current_pos.get_col()
    ''' This whole section can be better I feel'''
    # Change the positoin of the row
    if cardinal == Direction.UP:
        row = row + Direction.UP
        
    elif cardinal == Direction.DOWN:
        row = row + Direction.DOWN
        
    #Change the position of the col
    elif cardinal == Direction.LEFT:
        col = col + Direction.LEFT
    elif cardinal == Direction.RIGHT:
        col = col + Direction.RIGHT
    else:
        raise Exception("invalid direction")
    updated_coord = Coord(row,col)
    status = self.move(updated_coord)
        
    

def main() -> None:
    scanner = get_component("scanner_1")
    scanned = scanner.get_scanned()
    scanned = remove_empty_scan_results(scanned)
    for each_item in scanned:
        print(f"{each_item}:{scanned[each_item]}")


main()