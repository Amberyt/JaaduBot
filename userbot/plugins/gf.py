"""
Available Commands: .gf

by @KshitijGagan
inspired from @xcruzhd2 """

from telethon import events

import asyncio




@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 21)

    input_str = event.pattern_match.group(1)

    if input_str == "gf":

        await event.edit(input_str)

        animation_chars = [
        
            "`Ruk jaa , Abhi teri GF ko Fuck karta hu `",
            "`Making your Gf warm π₯`",
            "`Pressing her boobs π€π`",
            "`Stimulating her pussyπ`",
            "`Fingering her pussy π§ππ `",
            "`Asking her to taste my DICKπ`",
            "`Requested acceptedπ»π, Ready to taste my DICKπ`",
            "`Getting her ready to fuck π`",
            "`Your GF Is Ready To Fuck`",
            "`Fucking Your GFππ\n\n\nYour GF's Pussy Get Red\nTrying new SEX position to make her Squirt\n\nAlmost Done. 0%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's Pussy Get White\nHe squirted like a showerπ§π¦π\n\nAlmost Done..\n\nFucked Percentage... 4%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's Pussy Get Red\nDoing Extreme SEX with herπ\n\nAlmost Done...\n\nFucked Percentage... 8%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's Pussy Get Red\nWarming her Assπ to Fuck!ππ\n\nAlmost Done....\n\nFucked Percentage... 20%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's ASSπ Get Red\nInserted my Penisπ in her ASSπ\n\nAlmost Done.....\n\nFucked Percentage... 36%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's ASSπ Get Red\ndoing extreme sex with her\n\nAlmost Done......\n\nFucked Percentage... 52%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's Boobsπ€π are Awesome\nPressing her tight Nipplesπ€π\n\nAlmost Done.......\n\nFucked Percentage... 84%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's Lips Get Horny\nDoing French Kiss with your GFππ\n\nAlmost Done........\n\nFucked Percentage... 89%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's Boobsπ€π are Awesome\nI am getting ready to cum in her Mouthπ\n\nAlmost Done.......\n\nFucked Percentage... 90%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's Boobsπ€π are Awesome\nFinally, I have cummed in her Mouthππ\n\nAlmost Done.......\n\nFucked Percentage... 96%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's is Awesome\nShe is Licking my Dickπ in the Awesome Wayβπ€π€ππ\n\nAlmost Done.......\n\nFucked Percentage... 100%\nβββββββββββββββββββββββββ `",
            "`Fucking Your GFππ\n\n\nYour GF's ASSπ Get Red\nCummed On her Mouthππ\n\nYour GF got Pleasure\n\nResult: Now I Have 1 More SEX Partner ππ`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 100])
