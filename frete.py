"""
Cálculo de frete.

PADRÃO DE PROJETO APLICADO NA REFATORAÇÃO: STRATEGY

Participantes (nomeados conforme o domínio):
  - Strategy (interface):    EstrategiaDeFrete   -> define calcular(peso_kg)
  - ConcreteStrategy:        FretePAC, FreteSedex, RetiradaNaLoja
  - Context:                 CalculadoraDeFrete  -> escolhe a estratégia pelo
                                                    tipo e delega o cálculo
"""
from abc import ABC, abstractmethod


# ---------- Strategy ----------
class EstrategiaDeFrete(ABC):
    @abstractmethod
    def calcular(self, peso_kg):
        """Retorna o valor do frete para o peso informado."""


# ---------- ConcreteStrategies ----------
class FretePAC(EstrategiaDeFrete):
    def calcular(self, peso_kg):
        return 10.00 + 2.00 * peso_kg


class FreteSedex(EstrategiaDeFrete):
    def calcular(self, peso_kg):
        return 20.00 + 4.00 * peso_kg


class RetiradaNaLoja(EstrategiaDeFrete):
    def calcular(self, peso_kg):
        return 0.00


# ---------- Context ----------
class CalculadoraDeFrete:
    def __init__(self):
        self._estrategias = {
            "PAC": FretePAC(),
            "SEDEX": FreteSedex(),
            "RETIRADA": RetiradaNaLoja(),
        }

    def calcular(self, tipo, peso_kg):
        estrategia = self._estrategias.get(tipo)
        if estrategia is None:
            raise ValueError(f"Tipo de entrega desconhecido: {tipo}")
        return estrategia.calcular(peso_kg)


def calcular_frete(tipo, peso_kg):
    """Mantém a interface usada pelos testes (comportamento inalterado)."""
    return CalculadoraDeFrete().calcular(tipo, peso_kg)


# =====================================================================
# AUTOAVALIAÇÃO (Passo 3)
# =====================================================================
# Critérios atingidos:
#  1. Testes em arquivo separado (test_frete.py), com um teste para cada
#     uma das 3 variações (PAC, SEDEX, retirada) + 1 caso de erro. ATINGIDO.
#  2. Três commits, um por fase: red, green e refactor. ATINGIDO.
#  3. O commit red contém só os testes, sem a implementação. ATINGIDO.
#  4. Padrão Strategy aplicado e nomeado em comentário, com participantes
#     nomeados conforme o domínio. ATINGIDO.
#  5. Suíte passa após a refatoração; saída em resultado_testes.txt.
#     ATINGIDO.
# Critérios não atingidos: nenhum.
#
# O que mudou na estrutura entre verde e refatorada:
#  Na fase verde havia uma única função com if/elif/else. Na refatorada, cada
#  modalidade virou uma classe (FretePAC, FreteSedex, RetiradaNaLoja) que
#  implementa EstrategiaDeFrete, e CalculadoraDeFrete escolhe a estratégia
#  por um dicionário. Os testes não foram alterados.
#
# Parte que deu mais trabalho:
#  Decidir como manter a função calcular_frete() para os testes continuarem
#  iguais sem duplicar a lógica de escolha da estratégia.
#
# Uso de IA:
#  Ajudou: sugeriu o tema simples e a estrutura dos três commits.
#  Atrapalhou: nada relevante; foi preciso conferir manualmente os valores
#  esperados dos testes.
# =====================================================================
