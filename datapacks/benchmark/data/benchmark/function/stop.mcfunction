scoreboard players set #run bm_timer 0
spark profiler stop
playsound minecraft:block.note_block.pling master @a ~ ~ ~ 1 0.8
title @a actionbar {"text":"Spark SERVIDOR parado — para o CLIENTE (ver chat)","color":"red"}
tellraw @a ["",{"text":"[Benchmark] ","color":"gold"},{"text":"▶ Spark cliente: parar (clique)","color":"red","clickEvent":{"action":"run_command","value":"/sparkc profiler stop"},"hoverEvent":{"action":"show_text","contents":"/sparkc profiler stop"}}]
tellraw @a ["",{"text":"[Benchmark] ","color":"gold"},{"text":"▶ Ou sugerir /sparkc profiler stop (clique)","color":"aqua","clickEvent":{"action":"suggest_command","value":"/sparkc profiler stop"}}]
tellraw @a {"text":"[Benchmark] Concluído. Copia o link do Spark cliente. Para o HWiNFO e guarda o CSV.","color":"gray"}
scoreboard players set #ticks bm_timer 0
