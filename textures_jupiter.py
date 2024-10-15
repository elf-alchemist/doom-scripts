from omg import MapEditor, WAD

log_file = None
log_path = 'switches.log'

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
]

sidedef_switch_doublet: list[tuple[str, str]] = [
    ('BRNPOIS',  'BRNPOIS1'),
    ('NUKEPOIS', 'NUKPOIS1'),
]


def log(line: str) -> None:
    global log_file
    if not log_file:
        log_file = open(log_path, 'w')
    print(line)
    log_file.write(line + '\n')


def sidedef_switch(map_editor: MapEditor, initial: str, desired_tex: str):
    for single_sidedef in map_editor.sidedefs:
        # Loop
        if single_sidedef.tx_up == initial:
            log(f'Found {initial} replaced with {desired_tex}')
            single_sidedef.tx_up = desired_tex
        # through
        if single_sidedef.tx_mid == initial:
            log(f'Found {initial} replaced with {desired_tex}')
            single_sidedef.tx_mid = desired_tex
        # all
        if single_sidedef.tx_low == initial:
            log(f'Found {initial} replaced with {desired_tex}')
            single_sidedef.tx_low = desired_tex


base = WAD(from_file='cdce-addon-jupiter.wad')


for map_slot in all_maps:
    log(f'Fixing map {map_slot}')
    for doublet in sidedef_switch_doublet:
        initial_texture = doublet[0]
        desired_texture = doublet[1]
        map_edit = MapEditor(base.maps[map_slot])
        sidedef_switch(map_edit, initial_texture, desired_texture)

base.to_file('cdce-addon-jupiter_fixed.wad')
