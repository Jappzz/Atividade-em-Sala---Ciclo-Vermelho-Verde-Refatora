"""
PLANO (Passo 1)
===============
Problema: calculadora de frete de uma loja virtual.

Casos que vou testar (três variações de comportamento + um caso de erro):
  1. PAC:             R$ 10,00 fixos + R$ 2,00 por kg  (3 kg -> 16,00)
  2. SEDEX:           R$ 20,00 fixos + R$ 4,00 por kg  (3 kg -> 32,00)
  3. Retirada na loja: sempre R$ 0,00, não importa o peso
  4. Tipo de entrega desconhecido -> levanta ValueError

Padrão de projeto escolhido: STRATEGY.
Por quê: cada tipo de entrega é uma "regra de cálculo" diferente para a mesma
tarefa (calcular o frete). Na fase verde vou usar if/elif; quando surgir uma
nova modalidade, o if/elif cresceria e eu teria que mexer em código que já
funciona. Com Strategy, cada modalidade vira uma classe e novas modalidades
entram sem alterar as existentes (princípio aberto/fechado).


Uso de IA: usei IA para sugerir o tema (frete) e revisar a estrutura dos
commits. Os testes e o padrão foram conferidos por mim.
"""
import pytest

from frete import calcular_frete


def test_pac_cobra_taxa_fixa_mais_valor_por_kg():
    assert calcular_frete("PAC", 3) == 16.00


def test_sedex_cobra_taxa_fixa_mais_valor_por_kg():
    assert calcular_frete("SEDEX", 3) == 32.00


def test_retirada_na_loja_e_gratis_independente_do_peso():
    assert calcular_frete("RETIRADA", 10) == 0.00


def test_tipo_de_entrega_desconhecido_levanta_erro():
    with pytest.raises(ValueError):
        calcular_frete("DRONE", 1)
