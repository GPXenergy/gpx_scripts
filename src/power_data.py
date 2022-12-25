

class PowerData:
    timestamp = ''
    import_1 = 0  # in kWh
    import_2 = 0  # in kWh
    export_1 = 0  # in kWh
    export_2 = 0  # in kWh
    actual_import = 0  # in kW
    actual_export = 0  # in kW
    tariff = 1

    def __init__(self, timestamp, import_1=0, import_2=0, export_1=0, export_2=0, tariff=1, actual_import=0, actual_export=0):
        self.timestamp = timestamp
        self.import_1 = import_1
        self.import_2 = import_2
        self.export_1 = export_1
        self.export_2 = export_2
        self.tariff = tariff
        self.actual_import = actual_import
        self.actual_export = actual_export

    def as_payload(self, sn):
        return {
            'sn': sn,
            'timestamp': self.timestamp,
            'import_1': self.import_1,
            'import_2': self.import_2,
            'export_1': self.export_1,
            'export_2': self.export_2,
            'tariff': self.tariff,
            'actual_import': self.actual_import,
            'actual_export': self.actual_export,
        }
