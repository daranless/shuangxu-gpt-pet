# 霜序：离线使用说明

目录、规格与制作说明见根目录 [README.md](README.md)。

## 打开动画

下载并解压整个仓库后，双击 `index.html`，用 Edge、Chrome 或其他现代浏览器打开。无需安装 Python、Node.js，无需联网或 API Key。

- 点击九个动作按钮切换动画。
- 点击“暂停”停在当前帧，点击“播放”继续。
- 使用“方向”选择视线角度，或点击“视线循环”。
- 使用“大小”调整显示比例。
- 下方可播放 MP4，或打开 GIF 和透明 PNG。

如果 HTML 被编辑器打开，右键选择“打开方式”，再选浏览器。请保持 `index.html` 和 `outputs/` 的相对位置。

## 应用内使用

最终文件是 `outputs/shuangxu-spritesheet.png`。它是十一行 v2 透明精灵表，1536 × 2288 像素，每格 192 × 208 像素。

在支持这个格式的 Pets 流程中上传并验证最终 PNG，再按工具步骤创建和选用。下载仓库不会自动安装宠物，个人账号的宠物 ID 和选用状态也不会随文件分发。

状态文件只记录制作时的历史状态。需要九行格式的入口不能直接接受十一行图；不要拉伸或随意覆盖应用内部文件。

## 修改与复查

日常预览不需要执行 `work/` 或 `tools/` 中的脚本。源素材、提示词、帧和记录已保存，可用于研究制作流程。

仅复查结构时，安装 Python 3.10+ 和 Pillow，在根目录执行：

```bash
python -m pip install Pillow
python tools/work-pets/skills/create-pet/scripts/validate_atlas.py outputs/shuangxu-spritesheet.png --require-v2 --chroma-key "#00FF00" --json-out archive/validation-local.json
```

归一化脚本会改写帧，不是启动脚本。重新生成 MP4 需要 `ffmpeg`，新图像生成需要单独的生成工具。

播放器仅展示精灵动画。语音对话、GPT 接口、Live2D 或 VRM 角色属于后续独立开发工作。
