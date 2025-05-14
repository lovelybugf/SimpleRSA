# rsa_decrypt_no_exceptions.py
import ast # Để chuyển đổi chuỗi danh sách thành danh sách

# --- Hàm phụ trợ ---

def pow_mod(base, exponent, modulus):
    """Tính (base^exponent) % modulus một cách hiệu quả."""
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

# --- Giải mã thông điệp ---

# 1. Nhập thông điệp đã mã hoá
# Cảnh báo: Không có kiểm tra lỗi, nếu nhập sai định dạng chương trình sẽ crash.
encrypted_message_str = input("Nhập thông điệp đã mã hoá (dạng danh sách số, ví dụ: [123, 456, 789]): ")
# Chuyển đổi chuỗi nhập vào thành một list các số nguyên
encrypted_message = ast.literal_eval(encrypted_message_str)

# 2. Nhập khoá bí mật (n và d)
# Cảnh báo: Không có kiểm tra lỗi, nếu nhập không phải số chương trình sẽ crash.
n_str = input("Nhập giá trị n (modulus): ")
n = int(n_str)
d_str = input("Nhập giá trị d (private exponent): ")
d = int(d_str)

# 3. Giải mã từng số
decrypted_codes = [pow_mod(c, d, n) for c in encrypted_message]

# 4. Chuyển đổi mã số thành ký tự
# Cảnh báo: Không có kiểm tra lỗi, nếu mã giải mã không hợp lệ chương trình sẽ crash.
decrypted_message = "".join([chr(code) for code in decrypted_codes])


print("-" * 20)
print("--- KẾT QUẢ GIẢI MÃ ---")
print(f"Thông điệp mã hoá đã nhập: {encrypted_message}")
print(f"Khoá bí mật sử dụng: (n={n}, d={d})")
print(f"Thông điệp đã giải mã: {decrypted_message}")

