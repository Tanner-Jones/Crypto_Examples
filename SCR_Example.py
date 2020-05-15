import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes


# This module is to demonstrate a self-signed certificate. These can be used locally when you know everyone
# who will be interacting with one another and a certificate authority is not necessary. Additionally, normal
# certificates cost money so self-signed certificates can operate as placeholders during testing.
# The procedure for obtaining a normal certificate will look very much like this.


# Generate our key
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)



# Various details about who we are. For a self-signed certificate the
# subject and issuer are always the same.
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Colorado"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"Fort Collins"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Colorado State University"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"IoTDevice.com"),
])
cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    # Our certificate will be valid for 10 days
    datetime.datetime.utcnow() + datetime.timedelta(days=10)
).add_extension(
    x509.SubjectAlternativeName([x509.DNSName(u"localhost")]),
    critical=False,
# Sign our certificate with our private key
).sign(key, hashes.SHA256(), default_backend())

# This is where you would normally store a certificate like on a crypto chip or to some other memory.

