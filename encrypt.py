# rsa_encrypt.py
import random
import math

# --- Các hàm phụ trợ ---

def is_prime(num):
    """Kiểm tra xem một số có phải là số nguyên tố không."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime(min_val=100, max_val=10**9):
    """Sinh một số nguyên tố ngẫu nhiên trong khoảng [min_val, max_val]."""
    prime = random.randint(min_val, max_val)
    while not is_prime(prime):
        prime = random.randint(min_val, max_val)
    return prime

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modInverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def pow_mod(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

# --- Tạo khoá RSA ---

# 1. Sinh p và q ngẫu nhiên
p = generate_prime()
q = generate_prime()
# Đảm bảo p và q khác nhau
while p == q:
    q = generate_prime()

print(f"Số nguyên tố p = {p}")
print(f"Số nguyên tố q = {q}")

# 2. Tính n và phi(n)
n = p * q
phi = (p - 1) * (q - 1)
print(f"Modulus n = p * q = {n}")
print(f"Phi(n) = (p-1)*(q-1) = {phi}")

# 3. Chọn số mũ công khai e
# e thường là một số nguyên tố nhỏ, phổ biến là 65537
e = 65537
# Kiểm tra nếu gcd(e, phi) != 1 hoặc e >= phi, chọn e khác
if gcd(e, phi) != 1 or e >= phi:
     # Tìm e khác nhỏ nhất > 1 và nguyên tố cùng nhau với phi
    e = 3
    while gcd(e, phi) != 1:
       e += 2 # Chỉ cần kiểm tra các số lẻ > 2

print(f"Số mũ công khai e = {e}")

# 4. Tính số mũ bí mật d
d = modInverse(e, phi)
print(f"Số mũ bí mật d = {d}")
print("-" * 20)

# --- Mã hoá thông điệp ---
message = input("Nhập thông điệp cần mã hoá: ")

# Chuyển đổi từng ký tự thành số (mã ASCII)
message_encoded = [ord(char) for char in message]
print(f"Thông điệp dạng số (ASCII): {message_encoded}")

# Kiểm tra xem có mã ASCII nào lớn hơn hoặc bằng n không
# (Trong trường hợp p, q nhỏ, điều này có thể xảy ra)
for m_val in message_encoded:
    if m_val >= n:
        print(f"\nLỗi: Ký tự '{chr(m_val)}' (mã {m_val}) lớn hơn hoặc bằng n ({n}).")
        print("Hãy thử chạy lại chương trình để tạo p, q lớn hơn.")
        exit() # Thoát chương trình nếu có lỗi

# Mã hoá từng số
encrypted_message = [pow_mod(m, e, n) for m in message_encoded]

print("-" * 20)
print("--- KẾT QUẢ MÃ HOÁ ---")
print(f"Các tham số RSA:")
print(f"  p = {p}")
print(f"  q = {q}")
print(f"  n (modulus) = {n}")
print(f"  phi(n) = {phi}")
print(f"  e (public exponent) = {e}")
print(f"  d (private exponent) = {d}")
print(f"\nThông điệp gốc: {message}")
print(f"Thông điệp đã mã hoá : {encrypted_message}")
