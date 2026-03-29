scoreboard players set #run bm_timer 0
spark profiler stop
tellraw @a ["",{"text":"[Benchmark] ","color":"gold"},{"text":"▶ Parar Spark cliente (clique)","color":"red","clickEvent":{"action":"run_command","value":"/sparkc profiler stop"},"hoverEvent":{"action":"show_text","contents":"/sparkc profiler stop — copia o link"}}]
tellraw @a {"text":"[Benchmark] Concluído. Para o HWiNFO e guarda CSV + links Spark.","color":"gray"}
scoreboard players set #ticks bm_timer 0
