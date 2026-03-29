execute if score #run bm_timer matches 1 run scoreboard players add #ticks bm_timer 1
execute if score #run bm_timer matches 1 if score #ticks bm_timer matches 1..600 as @a at @s run tp @s ~ ~ ~1.5
execute if score #run bm_timer matches 1 if score #ticks bm_timer matches 600 run tp @a 0 150 0 0 0
execute if score #run bm_timer matches 1 if score #ticks bm_timer matches 601..1200 as @a at @s run tp @s ~ ~ ~1.5
execute if score #ticks bm_timer matches 1200 run function benchmark:stop
