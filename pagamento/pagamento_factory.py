from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPIX

class PagamentoFactory:

    @staticmethod
    def criar_pagamento(tipo_pagamento):
        if tipo_pagamento == "cartao":
            return PagamentoCartao()
        elif tipo_pagamento == "pix":
            return PagamentoPIX()
        else:
            raise ValueError(f"Tipo de pagamento '{tipo_pagamento}' inválido.")