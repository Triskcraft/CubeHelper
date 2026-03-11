from .modules import *
import CubeHelper.ListsLogic.MaterialLists  as MaterialLists

async def load(client: commands.Bot):
    print(f'\nLoading\t\tAddon\t\t{addon_name}')
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    cogs = [os.path.join(BASE_DIR, 'Commands'), os.path.join(BASE_DIR, 'ContextMenus'), os.path.join(BASE_DIR, 'Behaviours')]

    for cog in cogs:
        scripts = [filename for filename in os.listdir(cog) if filename.endswith('.py')]
        for script in scripts:
            try:
                parent, ccog = cog.split(os.sep)[-2:]
                module = os.path.join(parent, ccog, script).replace(os.sep, ".")[:-3]
                await client.load_extension(module)
                print(f'   • Loaded {os.path.basename(cog[:-1])} {script[:-3]}')
            except Exception:
                print(f'   • Unable to load {os.path.basename(cog[:-1])} {script[:-3]}')

    print(f'   • Updating Logs...')
    await MaterialLists.updateStates(client)
    print(f'   • Logs updated')
    print(f'   • Reactivating lists...')
    await MaterialLists.reactiveLists(client)
    print(f'   • Lists reactivated')
            
    print('   Loading Complete')
