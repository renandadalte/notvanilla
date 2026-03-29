spark profiler cancel
spark profiler start
tellraw @a ["",{"text":"[Benchmark] ","color":"gold"},{"text":"▶ Iniciar Spark cliente (clique)","color":"green","clickEvent":{"action":"run_command","value":"/sparkc profiler start"},"hoverEvent":{"action":"show_text","contents":"/sparkc profiler start"}}]
tellraw @a {"text":"[Benchmark] Liga o log HWiNFO antes disto. Clica no verde; o percurso começa em ~1s.","color":"yellow"}
schedule function benchmark:_begin_run 20t
