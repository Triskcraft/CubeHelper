from ..Functions import *
from ..modules import *

import CubeHelper.ListsLogic.MaterialLists as MaterialLists

class CubeHelperOnMessageDelete(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if MaterialLists.isActiveList(message.id):
            MaterialLists.UpdateListInfo(message.id, {'state':'deactivated'})
    
async def setup(client: commands.Bot):
    await client.add_cog(CubeHelperOnMessageDelete(client))