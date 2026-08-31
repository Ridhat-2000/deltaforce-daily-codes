from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from pathlib import Path
import json


# ============================================================
# CONFIG
# ============================================================

CONFIG = {

    # ========================================================
    # OUTPUT
    # ========================================================

    "output": "final_youtube_square.png",

    # --------------------------------------------------------
    # SQUARE YOUTUBE POST
    # --------------------------------------------------------

    "canvas_width": 1800,
    "canvas_height": 1800,

    # Space between cards
    "gap": 6,

    # Color visible between cards
    "gap_color": "#111111",


    # ========================================================
    # JSON DATA
    # ========================================================

    # The collector.py updates this file automatically
    "data_file": "codes.json",


    # ========================================================
    # DEFAULT FONTS
    # ========================================================

    "title_font": "DejaVuSans.ttf",

    # IMPORTANT:
    # Code uses the BOLD font
    "code_font": "DejaVuSans-Bold.ttf",

    "date_font": "DejaVuSans.ttf",


    # ========================================================
    # DEFAULT TEXT SIZES
    # ========================================================

    "title_size": 50,
    "code_size": 58,
    "date_size": 30,


    # ========================================================
    # DEFAULT TEXT COLORS
    # ========================================================

    "title_color": "#FFFFFF",
    "code_color": "#00FF9D",
    "date_color": "#AEB7B2",


    # ========================================================
    # DEFAULT CENTER TEXT POSITION
    #
    # 0   = left / top
    # 50  = center
    # 100 = right / bottom
    # ========================================================

    "text_x": 50,
    "text_y": 50,


    # ========================================================
    # DEFAULT DATE POSITION
    # ========================================================

    "date_x": 5,
    "date_y": 88,


    # ========================================================
    # TITLE / CODE SPACING
    # ========================================================

    "title_code_spacing": 30,


    # ========================================================
    # DEFAULT IMAGE SETTINGS
    # ========================================================

    # 0.0 = no dark overlay
    # 1.0 = completely black
    "overlay_opacity": 0.38,

    # 1.0 = original brightness
    # 0.8 = darker
    # 1.2 = brighter
    "brightness": 1.0,


    # ========================================================
    # SIX IMAGES
    #
    # Titles stay here.
    # Codes and dates are automatically loaded from JSON.
    # ========================================================

    "cards": [

        {
            "image": "images/zd.png",
            "title": "Zero Dam",
        },

        {
            "image": "images/lg.png",
            "title": "Layali Grove",
        },

        {
            "image": "images/b.webp",
            "title": "Brakkesh",
        },

        {
            "image": "images/sc.png",
            "title": "Space City",
        },

        {
            "image": "images/tp.jpg",
            "title": "Tide Prison",
        },

        {
            "image": "images/az3.png",
            "title": "AZ3",
        },

    ],


    # ========================================================
    # INDIVIDUAL SETTINGS FOR EACH IMAGE
    #
    # Anything here overrides the default CONFIG above.
    # ========================================================

    "card_settings": [

        # ====================================================
        # IMAGE 1 — ZERO DAM
        # ====================================================

        {

            "title_size": 50,
            "code_size": 58,
            "date_size": 30,

            "title_color": "#FFFFFF",
            "code_color": "#00FF9D",
            "date_color": "#AEB7B2",

            "text_x": 50,
            "text_y": 50,

            "date_x": 5,
            "date_y": 88,

            "title_code_spacing": 30,

            "overlay_opacity": 0.42,
            "brightness": 1.0,

            "image_x": 50,
            "image_y": 50,
        },


        # ====================================================
        # IMAGE 2 — LAYALI GROVE
        # ====================================================

        {

            "title_size": 50,
            "code_size": 58,
            "date_size": 30,

            "title_color": "#FFFFFF",
            "code_color": "#00FF9D",
            "date_color": "#AEB7B2",

            "text_x": 50,
            "text_y": 50,

            "date_x": 5,
            "date_y": 88,

            "title_code_spacing": 30,

            "overlay_opacity": 0.35,
            "brightness": 1.0,

            "image_x": 50,
            "image_y": 50,
        },


        # ====================================================
        # IMAGE 3 — BRAKKESH
        # ====================================================

        {

            "title_size": 50,
            "code_size": 58,
            "date_size": 30,

            "title_color": "#FFFFFF",
            "code_color": "#00FF9D",
            "date_color": "#AEB7B2",

            "text_x": 50,
            "text_y": 50,

            "date_x": 5,
            "date_y": 88,

            "title_code_spacing": 30,

            "overlay_opacity": 0.45,
            "brightness": 1.0,

            "image_x": 50,
            "image_y": 50,
        },


        # ====================================================
        # IMAGE 4 — SPACE CITY
        # ====================================================

        {

            "title_size": 50,
            "code_size": 58,
            "date_size": 30,

            "title_color": "#FFFFFF",
            "code_color": "#00FF9D",
            "date_color": "#AEB7B2",

            "text_x": 50,
            "text_y": 50,

            "date_x": 5,
            "date_y": 88,

            "title_code_spacing": 20,

            "overlay_opacity": 0.38,
            "brightness": 1.0,

            "image_x": 50,
            "image_y": 50,
        },


        # ====================================================
        # IMAGE 5 — TIDE PRISON
        # ====================================================

        {

            "title_size": 50,
            "code_size": 58,
            "date_size": 30,

            "title_color": "#FFFFFF",
            "code_color": "#00FF9D",
            "date_color": "#AEB7B2",

            "text_x": 50,
            "text_y": 50,

            "date_x": 5,
            "date_y": 88,

            "title_code_spacing": 30,

            "overlay_opacity": 0.42,
            "brightness": 1.0,

            "image_x": 50,
            "image_y": 50,
        },


        # ====================================================
        # IMAGE 6 — AZ3
        # ====================================================

        {

            "title_size": 50,
            "code_size": 58,
            "date_size": 30,

            "title_color": "#FFFFFF",
            "code_color": "#00FF9D",
            "date_color": "#AEB7B2",

            "text_x": 50,
            "text_y": 50,

            "date_x": 5,
            "date_y": 88,

            "title_code_spacing": 30,

            "overlay_opacity": 0.40,
            "brightness": 1.0,

            "image_x": 50,
            "image_y": 50,
        },

    ],
}


