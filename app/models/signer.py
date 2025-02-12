class Signer:
    name: str
    email: str
    private_key: bytes | None
    certificate: bytes | None
    
    def __init__(self, name,email, private_key, cert_pem = None):
        self.name = name
        self.email = email
        self.private_key = private_key
        self.certificate = cert_pem
    
    def get_certificate(self):
        return self.certificate
    
    def get_private_key(self):
        return self.private_key