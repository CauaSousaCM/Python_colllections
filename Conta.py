class Conta:
    def __init__(self, codigo) -> None:
        self.__codigo = codigo
        self.__saldo = 0
        
    def deposita(self, valor) -> None:
        self.__saldo += valor
    
    def __str__(self) -> str:
        return (
            f"[>>Codigo {self.__codigo} "\
            f"Saldo {self.__saldo}<<]"
        )
        