import tkinter as tk

# Khởi tạo cửa sổ
root = tk.Tk()
root.title("Calculator")

# KHAI BÁO BIẾN HIỂN THỊ
equation = tk.StringVar()
equation.set("0") # Thiết lập giá trị ban đầu

# TẠO MÀN HÌNH HIỂN THỊ (ENTRY)
display_entry = tk.Entry(
    root,
    textvariable=equation,
    font=('Arial', 20),
    bd=10,
    relief=tk.SUNKEN,
    justify=tk.RIGHT
)
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# =================================================================
# 2. ĐỊNH NGHĨA HÀM XỬ LÝ SỰ KIỆN (Commands)
# =================================================================

# Hàm này sẽ được gọi khi bấm số hoặc phép toán
def click_button(item):
    """Thêm ký tự vào biểu thức hiện tại."""
    # Logic chi tiết sẽ được viết sau, hiện tại chỉ là placeholder
    current = equation.get()
    if current == "0":
        equation.set(str(item))
    else:
        equation.set(current + str(item))

# Hàm xóa toàn bộ (C)
def clear():
    """Xóa toàn bộ biểu thức."""
    equation.set("0")

# Hàm xóa từng ký tự (Del)
def delete_char():
    """Xóa ký tự cuối cùng."""
    current = equation.get()
    if current != "0" and len(current) > 1:
        equation.set(current[:-1])
    else:
        equation.set("0")

# Hàm tính toán (=)
def calculate():
    """Tính toán kết quả."""
    # Logic chi tiết sẽ được viết sau
    try:
        result = str(eval(equation.get()))
        equation.set(result)
    except:
        equation.set("Error")

# =================================================================
# 3. TẠO VÀ BỐ CỤC CÁC NÚT BẤM (GRID Layout)
# =================================================================

# Danh sách các nút và vị trí của chúng (text, row, column, command)
buttons = [
    # Hàng 1 (Chức năng)
    ('C', 1, 0, clear),
    ('Del', 1, 1, delete_char),
    ('/', 1, 2, lambda: click_button('/')),
    ('*', 1, 3, lambda: click_button('*')),
    
    # Hàng 2 (Số 7, 8, 9)
    ('7', 2, 0, lambda: click_button('7')),
    ('8', 2, 1, lambda: click_button('8')),
    ('9', 2, 2, lambda: click_button('9')),
    ('-', 2, 3, lambda: click_button('-')),

    # Hàng 3 (Số 4, 5, 6)
    ('4', 3, 0, lambda: click_button('4')),
    ('5', 3, 1, lambda: click_button('5')),
    ('6', 3, 2, lambda: click_button('6')),
    ('+', 3, 3, lambda: click_button('+')),

    # Hàng 4 (Số 1, 2, 3)
    ('1', 4, 0, lambda: click_button('1')),
    ('2', 4, 1, lambda: click_button('2')),
    ('3', 4, 2, lambda: click_button('3')),
    ('=', 4, 3, calculate), # Nút '='

    # Hàng 5 (Số 0, Dấu chấm)
    ('0', 5, 0, lambda: click_button('0')),
    ('.', 5, 1, lambda: click_button('.')),
    
    # Kéo dài nút 0 qua 2 cột (hoặc tạo thêm nút khác)
    # Nếu muốn nút 0 chiếm 2 cột:
    # ('0', 5, 0, lambda: click_button('0'), 2)
    # Tuy nhiên, theo bố cục chuẩn (4x5), ta có thể cho 0 và . chiếm 1 cột, nút cuối cùng là '='
    # Chúng ta đã đặt '=' ở hàng 4, cột 3, hãy chuyển nó xuống hàng 5 và kéo dài nút 0:
    
    # ĐỊNH NGHĨA LẠI HÀNG CUỐI CHO PHÙ HỢP VỚI BỐ CỤC MÁY TÍNH THÔNG THƯỜNG
    # Bỏ nút '=' ở Hàng 4 đi (đã có ở trên) và dùng 0, ., = ở hàng 5
]

# Tạo vòng lặp để sinh ra các nút
row_pos = 1
col_pos = 0

for (btn_text, row, col, cmd) in buttons:
    # Tùy chỉnh màu sắc cho các loại nút khác nhau
    if btn_text in '/*-+':
        color = 'orange'
    elif btn_text in 'C Del':
        color = 'lightgray'
    elif btn_text == '=':
        color = 'lightblue'
    else:
        color = 'white'
        
    tk.Button(
        root,
        text=btn_text,
        padx=20, # Đệm ngang
        pady=20, # Đệm dọc
        font=('Arial', 14, 'bold'),
        bg=color,
        command=cmd # Gán hàm xử lý cho nút
    ).grid(row=row, column=col, sticky='nsew') # sticky='nsew' để nút lấp đầy ô lưới

# =================================================================
# 4. CẤU HÌNH LƯỚI CHO CÁC HÀNG VÀ CỘT
# =================================================================

# Thiết lập trọng số cho các cột và hàng để chúng tự co giãn khi cửa sổ thay đổi kích thước
# Đây là một bước tùy chọn nhưng được khuyến nghị cho GUI đẹp hơn.
for i in range(4): # 4 cột (0, 1, 2, 3)
    root.grid_columnconfigure(i, weight=1)

for i in range(6): # 6 hàng (0 - màn hình, 1-5 - nút)
    root.grid_rowconfigure(i, weight=1)

# VÒNG LẶP CHÍNH
root.mainloop()

# Khai báo biến điều khiển String (để lưu trữ biểu thức/kết quả)
equation = tk.StringVar()

# Tạo trường nhập liệu (màn hình hiển thị)
display_entry = tk.Entry(
    root,
    textvariable=equation,  # Liên kết nội dung với biến equation
    font=('Arial', 20),
    bd=10,
    relief=tk.SUNKEN,
    justify=tk.RIGHT
)

# Đặt trường nhập liệu ở hàng 0 và trải dài qua 4 cột
# columnspan=4 giúp nó chiếm toàn bộ chiều ngang
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Thiết lập giá trị ban đầu (tùy chọn)
equation.set("0")