from omg import MapEditor, WAD

log_file = None
log_path = 'tnt_textures.log'

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
    ('SLADRIP1', 'T_SLAD01'),
    ('SLADRIP2', 'T_SLAD01'),
    ('SLADRIP3', 'T_SLAD01'),
    ('SLAD2',    'T_SLAD01'),
    ('SLAD3',    'T_SLAD01'),
    ('SLAD4',    'T_SLAD01'),
    ('SLAD5',    'T_SLAD01'),
    ('SLAD6',    'T_SLAD01'),
    ('SLAD7',    'T_SLAD01'),
    ('SLAD8',    'T_SLAD01'),
    ('SLAD9',    'T_SLAD01'),
    ('SLAD10',   'T_SLAD01'),
    ('SLAD11',   'T_SLAD01'),
    ('BLODGR1',  'T_BLOD1'),
    ('BLODGR2',  'T_BLOD1'),
    ('BLODGR3',  'T_BLOD1'),
    ('BLODGR4',  'T_BLOD1'),
    ('BLOD3',    'T_BLOD1'),
    ('WFALL1',   'T_WALL1'),
    ('WFALL2',   'T_WALL1'),
    ('WFALL3',   'T_WALL1'),
    ('WFALL4',   'T_WALL1'),
    ('FALL3',    'T_WALL1'),
    ('SW1GSTON', 'SW1TNTA'),
    ('SW2GSTON', 'SW2TNTA'),
    ('SW1SKULL', 'SW1TNT1'),
    ('SW2SKULL', 'SW2TNT1'),
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


base = WAD(from_file='cdce-addon-tnt.wad')


for map_slot in all_maps:
    log(f'Fixing map {map_slot}')
    for sidedef in sidedef_arr:
        initial = sidedef[0]
        desired = sidedef[1]
        map_edit = MapEditor(base.maps[map_slot])
        sidedef_list(map_edit, initial, desired)
    base.to_file('./doom-addon-tnt.wad')

