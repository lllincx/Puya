
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
格式化 Typora/Markdown 中英文混排：

1. 在中文与英文/数字之间加入空格；
2. 按中文语境把英文半角标点转换为中文标点；
3. 跳过代码块、行内代码、URL、邮箱、HTML 标签和数学公式；
4. 处理加粗、斜体、删除线和 Markdown 链接文本；
5. 默认生成新文件，避免覆盖原文。

仅使用 Python 标准库。
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


CJK = r"\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF"
CJK_RE = re.compile(fr"[{CJK}]")
LATIN_OR_DIGIT_RE = re.compile(r"[A-Za-z0-9]")

FENCE_RE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})")
MATH_BLOCK_RE = re.compile(r"^[ \t]*(\$\$|\\\[|\\\])[ \t]*(?:\r?\n)?$")
YAML_BOUNDARY_RE = re.compile(r"^---[ \t]*(?:\r?\n)?$")

INLINE_CODE_RE = re.compile(r"(?<!\\)(`+)(.+?)(?<!`)\1(?!`)")
INLINE_MATH_RE = re.compile(
    r"(?<!\\)(\${1,2})(?!\$)(.+?)(?<!\\)\1(?!\$)"
)
URL_RE = re.compile(
    fr"(?i)\b(?:https?://|ftp://|www\.)"
    fr"[^\s<>(){CJK}]*[^\s<>(){CJK},.;:!?，。；：！？]"
)
EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
HTML_TAG_RE = re.compile(r"</?[A-Za-z][^>\n]*>")
AUTOLINK_RE = re.compile(r"<(?:https?://|mailto:)[^>\n]+>", re.I)

# 支持常见、不含嵌套括号的 Markdown 行内链接。
INLINE_LINK_RE = re.compile(
    r"(?P<image>!)?\[(?P<label>[^\]\n]+)\]"
    r"\((?P<dest>(?:[^()\n\\]|\\.)*)\)"
)
REFERENCE_LINK_RE = re.compile(
    r"(?P<image>!)?\[(?P<label>[^\]\n]+)\]"
    r"\[(?P<ref>[^\]\n]*)\]"
)


@dataclass
class Protected:
    raw: str
    left_kind: str | None = None
    right_kind: str | None = None


class Protector:
    """用 Unicode 私用区单字符占位，防止 Markdown 特殊内容被改写。"""

    START = 0xF0000

    def __init__(self) -> None:
        self.items: dict[str, Protected] = {}

    @staticmethod
    def _kind_from_start(text: str) -> str | None:
        for ch in text:
            if CJK_RE.match(ch):
                return "cjk"
            if ch.isascii() and ch.isalnum():
                return "latin"
        return None

    @staticmethod
    def _kind_from_end(text: str) -> str | None:
        for ch in reversed(text):
            if CJK_RE.match(ch):
                return "cjk"
            if ch.isascii() and ch.isalnum():
                return "latin"
        return None

    def add(
        self,
        raw: str,
        visible_text: str = "",
        *,
        visible: bool = True,
    ) -> str:
        token = chr(self.START + len(self.items))
        if visible:
            item = Protected(
                raw=raw,
                left_kind=self._kind_from_start(visible_text),
                right_kind=self._kind_from_end(visible_text),
            )
        else:
            item = Protected(raw=raw)
        self.items[token] = item
        return token

    def protect_regex(
        self,
        text: str,
        regex: re.Pattern[str],
        visible_getter: Callable[[re.Match[str]], str] | None = None,
        *,
        visible: bool = True,
    ) -> str:
        def repl(match: re.Match[str]) -> str:
            visible_text = (
                visible_getter(match) if visible_getter else match.group(0)
            )
            return self.add(
                match.group(0),
                visible_text,
                visible=visible,
            )

        return regex.sub(repl, text)

    def add_boundary_spaces(self, text: str) -> str:
        """为中文与受保护的英文/数字内容之间补空格，例如中文`code`中文。"""
        for token, item in self.items.items():
            escaped = re.escape(token)

            if item.left_kind == "latin":
                text = re.sub(
                    fr"([{CJK}])(?={escaped})",
                    r"\1 ",
                    text,
                )
            elif item.left_kind == "cjk":
                text = re.sub(
                    fr"([A-Za-z0-9])(?={escaped})",
                    r"\1 ",
                    text,
                )

            if item.right_kind == "latin":
                text = re.sub(
                    fr"(?<={escaped})([{CJK}])",
                    r" \1",
                    text,
                )
            elif item.right_kind == "cjk":
                text = re.sub(
                    fr"(?<={escaped})([A-Za-z0-9])",
                    r" \1",
                    text,
                )

        return text

    def restore(self, text: str) -> str:
        # 后加入的对象可能包含先加入的占位符，所以逆序恢复。
        for token, item in reversed(list(self.items.items())):
            text = text.replace(token, item.raw)
        return text


