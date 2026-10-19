"""把 index.html 引用的 shots-web/*.jpg 內嵌成 base64，輸出可單獨帶走的 簡報-單檔.html。

用法：python3 build.py
"""
import base64
import pathlib
import re

here = pathlib.Path(__file__).parent
src = (here / "index.html").read_text(encoding="utf-8")


def embed(m):
    path = here / m.group(1)
    data = base64.b64encode(path.read_bytes()).decode()
    return f'src="data:image/jpeg;base64,{data}"'


out = re.sub(r'src="(shots-web/[^"]+\.jpg)"', embed, src)
(here / "簡報-單檔.html").write_text(out, encoding="utf-8")
print(f"簡報-單檔.html：{len(out) / 1024 / 1024:.1f} MB")
