# Tuyên Ngôn Độc Lập

Đặt file âm thanh `tuyen-ngon-doc-lap.mp3` vào thư mục này.

## Gợi ý nguồn audio miễn phí (bản đọc gốc 1945)

- **Bản đọc chính thức (Bác Hồ, 2/9/1945)** — bản thu âm trên:
  - VOV (Voice of Vietnam): https://vov.vn
  - Thư viện Quốc gia VN
  - YouTube: tìm kiếm *"Bác Hồ đọc tuyên ngôn độc lập"*

- **Bản hiện đại dễ nghe** (phát thanh viên VOV):
  - Có thể dùng link online dạng:
    `https://example.com/tuyen-ngon-doc-lap.mp3`

## Nếu muốn dùng link online thay vì file local

Sửa trong `index.html`:

```html
<!-- Thay dòng này -->
<audio id="tuyenNgonAudio"
       src="assets/tuyen-ngon-doc-lap.mp3"
       ...></audio>

<!-- Thành link online -->
<audio id="tuyenNgonAudio"
       src="https://your-cdn.com/tuyen-ngon-doc-lap.mp3"
       ...></audio>
```

## Đặc điểm kỹ thuật

- File nên dài **~3-5 phút** (bản đọc gốc)
- Định dạng: **MP3** (hoặc OGG/WAV đều được — trình duyệt tự chọn)
- Bitrate: 128 kbps trở lên (dễ nghe)
- Khi phát: **loop vô hạn**, volume **30%** (đã cấu hình trong code)

## Lưu ý

- Trình duyệt **CHẶN autoplay** — user phải bấm nút loa 🔇 → 🔊 ở góc trên phải để bật
- File không tồn tại → nút loa sẽ tự **ẩn** (không báo lỗi)