def add_cjk_latin_spaces(text: str) -> str:
    """处理中英文/数字直接相邻，以及常见 Markdown 强调标记边界。"""
    text = re.sub(
        fr"(?<=[{CJK}])(?=[A-Za-z0-9])",
        " ",
        text,
    )
    text = re.sub(
        fr"(?<=[A-Za-z0-9])(?=[{CJK}])",
        " ",
        text,
    )

    # 中文**English**、中文*English*、中文~~English~~
    marker = r"(?:\*{1,3}|_{1,3}|~~)"
    text = re.sub(
        fr"([{CJK}])(?={marker}[A-Za-z0-9])",
        r"\1 ",
        text,
    )
    text = re.sub(
        fr"([A-Za-z0-9])({marker})(?=[{CJK}])",
        r"\1\2 ",
        text,
    )
    return text


def _nearest_semantic_char(text: str, index: int, step: int) -> str:
    """忽略空白和常见 Markdown 标记，寻找左右语义字符。"""
    ignored = set("*_~[]()")
    i = index + step
    while 0 <= i < len(text):
        ch = text[i]
        if ch.isspace() or ch in ignored:
            i += step
            continue
        return ch
    return ""


def convert_punctuation_smart(text: str) -> str:
    """
    只在中文语境转换半角标点，避免破坏纯英文内容、版本号和小数。
    """
    if not CJK_RE.search(text):
        return text

    chars = list(text)
    source = text

    simple_map = {
        ",": "，",
        ";": "；",
        ":": "：",
        "?": "？",
        "!": "！",
    }

    for i, ch in enumerate(source):
        if ch not in simple_map:
            continue

        prev_ch = source[i - 1] if i > 0 else ""
        next_ch = source[i + 1] if i + 1 < len(source) else ""

        # 保留 1,000 和 12:30 等数字内部格式。
        if ch in {",", ":"} and prev_ch.isdigit() and next_ch.isdigit():
            continue

        # 只要当前文本行包含中文，正文中的这些半角标点统一中文化。
        chars[i] = simple_map[ch]

    text = "".join(chars)

    # 三个英文句点转中文省略号。
    text = re.sub(r"(?<!\.)\.\.\.(?!\.)", "……", text)

    # 句号：不处理 3.14、v1.2.3；中文段落中的句末英文句点可以转换。
    chars = list(text)
    for i, ch in enumerate(text):
        if ch != ".":
            continue
        prev_ch = text[i - 1] if i > 0 else ""
        next_ch = text[i + 1] if i + 1 < len(text) else ""
        if prev_ch.isdigit() and next_ch.isdigit():
            continue

        left = _nearest_semantic_char(text, i, -1)
        right = _nearest_semantic_char(text, i, 1)
        at_line_end = not right or right in "\r\n"

        if (left and CJK_RE.match(left)) or (
            at_line_end and CJK_RE.search(text[:i])
        ):
            chars[i] = "。"
    text = "".join(chars)

    # 中文行中的成对半角括号统一转为全角括号，例如：模型(AI)。
    text = re.sub(
        r"\(([^()\n]*)\)",
        r"（\1）",
        text,
    )

    # 中文行中的成对直引号。
    text = re.sub(
        r'"([^"\n]+)"',
        r"“\1”",
        text,
    )
    text = re.sub(
        r"(?<![A-Za-z])'([^'\n]+)'(?![A-Za-z])",
        r"‘\1’",
        text,
    )

    return text


def convert_punctuation_all(text: str) -> str:
    """
    较激进模式：正文中的半角标点全部中文化；
    仍保留数字之间的小数点。
    """
    text = text.translate(
        str.maketrans(
            {
                ",": "，",
                ";": "；",
                ":": "：",
                "?": "？",
                "!": "！",
                "(": "（",
                ")": "）",
            }
        )
    )
    text = re.sub(r"(?<!\.)\.\.\.(?!\.)", "……", text)
    text = re.sub(r"(?<!\d)\.(?!\d)", "。", text)

    # 只转换成对引号；英文缩写中的单引号不处理。
    text = re.sub(r'"([^"\n]+)"', r"“\1”", text)
    text = re.sub(
        r"(?<![A-Za-z])'([^'\n]+)'(?![A-Za-z])",
        r"‘\1’",
        text,
    )
    return text


