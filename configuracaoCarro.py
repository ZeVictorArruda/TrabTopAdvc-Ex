class ConfiguracaoCarro:
    _instance = None

    def __new__(cls):
        # Aqui é onde o padrão Singleton é aplicado
        if cls._instance is None:
            print("Instância criada.")
            cls._instance = super().__new__(cls)
        else:
            print("Instância já existente.")
        return cls._instance

    def set_configuracao(self, configuracao):
        self.configuracao = configuracao

    def get_configuracao(self):
        return self.configuracao
