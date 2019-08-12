# crie uma tupla preenchida com os 20 primeiros colocados da Tabela do campeonato brasileiro de futebol, na ordem de
# colocação. dpois mostre: a)apenas os 5 primeiros colocados; b)os ultimos 4 colocados; c) uma lista c/os times em ordem
#  alfabetica; d) em que posição na tabela está o time da capecoense.

campeonato = ("palmeiras", "flamengo", "bahia", "atlético", "corinthians", "são paulo", "santos", "inter", "ceara",
              "goias", "botafogo", "atletico-pr", "chapeco", "fortale", "flumine", "cruzeiro", "csa", "gremio", "avai",
              "vasco")
print(f"5 primeiros colocados: {campeonato[:5]}")
print(f"4 ultimo colocados: {campeonato[-4:]}")
print(f"times ordenados: {sorted(campeonato)}")
print(f"chapeco está na {campeonato.index('chapeco')+1} posição")