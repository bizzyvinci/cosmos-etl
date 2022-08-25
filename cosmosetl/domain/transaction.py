class CosmTransaction:
    def __init__(self):
        self.hash = None
        self.height = None
        self.index = None
        self.code = None
        self.gas_used = None
        self.gas_wanted = None
        self.num_events = None
        self.root_hash = None
        self.tx = None
        self.data = None
        self.raw_data = None
        self.raw_log = None
        self.events = []
