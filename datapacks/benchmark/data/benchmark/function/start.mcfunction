gamemode spectator @a
tp @a 0 150 0 0 0
scoreboard players set #run bm_timer 1
scoreboard players set #ticks bm_timer 0
tellraw @a {"text":"Benchmark Iniciado! Voo automático acionado.","color":"green"}
