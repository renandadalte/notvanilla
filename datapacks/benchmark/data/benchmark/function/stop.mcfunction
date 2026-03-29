scoreboard players set #run bm_timer 0
playsound minecraft:block.note_block.bass master @a ~ ~ ~ 1 0.5
title @a actionbar {"text":"Benchmark terminado — para o log HWiNFO","color":"gray"}
tellraw @a {"text":"[Benchmark] Concluído. Para a gravação HWiNFO e guarda o CSV com data/versão do pack.","color":"gray"}
scoreboard players set #ticks bm_timer 0
