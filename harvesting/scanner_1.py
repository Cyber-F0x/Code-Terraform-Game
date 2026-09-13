from coordinate_handling import Coord

sector_data = {}

def generate_sector_names() -> list:
    sectors = []
    for row in range(65,73):
        for col in range(1,25):
            sectors.append(Coord(row,col).toString())
    return sectors

def perform_scan(debug=True):
    sectors = generate_sector_names()
    for each_sector in sectors:
        result = self.scan(each_sector)
        if result.status == "ok":
            sector_data[each_sector] = result
            if debug:
                print(f"Sector: {each_sector}: {result.name} - {result.value}")
        elif result.status == "empty":
            pass
        else:
            if debug:
                print(f"Something went wrong scaning {each_sector}")
            print(result.message)



def main():
    perform_scan()

main()