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
    ('SLADRIP1', 'T_SLAD01'),
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
    ('WFALL1',   'TNTWALL1'),
    ('WFALL2',   'TNTWALL1'),
    ('WFALL3',   'TNTWALL1'),
    ('WFALL4',   'TNTWALL1'),
    ('FALL3',    'TNTWALL1'),
    ('SW1GSTON', 'SW1TNT1'),
    ('SW2GSTON', 'SW2TNT1'),
    ('SW1SKULL', 'SW1TNT2'),
    ('SW2SKULL', 'SW2TNT2'),
]


def log(line: str) -> None:
    global log_file
    if not log_file:
        log_file = open(log_path, 'w')
    print(line)
    log_file.write(line + '\n')


def sidedef_list(editor: MapEditor, init_tex: str, tex: str):
    for single_sidedef in editor.sidedefs:
        # Loop
        if single_sidedef.tx_up == init_tex:
            log(f'Found hi tex {init_tex} replaced by {tex}')
        # through
        if single_sidedef.tx_mid == init_tex:
            log(f'Found mid tex {init_tex} replaced by {tex}')
        # all
        if single_sidedef.tx_low == init_tex:
            log(f'Found low tex {init_tex} replaced by {tex}')


base = WAD(from_file='cdce-addon-tnt.wad')


for map_slot in all_maps:
    log(f'Fixing map {map_slot}')
    for sidedef in sidedef_arr:
        initial = sidedef[0]
        desired = sidedef[1]
        map_edit = MapEditor(base.maps[map_slot])
        sidedef_list(map_edit, initial, desired)

