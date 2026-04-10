class ScaleIntervalVisualizer:
    def __init__(self):
        # 12音（シャープ表記）
        self.notes = [
            "C", "C#", "D", "D#", "E", "F",
            "F#", "G", "G#", "A", "A#", "B"
        ]

        # スケール定義（全音=1.0 / 半音=0.5）
        self.scale_intervals = {
            "Major": [1.0, 1.0, 0.5, 1.0, 1.0, 1.0, 0.5],
            "Natural Minor": [1.0, 0.5, 1.0, 1.0, 0.5, 1.0, 1.0],
            "Harmonic Minor": [1.0, 0.5, 1.0, 1.0, 0.5, 1.5, 0.5],
            "Melodic Minor": [1.0, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5],
            "Dorian": [1.0, 0.5, 1.0, 1.0, 1.0, 0.5, 1.0],
            "Phrygian": [0.5, 1.0, 1.0, 1.0, 0.5, 1.0, 1.0],
            "Lydian": [1.0, 1.0, 1.0, 0.5, 1.0, 1.0, 0.5],
            "Mixolydian": [1.0, 1.0, 0.5, 1.0, 1.0, 0.5, 1.0],
            "Pentatonic Major": [1.0, 1.0, 1.5, 1.0, 1.5],
            "Pentatonic Minor": [1.5, 1.0, 1.0, 1.5, 1.0],
        }

    def format_root(self, root_str):
        """ルート音の正規化（♭→#）"""
        root = root_str.upper()

        replacements = {
            "BB": "A#", "EB": "D#", "GB": "F#",
            "AB": "G#", "DB": "C#"
        }

        for flt, shp in replacements.items():
            root = root.replace(flt, shp)

        return root

    def get_scale_data(self, root, scale_name):
        """音名とインターバル（1周分）を取得"""
        if root not in self.notes:
            return None, f"エラー: '{root}' は有効な音名ではありません。"

        # スケール名マッチング
        matched_scale = None
        for s in self.scale_intervals.keys():
            if s.lower() == scale_name.lower():
                matched_scale = s
                break

        if not matched_scale:
            return None, f"エラー: スケール '{scale_name}' が見つかりません。"

        intervals = self.scale_intervals[matched_scale]
        current_idx = self.notes.index(root)

        scale_data = []

        # ルート（開始点）
        scale_data.append({
            "note": self.notes[current_idx],
            "interval": "-"
        })

        # 全インターバルを適用（最後にルートへ戻る）
        for step in intervals:
            current_idx = (current_idx + int(step * 2)) % 12

            scale_data.append({
                "note": self.notes[current_idx],
                "interval": step
            })

        return scale_data, None


def main():
    visualizer = ScaleIntervalVisualizer()

    print("=== Scale Interval Visualizer (Loop対応版) ===")
    print("例: 'C Major', 'Am Natural Minor', 'G# Pentatonic Minor'")
    print("終了するには 'exit' と入力してください。")

    while True:
        user_input = input("\nキーを入力してください > ").strip()

        if user_input.lower() == 'exit':
            print("プログラムを終了します。")
            break

        if not user_input:
            continue

        parts = user_input.split()
        if len(parts) < 2:
            print("形式エラー: 'Root ScaleName' の形式で入力してください。")
            continue

        root_raw = parts[0]
        scale_raw = " ".join(parts[1:])

        root = visualizer.format_root(root_raw)

        data, error = visualizer.get_scale_data(root, scale_raw)

        if error:
            print(error)
            continue

        print(f"\n【{root} {scale_raw.title()}】")

        header_notes = "音名:        "
        header_intervals = "インターバル: "

        for item in data:
            note_str = f"{item['note']}".ljust(5)
            interval = item['interval']

            if isinstance(interval, float):
                interval_str = f"{interval:.1f}".ljust(5)
            else:
                interval_str = f"{interval}".ljust(5)

            header_notes += f"| {note_str} "
            header_intervals += f"| {interval_str} "

        separator = "-" * len(header_notes)

        print(separator)
        print(header_notes + "|")
        print(header_intervals + "|")
        print(separator)


if __name__ == "__main__":
    main()