# ============================================================
# LOAD DAILY DATA FROM JSON
# ============================================================

def load_daily_data():

    data_file = Path(
        CONFIG["data_file"]
    )


    if not data_file.exists():

        raise FileNotFoundError(

            f"Could not find {data_file}\n\n"

            "Run collector.py first so that "
            "codes.json is created."
        )


    try:

        with open(
            data_file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


    except Exception as e:

        raise RuntimeError(

            f"Could not read {data_file}:\n{e}"
        )


    saved_date = data.get(
        "date"
    )


    codes = data.get(
        "codes",
        {}
    )


    # --------------------------------------------------------
    # Make sure all six codes exist
    # --------------------------------------------------------

    missing = [

        name

        for name in [

            "Zero Dam",
            "Layali Grove",
            "Brakkesh",
            "Space City",
            "Tide Prison",
            "AZ3",

        ]

        if name not in codes
    ]


    if missing:

        raise ValueError(

            "codes.json is missing codes for: "

            + ", ".join(missing)
        )


    return saved_date, codes


# ============================================================
# LOAD DATA
# ============================================================

SAVED_DATE, DAILY_CODES = load_daily_data()


# ============================================================
# ADD CODE + DATE TO CARDS
# ============================================================

for card in CONFIG["cards"]:

    title = card["title"]


    if title not in DAILY_CODES:

        raise ValueError(

            f"No code found in codes.json "
            f"for {title}"
        )


    # Code comes from JSON
    card["code"] = str(
        DAILY_CODES[title]
    )


    # Date comes from JSON
    card["date"] = str(
        SAVED_DATE
    )


# ============================================================
# FONT LOADER
# ============================================================

def load_font(
    path,
    size
):

    possible_paths = [

        path,

        # Linux
        "/usr/share/fonts/truetype/dejavu/"
        "DejaVuSans.ttf",

        "/usr/share/fonts/truetype/dejavu/"
        "DejaVuSans-Bold.ttf",

        # Windows
        "C:/Windows/Fonts/arial.ttf",

        "C:/Windows/Fonts/arialbd.ttf",

        # macOS
        "/System/Library/Fonts/"
        "Supplemental/Arial.ttf",

        "/System/Library/Fonts/"
        "Supplemental/Arial Bold.ttf",

    ]


    for font_path in possible_paths:

        try:

            if Path(
                font_path
            ).exists():

                return ImageFont.truetype(
                    font_path,
                    size
                )

        except Exception:

            pass


    raise FileNotFoundError(

        f"Could not find font: {path}\n"

        "Please provide a valid .ttf or .otf font."
    )


# ============================================================
# HEX COLOR → RGB
# ============================================================

def hex_to_rgb(
    hex_color
):

    hex_color = hex_color.lstrip(
        "#"
    )


    return tuple(

        int(
            hex_color[i:i + 2],
            16
        )

        for i in (
            0,
            2,
            4
        )

    )


# ============================================================
# IMAGE COVER
# ============================================================

def cover_image(
    img,
    target_width,
    target_height,
    position_x=50,
    position_y=50
):

    """
    Resize image so it completely covers
    the card.

    position_x:
        0   = crop favors left
        50  = centered
        100 = crop favors right

    position_y:
        0   = crop favors top
        50  = centered
        100 = crop favors bottom
    """


    source_width, source_height = (
        img.size
    )


    source_ratio = (
        source_width /
        source_height
    )


    target_ratio = (
        target_width /
        target_height
    )


    # ========================================================
    # RESIZE
    # ========================================================

    if source_ratio > target_ratio:

        # Image is wider

        new_height = target_height

        new_width = int(
            new_height *
            source_ratio
        )


    else:

        # Image is taller

        new_width = target_width

        new_height = int(
            new_width /
            source_ratio
        )


    img = img.resize(

        (
            new_width,
            new_height
        ),

        Image.Resampling.LANCZOS
    )


    # ========================================================
    # CROP POSITION
    # ========================================================

    extra_x = (
        new_width -
        target_width
    )


    extra_y = (
        new_height -
        target_height
    )


    left = int(

        extra_x *
        (
            position_x /
            100
        )
    )


    top = int(

        extra_y *
        (
            position_y /
            100
        )
    )


    # ========================================================
    # CROP
    # ========================================================

    return img.crop(

        (
            left,
            top,

            left +
            target_width,

            top +
            target_height
        )
    )


# ============================================================
# DRAW CENTERED TEXT
# ============================================================

def draw_centered_text(
    draw,
    xy,
    text,
    font,
    fill
):

    bbox = draw.textbbox(

        (0, 0),

        text,

        font=font
    )


    width = (
        bbox[2] -
        bbox[0]
    )


    height = (
        bbox[3] -
        bbox[1]
    )


    x = (
        xy[0] -
        width / 2
    )


    y = (
        xy[1] -
        height / 2
    )


    draw.text(

        (
            x,
            y
        ),

        text,

        font=font,

        fill=fill
    )


# ============================================================
# DRAW ONE CARD
# ============================================================

def draw_card(
    canvas,
    card,
    settings,
    x,
    y,
    width,
    height
):

    # ========================================================
    # LOAD IMAGE
    # ========================================================

    image_path = Path(
        card["image"]
    )


    if not image_path.exists():

        raise FileNotFoundError(

            f"Image not found:\n"
            f"{image_path}"
        )


    image = Image.open(
        image_path
    ).convert("RGB")


    # ========================================================
    # IMAGE CROP POSITION
    # ========================================================

    image_x = settings.get(
        "image_x",
        50
    )


    image_y = settings.get(
        "image_y",
        50
    )


    # ========================================================
    # COVER CARD WITH IMAGE
    # ========================================================

    image = cover_image(

        image,

        width,

        height,

        image_x,

        image_y
    )


    # ========================================================
    # BRIGHTNESS
    # ========================================================

    brightness = settings.get(

        "brightness",

        1.0
    )


    if brightness != 1.0:

        image = (
            ImageEnhance
            .Brightness(image)
            .enhance(brightness)
        )


    # ========================================================
    # PUT IMAGE ON CANVAS
    # ========================================================

    canvas.paste(

        image,

        (
            x,
            y
        )
    )


    # ========================================================
    # DARK OVERLAY
    # ========================================================

    overlay_opacity = settings.get(

        "overlay_opacity",

        CONFIG[
            "overlay_opacity"
        ]
    )


    overlay_opacity = max(

        0.0,

        min(
            1.0,
            overlay_opacity
        )
    )


    overlay = Image.new(

        "RGBA",

        (
            width,
            height
        ),

        (
            0,
            0,
            0,

            int(
                255 *
                overlay_opacity
            )
        )
    )


    canvas.paste(

        overlay,

        (
            x,
            y
        ),

        overlay
    )


    # ========================================================
    # DRAW
    # ========================================================

    draw = ImageDraw.Draw(
        canvas
    )


    # ========================================================
    # LOAD TITLE FONT
    # ========================================================

    title_font = load_font(

        CONFIG[
            "title_font"
        ],

        settings.get(

            "title_size",

            CONFIG[
                "title_size"
            ]
        )
    )


    # ========================================================
    # LOAD CODE FONT
    #
    # THIS IS BOLD
    # ========================================================

    code_font = load_font(

        CONFIG[
            "code_font"
        ],

        settings.get(

            "code_size",

            CONFIG[
                "code_size"
            ]
        )
    )


    # ========================================================
    # LOAD DATE FONT
    # ========================================================

    date_font = load_font(

        CONFIG[
            "date_font"
        ],

        settings.get(

            "date_size",

            CONFIG[
                "date_size"
            ]
        )
    )


    # ========================================================
    # TEXT POSITION
    # ========================================================

    text_x_percent = settings.get(

        "text_x",

        CONFIG[
            "text_x"
        ]
    )


    text_y_percent = settings.get(

        "text_y",

        CONFIG[
            "text_y"
        ]
    )


    center_x = (

        x +

        width *
        (
            text_x_percent /
            100
        )
    )


    center_y = (

        y +

        height *
        (
            text_y_percent /
            100
        )
    )


    # ========================================================
    # TEXT
    # ========================================================

    title = str(
        card["title"]
    )


    code = str(
        card["code"]
    )


    # ========================================================
    # MEASURE TITLE
    # ========================================================

    title_bbox = draw.textbbox(

        (0, 0),

        title,

        font=title_font
    )


    title_height = (

        title_bbox[3] -
        title_bbox[1]
    )


    # ========================================================
    # MEASURE CODE
    # ========================================================

    code_bbox = draw.textbbox(

        (0, 0),

        code,

        font=code_font
    )


    code_height = (

        code_bbox[3] -
        code_bbox[1]
    )


    # ========================================================
    # SPACING
    # ========================================================

    spacing = settings.get(

        "title_code_spacing",

        CONFIG[
            "title_code_spacing"
        ]
    )


    total_height = (

        title_height +

        spacing +

        code_height
    )


    # ========================================================
    # TITLE Y
    # ========================================================

    title_y = (

        center_y -

        total_height / 2
    )


    # ========================================================
    # CODE Y
    # ========================================================

    code_y = (

        title_y +

        title_height +

        spacing
    )


    # ========================================================
    # DRAW TITLE
    # ========================================================

    draw_centered_text(

        draw,

        (
            center_x,

            title_y +
            title_height / 2
        ),

        title,

        title_font,

        settings.get(

            "title_color",

            CONFIG[
                "title_color"
            ]
        )
    )


    # ========================================================
    # DRAW CODE
    #
    # CODE IS BOLD BECAUSE code_font IS
    # DejaVuSans-Bold.ttf
    # ========================================================

    draw_centered_text(

        draw,

        (
            center_x,

            code_y +
            code_height / 2
        ),

        code,

        code_font,

        settings.get(

            "code_color",

            CONFIG[
                "code_color"
            ]
        )
    )


    # ========================================================
    # DATE — BOTTOM LEFT
    # ========================================================

    date = str(
        card["date"]
    )


    date_x_percent = settings.get(

        "date_x",

        CONFIG[
            "date_x"
        ]
    )


    date_y_percent = settings.get(

        "date_y",

        CONFIG[
            "date_y"
        ]
    )


    date_x = (

        x +

        width *
        (
            date_x_percent /
            100
        )
    )


    date_y = (

        y +

        height *
        (
            date_y_percent /
            100
        )
    )


    draw.text(

        (
            date_x,
            date_y
        ),

        date,

        font=date_font,

        fill=settings.get(

            "date_color",

            CONFIG[
                "date_color"
            ]
        ),

        anchor="lm"
    )


# ============================================================
# CREATE SQUARE CANVAS
# ============================================================

canvas_width = CONFIG[
    "canvas_width"
]


canvas_height = CONFIG[
    "canvas_height"
]


canvas = Image.new(

    "RGB",

    (
        canvas_width,
        canvas_height
    ),

    hex_to_rgb(

        CONFIG[
            "gap_color"
        ]
    )
)


# ============================================================
# GRID
# ============================================================

columns = 3
rows = 2

gap = CONFIG[
    "gap"
]


# ============================================================
# CARD WIDTH
# ============================================================

card_width = (

    canvas_width -

    gap *
    (
        columns - 1
    )

) // columns


# ============================================================
# CARD HEIGHT
#
# 100 = square cards
# 90  = slightly rectangular
# 85  = recommended
# 80  = more rectangular
# ============================================================

CARD_HEIGHT_PERCENT = 85


natural_card_height = (

    canvas_height -

    gap *
    (
        rows - 1
    )

) // rows


card_height = int(

    natural_card_height *

    (
        CARD_HEIGHT_PERCENT /
        100
    )
)


# ============================================================
# TOTAL GRID HEIGHT
# ============================================================

grid_height = (

    card_height *
    rows

    +

    gap *
    (
        rows - 1
    )
)


# ============================================================
# CENTER GRID VERTICALLY
# ============================================================

top_margin = (

    canvas_height -

    grid_height

) // 2


# ============================================================
# CHECK SIX CARDS
# ============================================================

if len(
    CONFIG["cards"]
) != 6:

    raise ValueError(

        "CONFIG['cards'] must "
        "contain exactly 6 images."
    )


if len(
    CONFIG["card_settings"]
) != 6:

    raise ValueError(

        "CONFIG['card_settings'] "
        "must contain exactly "
        "6 settings dictionaries."
    )


# ============================================================
# DRAW ALL SIX CARDS
# ============================================================

for index, card in enumerate(

    CONFIG["cards"]
):

    # ========================================================
    # ROW
    # ========================================================

    row = (
        index //
        columns
    )


    # ========================================================
    # COLUMN
    # ========================================================

    column = (
        index %
        columns
    )


    # ========================================================
    # X POSITION
    # ========================================================

    x = (

        column *

        (
            card_width +
            gap
        )
    )


    # ========================================================
    # Y POSITION
    # ========================================================

    y = (

        top_margin +

        row *

        (
            card_height +
            gap
        )
    )


    # ========================================================
    # DEFAULT SETTINGS
    # ========================================================

    settings = {

        "title_size":
            CONFIG[
                "title_size"
            ],

        "code_size":
            CONFIG[
                "code_size"
            ],

        "date_size":
            CONFIG[
                "date_size"
            ],


        "title_color":
            CONFIG[
                "title_color"
            ],

        "code_color":
            CONFIG[
                "code_color"
            ],

        "date_color":
            CONFIG[
                "date_color"
            ],


        "text_x":
            CONFIG[
                "text_x"
            ],

        "text_y":
            CONFIG[
                "text_y"
            ],


        "date_x":
            CONFIG[
                "date_x"
            ],

        "date_y":
            CONFIG[
                "date_y"
            ],


        "title_code_spacing":
            CONFIG[
                "title_code_spacing"
            ],


        "overlay_opacity":
            CONFIG[
                "overlay_opacity"
            ],

        "brightness":
            CONFIG[
                "brightness"
            ],


        "image_x":
            50,

        "image_y":
            50,
    }


    # ========================================================
    # INDIVIDUAL OVERRIDES
    # ========================================================

    settings.update(

        CONFIG[
            "card_settings"
        ][index]
    )


    # ========================================================
    # DRAW CARD
    # ========================================================

    draw_card(

        canvas,

        card,

        settings,

        x,

        y,

        card_width,

        card_height
    )


# ============================================================
# SAVE
# ============================================================

canvas.save(

    CONFIG[
        "output"
    ],

    quality=95
)


# ============================================================
# INFORMATION
# ============================================================

print()

print(
    "=" * 60
)

print(
    "IMAGE CREATED"
)

print(
    "=" * 60
)

print(
    f"Output: "
    f"{CONFIG['output']}"
)

print(
    f"Size: "
    f"{canvas_width} × "
    f"{canvas_height}"
)

print(
    "Aspect ratio: 1:1"
)

print(
    f"Card size: "
    f"{card_width} × "
    f"{card_height}"
)

print(
    f"Card height: "
    f"{CARD_HEIGHT_PERCENT}%"
)

print(
    f"Date: "
    f"{SAVED_DATE}"
)

print()

print(
    "Codes:"
)

for card in CONFIG["cards"]:

    print(

        f"  {card['title']:<20}"
        f"{card['code']}"
    )

print(
    "=" * 60
)