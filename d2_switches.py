from omg import MapEditor, WAD

log_file = None
log_path = 'masterpack.log'
buffer_size = 16384
source_dir = 'source/'

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

sidedef_switch_doublet = [
    ['SKY4', 'MSKY1'],

    ['DBRAIN1', 'WATER'],
    ['SW1COMP', 'TT1COMP'],
    ['SW1STON1', 'TT1STON1'],
    ['SW1STON2', 'TT1STON2'],

    ['SW1STON2', 'TT1STON5'],

    ['SW1BRIK', 'TT1BRIK'],
    ['SW1STON1', 'TT1STON3'],
    ['SW1STON2', 'TT1STON4'],

    ['SW1VINE', 'TT1VINE'],
    ['SW1PIPE', 'TT1PIPE'],
    ['SW1STON1', 'TT1STON5'],
    ['SW1STON2', 'TT1STON6'],
    ['SW1STON6', 'TT1STON7'],

    ['PIC00', 'PORTAL1'],
    ['PIC01', 'PORTAL2'],
    ['PIC06', 'PORTAL3'],
    ['PIC07', 'PORTAL4'],
    ['PIC13', 'PORTAL5'],
]

def log(line: str) -> None:
    global log_file
    if not log_file:
        log_file = open(log_path, 'w')
    print(line)
    log_file.write(line + '\n')


def massive_simple_sidedef_switch(map: MapEditor, initial_tx: str, desired_tx: str):
    for sidedef in map.sidedefs:
        if sidedef.tx_up == initial_tx:
            sidedef.tx_up = desired_tx
        if sidedef.tx_mid == initial_tx:
            sidedef.tx_mid = desired_tx
        if sidedef.tx_low == initial_tx:
            sidedef.tx_low = desired_tx

base = WAD(from_file='doom_complete.wad')

for doublet in sidedef_switch_doublet:
    for map_slot in all_maps:
        map_edit = MapEditor(base.maps[map_slot]) #type:ignore
        initial_tex = doublet[0]
        desired_tex = doublet[1]
        massive_simple_sidedef_switch(map_edit, initial_tex, desired_tex)

