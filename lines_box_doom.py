from omg import MapEditor, WAD

log_file = None
log_path = 'lines_box_doom1.log'

all_maps = [
    'MAP01',
    'MAP02',
    'MAP03',
]

linedef_arr: list[tuple[str, str]] = [
    ('271', 'FOUND'),
    ('272', 'FOUND'),
    ('273', 'FOUND'),
]


def log(line: str) -> None:
    global log_file
    if not log_file:
        log_file = open(log_path, 'w')
    print(line)
    log_file.write(line + '\n')


def sidedef_list(editor: MapEditor, action: str, found: str):
    index = 0
    for single_linedef in editor.linedefs:
        log(f"{single_linedef.action} => {single_linedef.tag}")
        index += 1


base = WAD(from_file='bd1.wad')


for map_slot in all_maps:
    log(f'Fixing map {map_slot}')
    for linedef in linedef_arr:
        initial = linedef[0]
        desired = linedef[1]
        map_edit = MapEditor(base.maps[map_slot])
        sidedef_list(map_edit, initial, desired)
