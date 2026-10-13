# 制作归档分块

制作 ZIP 由于上传连接器的单次通信大小限制分成四块。制作素材也已完整展开在仓库 `work/` 中，预览动画无需合并。

下载整个仓库后，在根目录运行：

```bash
python tools/join_production_archive.py
```

脚本使用 Python 标准库，逐块验证 SHA-256 后生成 `outputs/shuangxu-production-files.zip`。分块不可单独解压。完整字节数和校验值见 `manifest.json`。
