from omg import MapEditor, WAD

log_file = None
log_path = 'tnt_textures.log'

all_maps = [
    'MAP06',
    'MAP08',
    'MAP10',
    'MAP11',
    'MAP13',
    'MAP16',
    'MAP19',
    'MAP20',
    'MAP21',
    'MAP30',
    'MAP31',

]

sidedef_arr: list[tuple[str, str]] = [
    ('DBRAIN1', 'MC01'),
    ('MC2', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('MC', 'MC01'),
    ('DBRAIN4', 'MC01'),
]


def log(line: str) -> None:
    global log_file
    if not log_file:
        log_file = open(log_path, 'w')
    print(line)
    log_file.write(line + '\n')


def sidedef_list(editor: MapEditor, init_tex: str, desired_tex: str):
    for single_sidedef in editor.sidedefs:
        # Loop
        if single_sidedef.tx_up == init_tex:
            log(f'Found hi tex {init_tex} replaced by {desired_tex}')
        # through
        if single_sidedef.tx_mid == init_tex:
            log(f'Found mid tex {init_tex} replaced by {desired_tex}')
        # all
        if single_sidedef.tx_low == init_tex:
            log(f'Found low tex {init_tex} replaced by {desired_tex}')


base = WAD(from_file='cdce-addon-plutonia.wad')


for map_slot in all_maps:
    log(f'Fixing map {map_slot}')
    for sidedef in sidedef_arr:
        initial = sidedef[0]
        desired = sidedef[1]
        map_edit = MapEditor(base.maps[map_slot])
        sidedef_list(map_edit, initial, desired)

