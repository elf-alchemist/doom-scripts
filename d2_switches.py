from omg import MapEditor, WAD

log_file = None
log_path = 'switches.log'

all_maps = [
    'MAP37',
    'MAP38',
    'MAP39',
    'MAP40',
    'MAP41',
    'MAP42',
    'MAP43',
    'MAP44',
    'MAP45',
    'MAP46',
    'MAP47',
    'MAP48',
    'MAP49',
    'MAP50',
    'MAP51',
    'MAP52',
    'MAP53',
    'MAP54',
    'MAP55',
    'MAP56',
    'MAP57',
    'MAP58',
    'MAP59',
    'MAP60',
    'MAP61',
    'MAP62',
    'MAP63',
    'MAP64',
    'MAP65',
    'MAP66',
    'MAP67',
    'MAP68',
    'MAP69',
    'MAP70',
    'MAP71',
    'MAP72',
    'MAP73',
    'MAP74',
    'MAP75',
    'MAP76',
    'MAP77',
]

sidedef_switch_doublet: list[tuple[str, str]] = [
    ('SW1BRN1',  'SW1BRCOM'),
    ('SW1STARG', 'SW1BRCOM'),
    ('SW1STON2', 'SW1BRCOM'),
    ('SW1STONE', 'SW1BRCOM'),
    ('SW2BRN1',  'SW2BRCOM'),
    ('SW2STARG', 'SW2BRCOM'),
    ('SW2STON2', 'SW2BRCOM'),
    ('SW2STONE', 'SW2BRCOM'),
]


def log(line: str) -> None:
    global log_file
    if not log_file:
        log_file = open(log_path, 'w')
    print(line)
    log_file.write(line + '\n')


def sidedef_switch(map_editor: MapEditor, initial_texture: str, desired_texture: str):
    for single_sidedef in map_editor.sidedefs:
        # Loop
        if single_sidedef.tx_up == initial_texture:
            log(f'Found {initial_tex}')
            single_sidedef.tx_up = desired_texture
        # through
        if single_sidedef.tx_mid == initial_texture:
            log(f'Found {initial_tex}')
            single_sidedef.tx_mid = desired_texture
        # all
        if single_sidedef.tx_low == initial_texture:
            log(f'Found {initial_tex}')
            single_sidedef.tx_low = desired_texture


base = WAD(from_file='cdce.wad')


for map_slot in all_maps:
    log(f'Fixing map {map_slot}')
    for doublet in sidedef_switch_doublet:
        initial_tex = doublet[0]
        desired_tex = doublet[1]
        map_edit = MapEditor(base.maps[map_slot]) #type:ignore
        sidedef_switch(map_edit, initial_tex, desired_tex)


base.to_file('cdce_fixed.wad')
