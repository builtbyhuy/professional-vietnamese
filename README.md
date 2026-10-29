# Professional Vietnamese

**Bộ skill giúp AI viết, dịch và rà soát tiếng Việt cho công việc.** Từ một yêu cầu ngắn, agent chọn workflow phù hợp với người đọc, giữ nguyên dữ kiện và giao bản có thể sử dụng.

Ví dụ: nhờ nhà cung cấp xác nhận lịch giao khi đơn hàng *có thể* chậm. Bộ skill giúp soạn email lịch sự, giữ đúng mức độ chưa chắc chắn và không tự hứa ngày giao mới.

## Bắt đầu nhanh

1. Tải hoặc clone repo này về máy.
2. Cài các skill vào Codex bằng Python 3:

   ```bash
   python scripts/install.py --dry-run
   python scripts/install.py
   ```

   Mặc định cài vào `~/.codex/skills`. Trên Windows, có thể dùng `py` thay cho `python`. Nếu một skill cùng tên đã tồn tại, trình cài **dừng trước khi ghi**; chọn thư mục khác bằng `--target` hoặc tự đối chiếu và cài từng skill. Không cần cài gói Python bên ngoài.

3. Mở phiên agent mới và thử:

   ```text
   Dùng $vietnamese-business-email viết email hỏi nhà cung cấp xác nhận lịch giao PO-473. Họ báo có thể trễ 5 ngày và chưa xác nhận ngày mới.
   ```

Các agent khác có thể dùng các thư mục `skills/` nếu hỗ trợ định dạng Agent Skills; vị trí cài phụ thuộc từng môi trường. Repo có manifest Codex tại `.codex-plugin/plugin.json`; cách cài plugin qua giao diện hoặc marketplace phụ thuộc môi trường và chưa được kiểm thử trong repo này. Cài thư mục skill như trên là đường đã được hỗ trợ bởi trình cài của repo.

## Chọn skill

| Khi cần | Skill | Kết quả |
| --- | --- | --- |
| Viết tiếng Việt công việc nói chung | [`professional-vietnamese`](skills/professional-vietnamese/SKILL.md) | Tổ chức ý, chọn ngữ vực và câu chữ theo ngữ cảnh |
| Rà bản thảo | [`vietnamese-writing-audit`](skills/vietnamese-writing-audit/SKILL.md) | Chỉ ra lỗi có tác động, dẫn chứng và gợi ý sửa |
| Viết email | [`vietnamese-business-email`](skills/vietnamese-business-email/SKILL.md) | Email và tiêu đề, phù hợp người nhận và mục đích |
| Soạn tin nhắn | [`vietnamese-work-chat`](skills/vietnamese-work-chat/SKILL.md) | Bản nháp ngắn, xưng hô theo quan hệ |
| Viết báo cáo quản trị | [`vietnamese-management-report`](skills/vietnamese-management-report/SKILL.md) | Kết luận gắn với số liệu, kỳ và giới hạn |
| Dịch hoặc viết lại | [`vietnamese-translation-rewrite`](skills/vietnamese-translation-rewrite/SKILL.md) | Tiếng Việt tự nhiên, giữ ý và điều kiện gốc |

Agent có thể chọn skill theo mô tả hoặc người dùng gọi trực tiếp bằng `$tên-skill` nếu môi trường hỗ trợ. Hành vi tự chọn không được bảo đảm giống nhau giữa các agent. Xem [workflow](docs/workflow.md) để phối hợp các bước mà không áp một quy trình dài cho mọi yêu cầu.

## Ví dụ yêu cầu

- “Audit đoạn này, chỉ ra lỗi ảnh hưởng đến cách hiểu và gợi ý sửa: …”
- “Viết báo cáo ngắn cho giám đốc từ số liệu này, nêu rõ phần chưa xác nhận: …”
- “Dịch đoạn này sang tiếng Việt tự nhiên, giữ nguyên các điều kiện và con số: …”
- “Soạn tin nhắn hỏi đồng nghiệp xác nhận số điều chỉnh **-840.000 đồng**; xưng em–chị.”

## Kiểm tra và giới hạn

[Tình huống đánh giá](docs/evaluation.md) có đầu vào và tiêu chí để thử có/không có skill. Thử nghiệm nhỏ trước đây chưa chứng minh cải thiện ổn định; các skill bổ sung cần được đánh giá tiếp. Đây là hướng dẫn cho mô hình, không phải công cụ xác minh sự thật, bảo đảm văn phong hay tự động gửi tin. Kiểm tra số liệu và bản cuối trước khi sử dụng.

## Đóng góp và giấy phép

Có thể báo lỗi bằng một ví dụ đã loại bỏ dữ liệu riêng tư, kết quả thực tế, kết quả mong muốn và môi trường chạy. Xem [hướng dẫn đóng góp](CONTRIBUTING.md). Giấy phép [MIT](LICENSE).
