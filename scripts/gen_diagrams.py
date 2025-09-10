from graphviz import Digraph
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

def node(dot: Digraph, key: str, label: str, fill: str | None = None, tip: str | None = None):
    attrs = {}
    if fill:
        attrs["fillcolor"] = fill
        attrs["style"] = "rounded,filled"
    else:
        attrs["style"] = "rounded,filled"
    if tip:
        attrs["tooltip"] = tip
    dot.node(key, label, **attrs)

def build_conjugation():
    dot = Digraph(comment="Japanese Verb Conjugation (行く・食べる)")
    dot.attr('graph', rankdir='LR')
    dot.attr('node', shape='box', color='lightgrey', fontname="Noto Sans JP", fontsize='12')
    dot.attr('edge', fontname="Noto Sans JP", fontsize='11')

    # === Базовые формы (活用形) ===
    node(dot, 'Mizen', '未然形（みぜんけい）\nнезавершённая',
         fill='#DDDDDD',
         tip='База для: отрицания (〜ない), волевой (〜う/よう), потенциала (〜れる/られる), пассива (〜れる/られる), каузатива (〜せる/させる).')
    node(dot, 'Renyou', '連用形（れんようけい）\nсоединительная',
         fill='#DDDDDD',
         tip='База для: ます-формы, たい, て/た и сложных глагольных конструкций.')
    node(dot, 'Shuushi', '終止形（しゅうしけい）\nконечная',
         fill='#DDDDDD',
         tip='Словарная/финальная форма. Часто конец предложения.')
    node(dot, 'Rentaikei', '連体形（れんたいけい）\nопределительная',
         fill='#DDDDDD',
         tip='Форма перед существительным (атрибутивная).')
    node(dot, 'Katei', '仮定形（かていけい）\nусловная',
         fill='#DDDDDD',
         tip='База для условных конструкций с ば: 〜えば/〜れば («если…»).')
    node(dot, 'Meirei', '命令形（めいれいけい）\nповелительная',
         fill='#DDDDDD',
         tip='Повелительная форма. Часто звучит резко; мягкие альтернативы: 〜てください, 〜なさい.')

    # === Производные от 未然形 (みぜんけい) ===
    node(dot, 'Neg', '行かない / 食べない\n(否定・ひてい)',
         fill='#F4A6A6',
         tip='Отрицательная форма: «не …». Образование: 未然形 + ない. Используется и как база для «обязан»: 〜なければならない/なりません.')
    node(dot, 'Vol', '行こう / 食べよう\n(意向形・いこうけい)',
         fill='#9EC9F5',
         tip='Волевая форма: предложение/намерение «давай…», «сделаю-ка…». 五段: 〜う, 一段: 〜よう.')
    node(dot, 'Pot', '行ける / 食べられる\n(可能形・かのうけい)',
         fill='#A9E5A9',
         tip='Потенциал («могу …»). 五段: 語幹+える (行ける), 一段: 〜られる (食べられる). Разг. у 一段: ら抜き → 食べれる.')
    node(dot, 'Pas', '行かれる / 食べられる\n(受身形・うけみけい)',
         fill='#F2E29F',
         tip='Пассив: «подвергаться действию». 行かれる/食べられる.')
    node(dot, 'Caus', '行かせる / 食べさせる\n(使役形・しえきけい)',
         fill='#D9A6E8',
         tip='Каузатив: «заставить/позволить …». 行かせる/食べさせる.')

    dot.edge('Mizen', 'Neg', tooltip='未然形 → 否定（〜ない）')
    dot.edge('Mizen', 'Vol', tooltip='未然形 → 意向形（〜う/よう）')
    dot.edge('Mizen', 'Pot', tooltip='未然形 → 可能形（〜れる/られる）')
    dot.edge('Mizen', 'Pas', tooltip='未然形 → 受身形（〜れる/られる）')
    dot.edge('Mizen', 'Caus', tooltip='未然形 → 使役形（〜せる/させる）')

    # === Производные от 連用形 (れんようけい) ===
    node(dot, 'Masu', '行きます / 食べます\n(ます形)',
         fill='#F3E39C',
         tip='Вежливая форма 〜ます. Основана на 連用形.')
    node(dot, 'Tai', '行きたい / 食べたい\n(たい形)',
         fill='#F7B6C4',
         tip='Желание «хочу …» (〜たい). Обычно о первом лице/собственном желании.')
    node(dot, 'Sugiru', '行きすぎる / 食べすぎる\n(すぎる)',
         fill='#CFEFF0',
         tip='«Слишком …» (〜すぎる). Присоединяется к 連用形.')
    node(dot, 'Te', '行って / 食べて\n(て形)',
         fill='#FFD1A9',
         tip='て-форма: связь действий, просьба (〜てください), прогрессив (〜ている), разрешение/запрет (〜てもいい/〜てはいけない) и др.')
    node(dot, 'Ta', '行った / 食べた\n(た形)',
         fill='#FFBEA3',
         tip='Прошедшее/совершённость: 〜た/〜だ. Формируется от て-формы.')

    dot.edge('Renyou', 'Masu', tooltip='連用形 → ます形')
    dot.edge('Renyou', 'Tai', tooltip='連用形 → たい形')
    dot.edge('Renyou', 'Sugiru', tooltip='連用形 → 〜すぎる')
    dot.edge('Renyou', 'Te', tooltip='連用形 → て形')
    dot.edge('Renyou', 'Ta', tooltip='連用形 → た形')

    # «Должен»: из отрицания ない → なければならない/なりません
    node(dot, 'Nakereba',
         '行かなければならない / 行かなければなりません\n食べなければならない / 食べなければなりません',
         fill='#D8C6EA',
         tip='«Должен …»: условие от отрицания (…なければ) + ならない/なりません. Разговорные сокращения: 〜なきゃ, 〜ないと.')
    dot.edge('Neg', 'Nakereba', tooltip='ない形 → なければならない/なりません')

    # 終止・連体 (словарная/атрибутивная)
    node(dot, 'Dict', '行く / 食べる\n(終止・連体)',
         fill='#FFFFFF',
         tip='Словарная (終止形) и определительная (連体形) формы: базовый вид; перед сущ.: 行く人/食べる人.')
    dot.edge('Shuushi', 'Dict', tooltip='終止形 → словарная форма')
    dot.edge('Rentaikei', 'Dict', tooltip='連体形 → определительная форма')

    # 仮定形 (〜ば)
    node(dot, 'If', '行けば / 食べれば\n(仮定形・ば)',
         fill='#E8F7E8',
         tip='Условная конструкция с ば: «если…». 五段: 語幹+えば, 一段: 語幹+れば.')
    dot.edge('Katei', 'If', tooltip='仮定形 → 〜ば')

    # 命令形
    node(dot, 'Imper', '行け / 食べろ\n(命令形)',
         fill='#B9C7E6',
         tip='Повелительная форма (резкая). Мягче: 〜てください, 〜なさい.')
    dot.edge('Meirei', 'Imper', tooltip='命令形')

    # Разговорный потенциал (ら抜き言葉) как примечание к 一段
    node(dot, 'PotCasual', '食べれる（口語） / 食べれない\n※ ら抜き言葉',
         fill='#A9E5A9',
         tip='Разговорный потенциал 一段: 食べられる → 食べれる. Отрицание: 食べれない. Уместен в разговоре; избегай в формальном письме.')
    dot.edge('Pot', 'PotCasual', style='dashed', tooltip='可能形（正式） → 口語（ら抜き）')

    # === Экспорт ===
    # SVG (с подсказками)
    dot.format = 'svg'
    dot.render(str(OUT / 'conjugation'), cleanup=True)
    # PNG (на всякий случай, без интерактива)
    dot.format = 'png'
    dot.render(str(OUT / 'conjugation'), cleanup=True)

if __name__ == "__main__":
    build_conjugation()
    print(f"Generated to: {OUT}")
