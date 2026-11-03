# Security Fix
# Memastikan input pengguna divalidasi sebelum diproses oleh aplikasi.

def validasi_input(teks):
    if not isinstance(teks, str):
        return False
    return len(teks.strip()) > 0