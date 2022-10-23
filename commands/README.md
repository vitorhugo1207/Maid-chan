<h1 align="center">🖱️ Commands 🖱️</h1>

<!-- ---------------------------------------------- -->
<br>

## 📝 Table of Contents

- [Home](../)
- [Pics](#pics)
- [Recreation](#recreation)
- [Utilities](#utilities)
- [Music](#music)

<br>

Note: how standard the bot use prefix: ``m!``, but may variable depending server config. Mention the bot for show prefix standard of the server. 

---
<!-- ---------------------------------------------- -->

## Pics <a name="pics"></a>
This type commands return a link image that is open automatically open in own Discord App. <br>
- Anime <br>
The command **Anime** use **API Waifu Pics**, see [technologies used](#Technologies_Used) for more information. This command return **only images sfw**. <br>
Sintax example:
```
m!anime
``` 
You also can pass one argument for specify the anime type, sintax example:
```
m!anime waifu
```
Arguments list: waifu, neko, shinobu, megumin , bully, cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile, wave, highfive, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe

<br>

- Hentai <br>
The command **Hentai** use **API Waifu Pics**, see [technologies used](#Technologies_Used) for more information. This command may be used **only nsfw chats**.<br>
Sintax example:
```
m!hentai
```
You also can pass one argument for specify the hentai type, sintax example:
```
m!hentai neko
```
Arguments list: waifu, neko, trap, blowjob

<br>

- Fox <br>
The command **Fox** use **Random Fox API**, see [technologies used](#Technologies_Used) for more information.
Sintax example:
```
m!fox
```

---
## Recreation <a name="recreation"></a>
- Dice <br>

This command is part of **RollDice Project**, see [technologies used](#Technologies_Used) for more information. The rolldice can roll dice at the interval that you choose, times as you want and sum bonus. And return list of rolls (with bonus if add) and total roll.<br>
Sintax example:
```
m!dice 2d30+4
``` 
"2" is amount of times the dice will be rolled, "30" is the max number of dice and "+4" is the bonus will be sum in total roll. If this command for used without amount of time, it will roll just one time; without "30" it will return error; without "+4", obviously, it will return without any bonus, the bonus supported is ``+`` ``-``, ``*`` or ``/``. <br>
Return example:
```
2d30+4
[13, 1, '+4'] -> 18
```

<br>

---
## Utilities <a name="utilities"></a>
- Say <br>
This command will return that you tell for repeat and will delete your mensage. <br>
Sintax example:
```
m!say Hello, world!
```
<br>

- Math <br>
This command do math operations. <br>
Sintax example:
```
m!math (2+2)*4
```
Operations supported: ``+`` ``-``, ``*``, ``/``, ``**`` and ``sqrt``.

<br>

- Avatar <br>
This type commands return a link avatar image that is open automatically open in own Discord App. <br>
Sintax example:
```
m!avatar @Maid-chan#0233
```
If no pass **user id** or **user name**, it will return your avatar image.

<br>

- Ping <br>
This command will return ms response.
Sintax example:
```
m!ping
```
Return example:
```
Pong! 38ms.
```

<br>

- Scene Anime Search <br>
This command will search for anime using a Scene (gif, image, vídeo). This command use **Trace.moe API**, see [technologies used](#Technologies_Used) for more information. By limitations of API file size is limited to 10MB and the recommended resolution is 640 x 360px.
Sintax example:
```
m!animesearch https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg
```
Return example:
```
Similarity: 97.35

Anilist: https://anilist.co/anime/21034
Tittle romaji: Gochuumon wa Usagi desu ka??
Tittle romaji: Is the Order a Rabbit?? Season 2
Episode: 1
Time between: 0:04:48 and 0:04:52
```

## Music <a name="music"></a>
This command play some video from Youtube in voice channel. <br>

- Join <br>
Join in voice channel you are in.
Sintax example:
```
m!join
```

<br>

- Leave <br>
Leave of voice channel.
Sintax example:
```
m!leave
```

<br>

- Stop <br>
Stop play music.
Sintax example:
```
m!stop
```

<br>

- Play <br>
Play some video passing a link.
Sintax example:
```
m!play https://www.youtube.com/watch?v=9lNZ_Rnr7Jc
```

<br>

- Pause <br>
Pause Music.
Sintax example:
```
m!pause
```

<br>

- Resume <br>
Resume Music.
```
m!resume
```
