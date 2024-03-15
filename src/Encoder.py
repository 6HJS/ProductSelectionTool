import Item

class Encoder(Item):
    def __init__(self, type, model_num, mech_design, comm_interf, connect_type):
        super().__init__(type, model_num)
        self.mech_design = mech_design
        self.comm_interf = comm_interf
        self.connect_type = connect_type
    
    @classmethod
    def get_mech_design(self):
        return self.mech_design
    
    @classmethod
    def set_mech_design(self, mech_design):
        self.mech_design = mech_design
    
    @classmethod
    def get_comm_interf(self):
        return self.comm_interf
    
    @classmethod
    def set_comm_interf(self, comm_interf):
        self.comm_interf = comm_interf
        
    @classmethod
    def get_connect_type(self):
        return self.connect_type
    
    @classmethod
    def set_connect_type(self, connect_type):
        self.connect_type = connect_type

class Increment_Encoder(Encoder):
    def __init__(self, type, model_num, mech_design, comm_interf, connect_type, pulse_per_revo):
        super().__init__(type, model_num, mech_design, comm_interf, connect_type)
        self.pulse_per_revo = pulse_per_revo
    
    @classmethod
    def get_pulse_per_revo(self):
        return self.pulse_per_revo
    
    @classmethod
    def set_pulse_per_revo(self, pulse_per_revo):
        self.pulse_per_revo = pulse_per_revo

class Abs_encoder(Encoder):
    def __init__(self, type, model_num, mech_design, comm_interf, connect_type, version, max_resol, prog_interf):
        super().__init__(type, model_num, mech_design, comm_interf, connect_type)
        self.version = version
        self.max_resol = max_resol
        self.prog_interf = prog_interf
    
    @classmethod
    def get_version(self):
        return self.version
    
    @classmethod
    def set_version(self, version):
        self.version = version
        
    @classmethod
    def get_max_resol(self):
        return self.max_resol
    
    @classmethod
    def set_max_resol(self, max_resol):
        self.max_resol = max_resol
        
    @classmethod
    def get_prog_interf(self):
        return self.prog_interf
    
    @classmethod
    def set_prog_interf(self, prog_interf):
        self.prog_interf = prog_interf