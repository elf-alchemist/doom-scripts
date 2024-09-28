from omg import MapEditor, WAD

log_file = None
log_path = 'plutonia_textures.log'

all_maps = [
    'MAP01',
    'MAP02',
    'MAP03',
    'MAP04',
    'MAP05',
    'MAP06',
    'MAP07',
    'MAP08',
    'MAP09',
    'MAP10',
    'MAP11',
    'MAP12',
    'MAP13',
    'MAP14',
    'MAP15',
    'MAP16',
    'MAP17',
    'MAP18',
    'MAP19',
    'MAP20',
    'MAP21',
    'MAP22',
    'MAP23',
    'MAP24',
    'MAP25',
    'MAP26',
    'MAP27',
    'MAP28',
    'MAP29',
    'MAP30',
    'MAP31',
    'MAP32',
]

sidedef_arr: list[tuple[str, str]] = [
    ('DBRAIN1',  'MC01'),
    ('MC2',      'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('MC',       'MC01'),
    ('DBRAIN4',  'MC01'),
    ('FIREBLU1', 'AROCK1'),
    ('AROCK2',   'AROCK1'),
    ('AROCK3',   'AROCK1'),
    ('AROCK4',   'AROCK1'),
    ('AROCK5',   'AROCK1'),
    ('FIREBLU2', 'AROCK1'),
    ('SW1SKULL', 'SW1PLUT'),
    ('SW2SKULL', 'SW2PLUT'),
]


def log(line: str) -> None:
    global log_file
    if not log_file:
        log_file = open(log_path, 'w')
    print(line)
    log_file.write(line + '\n')


def sidedef_list(editor: MapEditor, init_tex: str, tex: str):
    index = 0
    for single_sidedef in editor.sidedefs:
        sector = single_sidedef.sector
        off_x = single_sidedef.off_x
        off_y = single_sidedef.off_y
        # Loop
        if single_sidedef.tx_up == init_tex:
            log(f'  #{index}\tHi  {init_tex}\tx\t{off_x} y\t{off_y}\t-> {tex} := {sector}')
        # through
        if single_sidedef.tx_mid == init_tex:
            log(f'  #{index}\tMid {init_tex}\tx\t{off_x} y\t{off_y}\t-> {tex} := {sector}')
        # all
        if single_sidedef.tx_low == init_tex:
            log(f'  #{index}\tLow {init_tex}\tx\t{off_x} y\t{off_y}\t-> {tex} := {sector}')
        index += 1

base = WAD(from_file='cdce-addon-plutonia.wad')


for map_slot in all_maps:
    log(f'Fixing map {map_slot}')
    for sidedef in sidedef_arr:
        initial = sidedef[0]
        desired = sidedef[1]
        map_edit = MapEditor(base.maps[map_slot])
        sidedef_list(map_edit, initial, desired)

