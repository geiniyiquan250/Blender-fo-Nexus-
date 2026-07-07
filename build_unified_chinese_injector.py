from __future__ import annotations

import base64
import json
import re
import textwrap
import zlib
from pathlib import Path


OUTPUT_NAME = "NeXus中文汉化与文档整合注入工具.pyw"
BASE_TOOL_NAME = "NeXus自包含一键汉化工具.pyw"

DOC_PATCHED_FILES = [
    "operators/modifier_help.py",
    "operators/__init__.py",
    "nxAttract.md",
    "nxAvoid.md",
    "nxBlend.md",
    "nxCache.md",
    "nxCollider.md",
    "nxColor.md",
    "nxConstraints.md",
    "nxCover.md",
    "nxDirection.md",
    "nxDrag.md",
    "nxEmitter.md",
    "nxExplode.md",
    "nxExplosiaFX.md",
    "nxFlock.md",
    "nxFalloff.md",
    "nxFollowGeo.md",
    "nxFluids.md",
    "nxFolder.md",
    "nxGenerator.md",
    "nxGravity.md",
    "nxGroup.md",
    "nxInfectio.md",
    "nxKill.md",
    "nxMesher.md",
    "nxQuestion.md",
    "nxLimit.md",
    "nxPush.md",
    "nxRotate.md",
    "nxSpeed.md",
    "nxScale.md",
    "nxSplash.md",
    "nxSpin.md",
    "nxSticky.md",
    "nxTrail.md",
    "nxTurbulence.md",
    "nxUpres.md",
    "nxVorticity.md",
    "nxWave.md",
    "nxWind.md",
]


def _payload_literal(doc_root: Path) -> str:
    payload = {}
    for rel in DOC_PATCHED_FILES:
        path = doc_root / rel
        if not path.exists():
            raise FileNotFoundError(rel)
        payload[rel] = base64.b64encode(path.read_bytes()).decode("ascii")
    raw = json.dumps(payload, ensure_ascii=True, sort_keys=True).encode("ascii")
    encoded = base64.b64encode(zlib.compress(raw, level=9)).decode("ascii")
    return "\n".join(f'    "{line}"' for line in textwrap.wrap(encoded, 96))


def _insert_after(text: str, marker: str, insertion: str) -> str:
    if marker not in text:
        raise RuntimeError(f"Marker not found: {marker!r}")
    return text.replace(marker, marker + insertion, 1)


def _replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise RuntimeError(f"Block not found: {old[:80]!r}")
    return text.replace(old, new, 1)


def _remove_between(text: str, start: str, end: str) -> str:
    start_idx = text.find(start)
    if start_idx < 0:
        raise RuntimeError(f"Start marker not found: {start!r}")
    end_idx = text.find(end, start_idx)
    if end_idx < 0:
        raise RuntimeError(f"End marker not found after {start!r}: {end!r}")
    return text[:start_idx] + text[end_idx:]


