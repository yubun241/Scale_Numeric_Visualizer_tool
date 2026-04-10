## Scale_Numeric_Visualizer_tool
音楽のスケール（音階）を構成する音名と、そのステップ（数値）を素早く確認するためのコマンドラインツールです。

ルート音とスケール名を指定することで、各構成音を一覧表示します。


## 特徴
多様なスケールに対応: Major, Minorはもちろん、DorianやLydianなどのモード、Pentatonicスケールにも対応しています。

柔軟な入力: ♭（フラット）表記のルート音（例: Eb）を自動的に#（シャープ）表記（D#）に変換して処理します。

数値化表示: ルートを1.0とし、全音を1.0、半音を0.5としてカウントした数値を表示するため、音楽理論的な間隔を直感的に把握できます。


## 使い方
実行方法

Pythonがインストールされている環境で、スクリプトを実行してください。

bash


python main.py

##操作方法
プログラムが起動すると入力待機状態になります。ルート音 スケール名 の形式で入力してください。

入力例:

C Major

Eb Natural Minor

G# Lydian

A Pentatonic Minor

終了する場合は exit と入力します。


対応スケール一覧

現在、以下のスケール名に対応しています：


分類	スケール名 (入力用キーワード)

メジャー/マイナー	Major, Natural Minor, Harmonic Minor, Melodic Minor

チャーチモード	Dorian, Phrygian, Lydian, Mixolydian

ペンタトニック	Pentatonic Major, Pentatonic Minor

出力イメージ

text

キーを入力してください > C Major

【C Major】の構成音と数値:
------------------------------------------------------------

音名: | C     | D     | E     | F     | G     | A     | B     |

数値: | 1.0   | 2.0   | 3.0   | 3.5   | 4.5   | 5.5   | 6.5   |

------------------------------------------------------------


## クラスの仕様（開発者向け）
ScaleNumericVisualizer クラス

format_root(root_str): 入力されたルート音を大文字化し、♭を#に正規化します。

get_scale_data(root, scale_name): 指定されたルートとスケールに基づき、音名と数値を含む辞書のリストを返します。

scale_intervals: 各スケールの音程間隔をリスト形式で定義しています（1.0＝全音, 0.5＝半音）。
