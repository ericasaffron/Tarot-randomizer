from PIL import Image, ImageDraw, ImageFont
import os

BASE = os.path.dirname(os.path.abspath(__file__))
IMAGES = os.path.join(BASE, "Images")
OUT = os.path.join(BASE, "random-card-service", "composed")
os.makedirs(OUT, exist_ok=True)

FONT_SERIF = "C:/Windows/Fonts/yumin.ttf"
FONT_SERIF_BOLD = "C:/Windows/Fonts/yumindb.ttf"

CANVAS_W, CANVAS_H = 320, 620
CARD_W = 240
CREAM = (255, 253, 249)
GOLD = (228, 201, 138)
GOLD_DARK = (150, 116, 47)
INK = (74, 63, 53)
MUTED = (138, 122, 104)

cards = [
    ("RWS_Tarot_00_Fool.jpg", "0 – 愚者", "自由な始まりと無限の可能性"),
    ("RWS_Tarot_01_Magician.jpg", "I – 魔術師", "意志の力で新しい扉を開く"),
    ("RWS_Tarot_02_High_Priestess.jpg", "II – 女教皇", "静かな直感と内なる知恵"),
    ("RWS_Tarot_03_Empress.jpg", "III – 女帝", "豊かさと創造性を大切に"),
    ("RWS_Tarot_04_Emperor.jpg", "IV – 皇帝", "安定と秩序で土台を築く"),
    ("RWS_Tarot_05_Hierophant.jpg", "V – 教皇", "信頼できる伝統と学び"),
    ("RWS_Tarot_06_Lovers.jpg", "VI – 恋人", "選択と調和、心のままに"),
    ("RWS_Tarot_07_Chariot.jpg", "VII – 戦車", "迷いを断ち切り前進する"),
    ("RWS_Tarot_08_Strength.jpg", "VIII – 力", "内なる強さと優しい忍耐"),
    ("RWS_Tarot_09_Hermit.jpg", "IX – 隠者", "一人の時間が答えをくれる"),
    ("RWS_Tarot_10_Wheel_of_Fortune.jpg", "X – 運命の輪", "巡り合わせと訪れる転機"),
    ("RWS_Tarot_11_Justice.jpg", "XI – 正義", "誠実な判断が公正を導く"),
    ("RWS_Tarot_12_Hanged_Man.jpg", "XII – 吊された男", "視点を変えて待つ勇気"),
    ("RWS_Tarot_13_Death.jpg", "XIII – 死神", "終わりの先にある再生"),
    ("RWS_Tarot_14_Temperance.jpg", "XIV – 節制", "焦らず穏やかに整える調和"),
    ("RWS_Tarot_15_Devil.jpg", "XV – 悪魔", "執着と誘惑への気づき"),
    ("RWS_Tarot_16_Tower.jpg", "XVI – 塔", "崩れた先にある新しい景色"),
    ("RWS_Tarot_17_Star.jpg", "XVII – 星", "静かに叶っていく希望"),
    ("RWS_Tarot_18_Moon.jpg", "XVIII – 月", "不安の奥にある直感"),
    ("RWS_Tarot_19_Sun.jpg", "XIX – 太陽", "ありのままで輝く喜び"),
    ("RWS_Tarot_20_Judgement.jpg", "XX – 審判", "過去を認め次へ進む決断"),
    ("RWS_Tarot_21_World.jpg", "XXI – 世界", "一つの旅の終わりと完成"),
]

font_name = ImageFont.truetype(FONT_SERIF_BOLD, 26)
font_meaning = ImageFont.truetype(FONT_SERIF, 20)


def centered_text(draw, text, y, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (CANVAS_W - w) / 2
    draw.text((x, y), text, font=font, fill=fill)


for i, (fname, name, meaning) in enumerate(cards):
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), CREAM)
    draw = ImageDraw.Draw(canvas)

    draw.rounded_rectangle([4, 4, CANVAS_W - 5, CANVAS_H - 5], radius=18, outline=GOLD, width=2)

    card = Image.open(os.path.join(IMAGES, fname)).convert("RGB")
    ratio = CARD_W / card.width
    card = card.resize((CARD_W, int(card.height * ratio)))

    card_x = (CANVAS_W - CARD_W) // 2
    card_y = 30
    border = 5
    draw.rectangle(
        [card_x - border, card_y - border, card_x + CARD_W + border, card_y + card.height + border],
        fill=(255, 255, 255),
        outline=GOLD,
        width=1,
    )
    canvas.paste(card, (card_x, card_y))

    text_y = card_y + card.height + border + 26
    centered_text(draw, name, text_y, font_name, INK)
    centered_text(draw, meaning, text_y + 40, font_meaning, MUTED)

    canvas.save(os.path.join(OUT, f"{i}.png"))

print(f"generated {len(cards)} composites in {OUT}")