def format_inline_text(text: str, punctuation: str) -> str:
    protector = Protector()

    # 1. 先保护行内代码和数学公式。
    text = protector.protect_regex(
        text,
        INLINE_CODE_RE,
        visible_getter=lambda m: m.group(2),
    )
    text = protector.protect_regex(
        text,
        INLINE_MATH_RE,
        visible_getter=lambda m: m.group(2),
    )

    # 2. Markdown 链接：格式化显示文字，保护 URL/引用标识。
    def inline_link_repl(match: re.Match[str]) -> str:
        is_image = bool(match.group("image"))
        label = format_inline_text(match.group("label"), punctuation)
        raw = (
            ("!" if is_image else "")
            + "["
            + label
            + "]("
            + match.group("dest")
            + ")"
        )
        return protector.add(
            raw,
            label,
            visible=not is_image,
        )

    text = INLINE_LINK_RE.sub(inline_link_repl, text)

    def reference_link_repl(match: re.Match[str]) -> str:
        is_image = bool(match.group("image"))
        label = format_inline_text(match.group("label"), punctuation)
        raw = (
            ("!" if is_image else "")
            + "["
            + label
            + "]["
            + match.group("ref")
            + "]"
        )
        return protector.add(
            raw,
            label,
            visible=not is_image,
        )

    text = REFERENCE_LINK_RE.sub(reference_link_repl, text)

    # 3. 保护其余不应改写的内容。
    text = protector.protect_regex(text, AUTOLINK_RE)
    text = protector.protect_regex(text, URL_RE)
    text = protector.protect_regex(text, EMAIL_RE)
    text = protector.protect_regex(text, HTML_TAG_RE, visible=False)

    # 4. 正文格式化。
    text = add_cjk_latin_spaces(text)

    if punctuation == "smart":
        text = convert_punctuation_smart(text)
    elif punctuation == "all":
        text = convert_punctuation_all(text)

    # 5. 为中文与行内代码、链接、URL 等受保护对象补空格。
    text = protector.add_boundary_spaces(text)
    return protector.restore(text)


def format_markdown(content: str, punctuation: str = "smart") -> str:
    lines = content.splitlines(keepends=True)
    output: list[str] = []

    in_fence = False
    fence_char = ""
    fence_len = 0
    in_math_block = False
    in_yaml = False

    for line_no, line in enumerate(lines):
        # 文件顶部 YAML Front Matter 原样保留。
        if line_no == 0 and YAML_BOUNDARY_RE.match(line):
            in_yaml = True
            output.append(line)
            continue

        if in_yaml:
            output.append(line)
            if YAML_BOUNDARY_RE.match(line):
                in_yaml = False
            continue

        fence_match = FENCE_RE.match(line)
        if fence_match:
            marker = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_char = marker[0]
                fence_len = len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_len:
                in_fence = False
                fence_char = ""
                fence_len = 0
            output.append(line)
            continue

        if in_fence:
            output.append(line)
            continue

        if MATH_BLOCK_RE.match(line):
            in_math_block = not in_math_block
            output.append(line)
            continue

        if in_math_block:
            output.append(line)
            continue

        # Markdown 链接引用定义的目标地址原样保留，只格式化可选标题之前的文本没有必要。
        if re.match(r"^[ \t]{0,3}\[[^\]]+\]:[ \t]*\S+", line):
            output.append(line)
            continue

        output.append(format_inline_text(line, punctuation))

    return "".join(output)


def read_text_preserve_bom(path: Path) -> tuple[str, bool]:
    raw = path.read_bytes()
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    encoding = "utf-8-sig" if has_bom else "utf-8"
    return raw.decode(encoding), has_bom


def write_text_preserve_bom(path: Path, text: str, has_bom: bool) -> None:
    data = text.encode("utf-8")
    if has_bom:
        data = b"\xef\xbb\xbf" + data
    path.write_bytes(data)


def default_output_path(input_path: Path) -> Path:
    return input_path.with_name(
        f"{input_path.stem}.formatted{input_path.suffix}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="格式化 Typora/Markdown 中英文混排。"
    )
    parser.add_argument("input", type=Path, help="输入 .md 文件")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="输出文件；默认是 xxx.formatted.md",
    )
    parser.add_argument(
        "-i",
        "--in-place",
        action="store_true",
        help="直接覆盖原文件",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="覆盖原文件时创建 .bak 备份",
    )
    parser.add_argument(
        "--punctuation",
        choices=("smart", "all", "off"),
        default="smart",
        help="标点转换：smart=仅中文语境；all=正文全部；off=不转换",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path: Path = args.input

    if not input_path.is_file():
        print(f"错误：文件不存在：{input_path}", file=sys.stderr)
        return 2

    if args.in_place and args.output:
        print("错误：--in-place 与 --output 不能同时使用。", file=sys.stderr)
        return 2

    output_path = (
        input_path
        if args.in_place
        else (args.output or default_output_path(input_path))
    )

    try:
        content, has_bom = read_text_preserve_bom(input_path)
        formatted = format_markdown(
            content,
            punctuation=args.punctuation,
        )

        if args.in_place and args.backup:
            backup_path = input_path.with_suffix(input_path.suffix + ".bak")
            shutil.copy2(input_path, backup_path)
            print(f"已创建备份：{backup_path}")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        write_text_preserve_bom(output_path, formatted, has_bom)
        print(f"处理完成：{output_path}")
        return 0

    except UnicodeDecodeError:
        print(
            "错误：输入文件不是 UTF-8 编码，请先在 Typora 中另存为 UTF-8。",
            file=sys.stderr,
        )
        return 3
    except OSError as exc:
        print(f"错误：{exc}", file=sys.stderr)
        return 4


if __name__ == "__main__":
    raise SystemExit(main())
