from hebill.html import Document
from http.server import BaseHTTPRequestHandler, HTTPServer

doc = Document()

wrap = doc.html.body.middle.create.component.container()
alert = wrap.create.component.alert('你好！')
alert.color.set_danger()

table = wrap.create.component.table()
table.set_bordered()

alert.set_toggle_target_by_id(table, True)
btn = wrap.create.component.button('点击')
btn.color.set_primary()
btn.set_toggle_target_by_id(table, True)


table.head.add_row(['ID', '姓名', '年龄', '职位'])

table.body.add_row(['1', '张三', '18', '总监'])
table.body.add_row(['2', '李四', '18', '总监'])
table.body.add_row(['3', '王二', '18', '总监'])

table.body.add_row(['4', '麻一', '18', '总监'])

breadcrumb = wrap.create.component.breadcrumb()
breadcrumb.set_divider('>')
breadcrumb.add_item('Home')
breadcrumb.add_item('Library')
breadcrumb.add_item('Data', "", True)

pagination = wrap.create.component.pagination()
pagination.add_item('Home')
pagination.add_item('Library')
pagination.add_item('Data', "", True)
pagination.size.set_small()


# 定义一个处理HTTP请求的处理程序
class MyHandler(BaseHTTPRequestHandler):
    # 处理GET请求
    # noinspection PyPep8Naming
    def do_GET(self):
        self.send_response(200)  # 发送HTTP响应码200，表示成功
        self.send_header('Content-type', 'text/html')  # 发送响应头，指定内容类型为HTML
        self.end_headers()  # 结束响应头的发送
        # 发送响应内容
        self.wfile.write(doc.output().encode('utf-8'))


# 主函数，用于启动服务器
def main():
    host = 'localhost'  # 主机名
    port = 1080  # 端口号

    # 创建HTTP服务器对象，并指定请求处理程序
    server = HTTPServer((host, port), MyHandler)
    print(f"Server started on http://{host}:{port}")

    try:
        # 启动服务器，一直运行直到手动停止或程序异常退出
        server.serve_forever()
    except KeyboardInterrupt as e:
        # 捕获键盘中断信号（Ctrl+C），停止服务器
        print(f"\n Server stopped. {e}")
        server.shutdown()
    except ConnectionAbortedError as e:
        print(f"\n Client interrupted. {e}")
    except Exception as e:
        print(f"\n Unknown error. {e}")


if __name__ == "__main__":
    main()