def build() -> Path:
    script_path = Path(__file__).resolve()
    doc_root = script_path.parent
    package_root = script_path.parents[2]
    i18n_root = package_root / "开发源文件" / "i18n_localization_source"
    base_path = i18n_root / BASE_TOOL_NAME
    if not base_path.exists():
        base_path = package_root / "发布工具" / BASE_TOOL_NAME
    output_path = package_root / "发布工具" / OUTPUT_NAME

    source = base_path.read_text(encoding="utf-8-sig")
    payload = _payload_literal(doc_root)

    old_tk_import = "import tkinter as tk\nfrom tkinter import messagebox, scrolledtext\n"
    if old_tk_import in source:
        source = source.replace(
            old_tk_import,
            '''try:
    import tkinter as tk
    from tkinter import messagebox, scrolledtext
except Exception:
    tk = None
    messagebox = None
    scrolledtext = None
''',
            1,
        )
    source = source.replace(
        'LOG_FILE = os.path.join(TOOL_DIR, "NeXus自包含一键汉化工具.log")',
        'LOG_FILE = os.path.join(TOOL_DIR, "NeXus中文汉化与文档整合注入工具.log")',
        1,
    )

    constants = f'''

DOC_BACKUP_SUFFIX = ".dochelp.bak"
DOC_PATCHED_FILES = {json.dumps(DOC_PATCHED_FILES, ensure_ascii=False, indent=4)}

EMBEDDED_DOC_PAYLOAD = (
{payload}
)


def _decode_doc_payload():
    raw = zlib.decompress(base64.b64decode(EMBEDDED_DOC_PAYLOAD)).decode("ascii")
    payload = json.loads(raw)
    return {{rel: base64.b64decode(data) for rel, data in payload.items()}}


def _get_doc_payload():
    if not hasattr(_get_doc_payload, "_cache"):
        _get_doc_payload._cache = _decode_doc_payload()
    return _get_doc_payload._cache


def _file_matches_bytes(path, data):
    try:
        with open(path, "rb") as f:
            return f.read() == data
    except OSError:
        return False
'''
    source, patched_count = re.subn(
        r"PATCHED_SOURCE_FILES = \[[^\n]*\]",
        lambda match: match.group(0) + constants,
        source,
        count=1,
    )
    if patched_count != 1:
        raise RuntimeError("PATCHED_SOURCE_FILES marker not found")
    source = source.replace(
        "for rel in PATCHED_SOURCE_FILES:\n                self.restore_file(rel)",
        "for rel in RESTORE_SOURCE_FILES:\n                self.restore_file(rel)",
        1,
    )

    source = source.replace(
        'self.root.title("NeXus \\u6c49\\u5316\\u81ea\\u52a8\\u6ce8\\u5165\\u5de5\\u5177")',
        'self.root.title("NeXus \\u4e2d\\u6587\\u6c49\\u5316\\u4e0e\\u6587\\u6863\\u6574\\u5408\\u6ce8\\u5165\\u5de5\\u5177")',
        1,
    )
    source = source.replace(
        'tk.Label(header, text="NeXus \\u4e00\\u952e\\u6c49\\u5316\\u8865\\u4e01\\u6ce8\\u5165", font=self.font_title, fg=self.colors["text"], bg=self.colors["panel"]).pack(anchor="center", pady=(24, 8))',
        'tk.Label(header, text="NeXus \\u4e2d\\u6587\\u6c49\\u5316\\u4e0e\\u5e2e\\u52a9\\u6587\\u6863\\u6ce8\\u5165", font=self.font_title, fg=self.colors["text"], bg=self.colors["panel"]).pack(anchor="center", pady=(24, 8))',
        1,
    )
    source = source.replace(
        'meta_line = "\\u7ffb\\u8bd1\\u5b57\\u5178: Shuimeng  |  \\u517c\\u5bb9\\u63d2\\u4ef6\\u7248\\u672c: " + SUPPORTED_PLUGIN_VERSION',
        'meta_line = "\\u7ffb\\u8bd1\\u5b57\\u5178: Shuimeng  |  \\u4e2d\\u6587\\u6587\\u6863\\u4f5c\\u8005: Shuimeng  |  \\u4e2d\\u6587\\u6587\\u6863: " + str(len(DOC_PATCHED_FILES)) + " \\u4e2a\\u6587\\u4ef6  |  \\u517c\\u5bb9\\u63d2\\u4ef6\\u7248\\u672c: " + SUPPORTED_PLUGIN_VERSION',
        1,
    )

    old_buttons = '''        btn_row.grid_columnconfigure(0, weight=1, uniform="actions")
        btn_row.grid_columnconfigure(1, weight=1, uniform="actions")
        btn_row.grid_columnconfigure(2, weight=1, uniform="actions")
        btn_row.grid_columnconfigure(3, weight=1, uniform="actions")
        self.btn_run = self._create_action_button(btn_row, "\\u4e2d\\u6587\\u6c49\\u5316", self.colors["success"], "#16a34a", self.start_patch)
        self.btn_run.grid(row=0, column=0, sticky="ew")
        self.btn_bilingual = self._create_action_button(btn_row, "\\u53cc\\u8bed\\u6c49\\u5316", self.colors["info"], "#3b82f6", self.start_bilingual)
        self.btn_bilingual.grid(row=0, column=1, sticky="ew", padx=12)
        self.btn_update_original = self._create_action_button(btn_row, "\\u66f4\\u65b0\\u539f\\u7248\\u57fa\\u7ebf", "#f59e0b", "#d97706", self.start_update_original)
        self.btn_update_original.grid(row=0, column=2, sticky="ew")
        self.btn_restore = self._create_action_button(btn_row, "\\u8fd8\\u539f\\u539f\\u7248", self.colors["danger"], "#ef4444", self.start_restore)
        self.btn_restore.grid(row=0, column=3, sticky="ew", padx=(12, 0))
        self.action_buttons = [self.btn_run, self.btn_bilingual, self.btn_update_original, self.btn_restore]
'''
    new_buttons = '''        for column in range(5):
            btn_row.grid_columnconfigure(column, weight=1, uniform="actions")
        self.btn_run = self._create_action_button(btn_row, "\\u4e2d\\u6587\\u6c49\\u5316", self.colors["success"], "#16a34a", self.start_patch)
        self.btn_run.grid(row=0, column=0, sticky="ew")
        self.btn_bilingual = self._create_action_button(btn_row, "\\u53cc\\u8bed\\u6c49\\u5316", self.colors["info"], "#3b82f6", self.start_bilingual)
        self.btn_bilingual.grid(row=0, column=1, sticky="ew", padx=(10, 0))
        self.btn_docs = self._create_action_button(btn_row, "\\u6ce8\\u5165\\u6587\\u6863", self.colors["accent"], "#5aa7ee", self.start_doc_patch)
        self.btn_docs.grid(row=0, column=2, sticky="ew", padx=(10, 0))
        self.btn_restore_docs = self._create_action_button(btn_row, "\\u8fd8\\u539f\\u6587\\u6863", self.colors["info"], "#d97706", self.start_doc_restore)
        self.btn_restore_docs.grid(row=0, column=3, sticky="ew", padx=(10, 0))
        self.btn_restore = self._create_action_button(btn_row, "\\u8fd8\\u539f\\u6c49\\u5316", self.colors["danger"], "#ef4444", self.start_restore)
        self.btn_restore.grid(row=0, column=4, sticky="ew", padx=(10, 0))
        self.action_buttons = [self.btn_run, self.btn_bilingual, self.btn_docs, self.btn_restore_docs, self.btn_restore]
'''
    source = _replace_once(source, old_buttons, new_buttons)

    old_width = '''count = max(len(self.action_buttons), 1)
        button_width = max(145, (width - (gap * (count - 1))) // count)'''
    new_width = '''count = max(len(self.action_buttons), 1)
        button_width = max(128, (width - (gap * (count - 1))) // count)'''
    source = _replace_once(source, old_width, new_width)

    old_set_buttons = '''    def set_buttons(self, state):
        enabled = state == "normal"
        self._set_action_button_state(self.btn_run, enabled)
        self._set_action_button_state(self.btn_bilingual, enabled)
        self._set_action_button_state(self.btn_update_original, enabled)
        self._set_action_button_state(self.btn_restore, enabled)
'''
    new_set_buttons = '''    def set_buttons(self, state):
        enabled = state == "normal"
        for button in self.action_buttons:
            self._set_action_button_state(button, enabled)
'''
    source = _replace_once(source, old_set_buttons, new_set_buttons)
    source = _remove_between(
        source,
        "\n    def update_original_baseline(self):\n",
        "\n    def check_supported_plugin(self):\n",
    )
    source = _remove_between(
        source,
        "\n    def run_update_original(self):\n",
        "\n    def start_patch(self):\n",
    )
    source = _remove_between(
        source,
        "\n    def start_update_original(self):\n",
        "\n    def start_restore(self):\n",
    )

    methods = '''
    def detect_doc_state(self):
        payload = _get_doc_payload()
        matched = 0
        backups = 0
        missing = []
        for rel, data in payload.items():
            file_path = os.path.join(PLUGIN_DIR, rel)
            if _file_matches_bytes(file_path, data):
                matched += 1
            elif not os.path.exists(file_path):
                missing.append(rel)
            if os.path.exists(file_path + DOC_BACKUP_SUFFIX):
                backups += 1
        return matched, len(payload), backups, missing

    def report_doc_state(self):
        matched, total, backups, missing = self.detect_doc_state()
        self.log("\\u4e2d\\u6587\\u5e2e\\u52a9\\u6587\\u6863: " + str(matched) + "/" + str(total) + " \\u4e2a\\u6587\\u4ef6\\u5df2\\u5339\\u914d")
        self.log("\\u6587\\u6863\\u5907\\u4efd: " + str(backups) + " \\u4e2a")
        if missing and matched == 0 and backups == 0:
            self.log("\\u4e2d\\u6587\\u5e2e\\u52a9\\u6587\\u6863\\u5c1a\\u672a\\u6ce8\\u5165\\uff0c\\u5f85\\u5199\\u5165\\u6587\\u4ef6: " + ", ".join(missing[:8]))
        elif missing:
            self.log("[\\u8b66\\u544a] \\u90e8\\u5206\\u6587\\u6863\\u6587\\u4ef6\\u672a\\u5339\\u914d: " + ", ".join(missing[:8]))

    def backup_doc_file(self, file_path):
        if not os.path.exists(file_path):
            return False
        backup_path = file_path + DOC_BACKUP_SUFFIX
        if not os.path.exists(backup_path):
            try:
                shutil.copy2(file_path, backup_path)
            except OSError as exc:
                raise RuntimeError("\\u521b\\u5efa\\u6587\\u6863\\u5907\\u4efd\\u5931\\u8d25: " + _safe_relpath(file_path, PLUGIN_DIR) + " | " + str(exc)) from exc
            self.log("\\u521b\\u5efa\\u6587\\u6863\\u5907\\u4efd: " + os.path.relpath(backup_path, PLUGIN_DIR))
        return True

    def inject_docs(self):
        ok, reason = self.check_supported_plugin()
        if not ok:
            raise RuntimeError(reason)
        payload = _get_doc_payload()
        for rel in DOC_PATCHED_FILES:
            data = payload.get(rel)
            if data is None:
                raise RuntimeError("\\u5185\\u7f6e\\u6587\\u6863 payload \\u7f3a\\u5931: " + rel)
            file_path = os.path.join(PLUGIN_DIR, rel)
            self.backup_doc_file(file_path)
            self.write_bytes(file_path, data)
            self.log("\\u5df2\\u6ce8\\u5165\\u6587\\u6863: " + rel)
        self.report_doc_state()

    def restore_docs(self):
        ok, reason = self.check_supported_plugin()
        if not ok:
            raise RuntimeError(reason)
        restored = 0
        removed = 0
        payload = _get_doc_payload()
        for rel in DOC_PATCHED_FILES:
            file_path = os.path.join(PLUGIN_DIR, rel)
            backup_path = file_path + DOC_BACKUP_SUFFIX
            if not os.path.exists(backup_path):
                data = payload.get(rel)
                if data is not None and _file_matches_bytes(file_path, data):
                    try:
                        os.remove(file_path)
                    except OSError as exc:
                        raise RuntimeError("\\u5220\\u9664\\u6ce8\\u5165\\u65b0\\u589e\\u6587\\u6863\\u5931\\u8d25: " + rel + " | " + str(exc)) from exc
                    removed += 1
                    self.log("\\u5df2\\u5220\\u9664\\u6ce8\\u5165\\u65b0\\u589e\\u6587\\u6863: " + rel)
                    continue
                self.log("\\u672a\\u627e\\u5230\\u6587\\u6863\\u5907\\u4efd\\uff0c\\u8df3\\u8fc7: " + rel)
                continue
            try:
                shutil.copy2(backup_path, file_path)
                os.remove(backup_path)
            except OSError as exc:
                raise RuntimeError("\\u8fd8\\u539f\\u6587\\u6863\\u5931\\u8d25: " + rel + " | " + str(exc)) from exc
            restored += 1
            self.log("\\u5df2\\u8fd8\\u539f\\u6587\\u6863: " + rel)
        self.log("\\u6587\\u6863\\u8fd8\\u539f\\u5b8c\\u6210\\uff0c\\u5df2\\u8fd8\\u539f\\u6587\\u4ef6\\u6570: " + str(restored))
        if removed:
            self.log("\\u5df2\\u5220\\u9664\\u6ce8\\u5165\\u65b0\\u589e\\u6587\\u4ef6\\u6570: " + str(removed))
        self.report_doc_state()

    def run_doc_patching(self):
        self.set_buttons("disabled")
        try:
            self.log("")
            self.log("\\u5f00\\u59cb\\u6ce8\\u5165\\u4e2d\\u6587\\u5e2e\\u52a9\\u6587\\u6863...")
            self.inject_docs()
            self.log("")
            self.log("\\u6587\\u6863\\u6ce8\\u5165\\u5b8c\\u6210\\uff0c\\u8bf7\\u91cd\\u542f Blender \\u751f\\u6548\\u3002")
            messagebox.showinfo("\\u6210\\u529f", "NeXus \\u4e2d\\u6587\\u5e2e\\u52a9\\u6587\\u6863\\u6ce8\\u5165\\u5b8c\\u6210\\uff01" + chr(10) + "\\u8bf7\\u91cd\\u542f Blender \\u751f\\u6548\\u3002")
        except Exception as exc:
            self.show_error("\\u4e2d\\u6587\\u5e2e\\u52a9\\u6587\\u6863\\u6ce8\\u5165", exc)
        finally:
            self.set_buttons("normal")

    def run_doc_restore(self):
        self.set_buttons("disabled")
        try:
            self.log("")
            self.log("\\u5f00\\u59cb\\u8fd8\\u539f\\u4e2d\\u6587\\u5e2e\\u52a9\\u6587\\u6863...")
            self.restore_docs()
            self.log("")
            self.log("\\u6587\\u6863\\u8fd8\\u539f\\u5b8c\\u6210\\uff0c\\u8bf7\\u91cd\\u542f Blender \\u751f\\u6548\\u3002")
            messagebox.showinfo("\\u6210\\u529f", "\\u5df2\\u8fd8\\u539f\\u4e2d\\u6587\\u5e2e\\u52a9\\u6587\\u6863\\u3002" + chr(10) + "\\u8bf7\\u91cd\\u542f Blender \\u751f\\u6548\\u3002")
        except Exception as exc:
            self.show_error("\\u8fd8\\u539f\\u4e2d\\u6587\\u5e2e\\u52a9\\u6587\\u6863", exc)
        finally:
            self.set_buttons("normal")

    def start_doc_patch(self):
        self.log("")
        self.log("----------------------")
        threading.Thread(target=self.run_doc_patching, daemon=True).start()

    def start_doc_restore(self):
        answer = messagebox.askyesno("\\u786e\\u8ba4", "\\u786e\\u5b9a\\u8981\\u8fd8\\u539f\\u4e2d\\u6587\\u5e2e\\u52a9\\u6587\\u6863\\u5417\\uff1f")
        if answer:
            self.log("")
            self.log("----------------------")
            threading.Thread(target=self.run_doc_restore, daemon=True).start()

'''
    source = _replace_once(source, "    def start_patch(self):\n", methods + "    def start_patch(self):\n")

    source = source.replace(
        'self.log(self.current_state_var.get().replace("\\u5f53\\u524d\\u72b6\\u6001: ", "\\u5f53\\u524d\\u7ffb\\u8bd1\\u72b6\\u6001: "))',
        'self.log(self.current_state_var.get().replace("\\u5f53\\u524d\\u72b6\\u6001: ", "\\u5f53\\u524d\\u7ffb\\u8bd1\\u72b6\\u6001: "))\n        self.report_doc_state()',
        1,
    )

    fallback = r'''
def _native_message(title, text, flags=0):
    import ctypes
    return ctypes.windll.user32.MessageBoxW(None, text, title, flags)


def _fallback_log(message):
    _append_log_file(message)


def _fallback_log_diagnostic(action, exc):
    for line in _diagnostic_lines(action, exc):
        for part in str(line).rstrip().splitlines() or [""]:
            _fallback_log(part)
    _fallback_log("请把上面的诊断日志或日志文件发给维护者。")


def _fallback_choose_action():
    yes_no_cancel = 0x00000003
    icon_question = 0x00000020
    result = _native_message(
        "NeXus 中文汉化与文档整合注入工具",
        "当前 Python 环境没有 tkinter，已切换到简易模式。\n\n选择操作：\n是 = 中文汉化\n否 = 其他操作\n取消 = 退出",
        yes_no_cancel | icon_question,
    )
    if result == 6:
        return "patch"
    if result != 7:
        return None
    result = _native_message(
        "选择操作",
        "选择操作：\n是 = 双语汉化\n否 = 文档/还原操作\n取消 = 退出",
        yes_no_cancel | icon_question,
    )
    if result == 6:
        return "bilingual"
    if result != 7:
        return None
    result = _native_message(
        "选择操作",
        "选择操作：\n是 = 注入中文帮助文档\n否 = 还原操作\n取消 = 退出",
        yes_no_cancel | icon_question,
    )
    if result == 6:
        return "docs"
    if result != 7:
        return None
    result = _native_message(
        "选择操作",
        "选择操作：\n是 = 还原中文帮助文档\n否 = 还原汉化\n取消 = 退出",
        yes_no_cancel | icon_question,
    )
    if result == 6:
        return "restore_docs"
    if result == 7:
        return "restore"
    return None


def _run_without_tk():
    action = _fallback_choose_action()
    if not action:
        return
    app = object.__new__(PatcherApp)
    app.log = _fallback_log
    app.set_buttons = lambda _state: None
    try:
        _fallback_log("")
        _fallback_log("----------------------")
        _fallback_log("目标插件路径: " + PLUGIN_DIR)
        if action == "patch":
            _fallback_log("开始注入中文汉化...")
            app.apply_patch(bilingual=False)
        elif action == "bilingual":
            _fallback_log("开始注入双语汉化...")
            app.apply_patch(bilingual=True)
        elif action == "docs":
            _fallback_log("开始注入中文帮助文档...")
            app.inject_docs()
        elif action == "restore_docs":
            _fallback_log("开始还原中文帮助文档...")
            app.restore_docs()
        elif action == "restore":
            result = _native_message(
                "确认还原",
                "确定要还原汉化吗？\n这会还原已备份的源码，并移除或恢复 translations.py。",
                0x00000004 | 0x00000030,
            )
            if result != 6:
                return
            _fallback_log("开始还原汉化...")
            for rel in RESTORE_SOURCE_FILES:
                app.restore_file(rel)
            trans_path = os.path.join(PLUGIN_DIR, "translations.py")
            trans_bak = trans_path + ".bak"
            if os.path.exists(trans_bak):
                shutil.copy2(trans_bak, trans_path)
                os.remove(trans_bak)
                _fallback_log("已恢复: translations.py")
            elif os.path.exists(trans_path):
                os.remove(trans_path)
                _fallback_log("已删除: translations.py")
        _fallback_log("操作完成，请重启 Blender 生效。")
        _native_message(
            "操作完成",
            "操作完成，请重启 Blender 生效。\n\n日志文件：\n" + os.path.join(TOOL_DIR, "NeXus中文汉化与文档整合注入工具.log"),
            0x00000040,
        )
    except Exception as exc:
        _fallback_log_diagnostic("简易模式操作: " + str(action), exc)
        _native_message(
            "错误",
            str(exc) + "\n\n详细诊断已写入日志文件：\n" + LOG_FILE,
            0x00000010,
        )

'''
    source = _replace_once(source, '\nif __name__ == "__main__":\n', "\n" + fallback + 'if __name__ == "__main__":\n')
    old_simple_main = '''if __name__ == "__main__":
    root = tk.Tk()
    app = PatcherApp(root)
    root.mainloop()
'''
    new_guarded_main = '''if __name__ == "__main__":
    try:
        if tk is None:
            _run_without_tk()
        else:
            try:
                root = tk.Tk()
            except Exception as exc:
                _fallback_log("[警告] Tk 初始化失败，切换到简易模式: " + str(exc))
                _native_message(
                    "Tk 初始化失败",
                    "当前 Python 无法初始化 tkinter 图形界面，已切换到简易模式。" + chr(10) + chr(10) + str(exc),
                    0x00000030,
                )
                _run_without_tk()
            else:
                app = PatcherApp(root)
                root.mainloop()
    except Exception as exc:
        try:
            _fallback_log_diagnostic("启动工具", exc)
            _native_message(
                "启动错误",
                str(exc) + chr(10) + chr(10) + "详细诊断已写入日志文件：" + chr(10) + LOG_FILE,
                0x00000010,
            )
        except Exception:
            raise
'''
    if old_simple_main in source:
        source = source.replace(old_simple_main, new_guarded_main, 1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(source, encoding="utf-8")
    return output_path


if __name__ == "__main__":
    print(build())
