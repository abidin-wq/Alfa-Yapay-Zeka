import hashlib

def initialize_security():
    """
    Güvenlik katmanlarını başlatır.
    """
    print("Sistem güvenliği başlatıldı.")
    # Örnek: Şifreleme anahtarını oluştur
    key = hashlib.sha256(b"secure_key").hexdigest()
    print(f"Şifreleme Anahtarı: {key}")
