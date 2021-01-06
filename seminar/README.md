<h1> Nhóm N008 </h1>
<h2> Các thành viên: </h2>
<p><b> Hồ Chung Đức Khánh </b><br> 
MSSV: <i>19520624</i></p>
<p><b> Võ Minh Hiếu </b><br> 
MSSV: <i>19520084</i></p>
<p><b> Nguyễn Minh Huy </b><br> 
MSSV: <i>19520109</i></p>

<h2> Các câu hỏi: <br> </h2>
<h4> 1. Phân biệt DFS và BFS? </h4>
Trả lời: 
<br>
BFS và DFS khác nhau ở thứ tự duyệt cây, cụ thể là thứ tự duyệt các nhánh của lời giải cho bài toán này. 
Trong các trường hợp khác nhau thì 2 thuật toán có thể có tốc độ khác nhau, tuy nhiên tính theo trung bình thì độ hiệu quả của cả hai là như nhau.
Ở đây nhóm em áp dụng DFS vì ưu điểm dễ cài đặt dễ debug.
<br> <br>
<h4> 2. Trong cây Fenwick, tại sao phải nén số? </h4>
Trả lời: 
<br>
Vì để trả lời các truy vấn tìm max trong công thức quy hoạch động, cần phải dựng một cây Fenwick/cây phân đoạn với index là giá trị của các phần tử trong dãy A. 
Tuy nhiên các phần tử trong dãy A có thể chứa số rất lớn nên phải tìm cách nén chúng lại mà vẫn đảm bảo thứ tự lớn bé.
<br> <br>
<h4> 3. Tại sao xài Fenwick Tree? </h4>
Trả lời: 
<br>
Đầu tiên, ví dụ mà nhóm chúng em đưa ra nhằm để show mọi người cách Computational Thinking được áp dụng vào việc giải quyết các bài toán.
Cụ thể, thông qua các bước Decomposition và Pattern Recognition, chúng ta có thể đi tới lời giải quy hoạch động một cách tự nhiên, 
sau đó tiếp tục đặt vấn đề tối ưu truy vấn tìm max và tìm cách giải quyết bằng cây Fenwick, cuối cùng là hoàn thiện lời giải bằng kỹ thuật nén số.
<br> <br>
Thứ hai, lí do nhóm em không giới thiệu cây phân đoạn mà lại đề cập đến cây Fenwick là vì đây là một cấu trúc dữ liệu rất thú vị,
cấu trúc dữ liệu này cho chúng ta biết thêm nhiều điều mới mẻ về các phép thao tác bit. 
<br>
Ngoài ra còn một lưu ý khác rất quan trọng: nếu áp dụng đúng trường hợp và bài toán, mà cụ thể là bài toán này, cây Fenwick tiết kiệm bộ nhớ gấp 4 lần so với cây phân đoạn!
Điều này cho thấy rằng việc khéo léo lựa chọn giải thuật và cấu trúc dữ liệu hợp lí ảnh hưởng rất nhiều đến độ hiệu quả của một lời giải.
<br>

