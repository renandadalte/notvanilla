execute if score #run bm_timer matches 1 as @a at @s run tp @s ~ ~ ~1.5
execute if score #run bm_timer matches 1 run scoreboard players add #ticks bm_timer 1
execute if score #ticks bm_timer matches 1200 run function benchmark:stop
