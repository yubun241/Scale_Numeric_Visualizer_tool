class ScaleNumericVisualizer:
    def __init__(self):
        # 12音の定義（シャープ表記に統一）
        self.notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        
        # スケールの定義 (各音のステップ間隔: 1.0=全音, 0.5=半音)
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
        """入力されたルート音を正規化（大文字化、♭を#へ置換）"""
        root = root_str.upper()
        # 簡易的な♭→#変換
        replacements = {"BB": "A#", "EB": "D#", "GB": "F#", "AB": "G#", "DB": "C#"}
        for flt, shp in replacements.items():
            root = root.replace(flt, shp)
        return root

    def get_scale_data(self, root, scale_name):
        """ルート音名と数値のリストを生成"""
        if root not in self.notes:
            return None, f"エラー: '{root}' は有効な音名ではありません。"
        
        # スケール名の名寄せ（入力のゆれを吸収）
        matched_scale = None
        for s in self.scale_intervals.keys():
            if s.lower() == scale_name.lower():
                matched_scale = s
                break
        
        if not matched_scale:
            return None, f"エラー: スケール '{scale_name}' が見つかりません。"

        intervals = self.scale_intervals[matched_scale]
        start_idx = self.notes.index(root)
        
        scale_data = []
        current_idx = start_idx
        current_val = 1.0  # ルートを1.0とする
        
        # ルート（第1音）を追加
        scale_data.append({"note": self.notes[current_idx], "value": current_val})
        
        # 2番目以降の構成音を計算
        for step in intervals[:-1]:
            current_idx = (current_idx + int(step * 2)) % 12
            current_val += step
            scale_data.append({"note": self.notes[current_idx], "value": current_val})
            
        return scale_data, None

def main():
    visualizer = ScaleNumericVisualizer()
    
    print("=== Scale Degree & Note Visualizer ===")
    print("例: 'C Major', 'Am Natural Minor', 'G# Pentatonic Minor'")
    print("終了するには 'exit' と入力してください。")
    
    while True:
        user_input = input("\nキーを入力してください > ").strip()
        
        if user_input.lower() == 'exit':
            print("プログラムを終了します。")
            break
        
        if not user_input:
            continue

        # スペースで分割 (例: "C", "Major")
        parts = user_input.split()
        if len(parts) < 2:
            print("形式エラー: 'Root ScaleName' の形式で入力してください。")
            continue
            
        root_raw = parts[0]
        scale_raw = " ".join(parts[1:]) # "Natural Minor" のようにスペースを含む場合に対応
        
        # 正規化処理
        root = visualizer.format_root(root_raw)
        
        # データ取得
        data, error = visualizer.get_scale_data(root, scale_raw)
        
        if error:
            print(error)
        else:
            print(f"\n【{root} {scale_raw.title()}】の構成音と数値:")
            
            # 見やすく整形して表示
            header_notes = "音名: "
            header_values = "数値: "
            
            for item in data:
                note_str = f"{item['note']}".ljust(5)
                val_str = f"{item['value']:.1f}".ljust(5)
                header_notes += f"| {note_str} "
                header_values += f"| {val_str} "
            
            separator = "-" * len(header_notes)
            print(separator)
            print(header_notes + "|")
            print(header_values + "|")
            print(separator)

if __name__ == "__main__":
    main()
