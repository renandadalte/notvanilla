spark profiler cancel
spark profiler start
playsound minecraft:block.note_block.pling master @a ~ ~ ~ 1 1.2
title @a actionbar {"text":"Spark SERVIDOR ligado — agora o CLIENTE (ver chat)","color":"yellow"}
tellraw @a ["",{"text":"[Benchmark] ","color":"gold"},{"text":"▶ Spark cliente: executar (clique)","color":"green","clickEvent":{"action":"run_command","value":"/sparkc profiler start"},"hoverEvent":{"action":"show_text","contents":"Executa /sparkc profiler start"}}]
tellraw @a ["",{"text":"[Benchmark] ","color":"gold"},{"text":"▶ Ou abrir chat com o comando (clique)","color":"aqua","clickEvent":{"action":"suggest_command","value":"/sparkc profiler start"},"hoverEvent":{"action":"show_text","contents":"Coloca o texto no chat; confirma com Enter"}}]
tellraw @a {"text":"[Benchmark] O servidor NÃO corre /sparkc no teu PC. Tens de clicar acima OU escrever /sparkc profiler start. Percurso em ~3s.","color":"red"}
tellraw @a {"text":"[Benchmark] HWiNFO: inicia o log antes se ainda não estiver a gravar.","color":"gray"}
schedule function benchmark:_begin_run 60t
