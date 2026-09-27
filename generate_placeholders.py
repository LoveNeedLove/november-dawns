import os
import struct
import zlib

# ==========================================
# CONFIGURATION
# ==========================================
OUTPUT_DIR = "game/images/illu"
DEFAULT_WIDTH = 449
DEFAULT_HEIGHT = 489
INPUT_FILE = "to_generate.txt"
# ==========================================

# Police bitmap 5x7 minimale (caractères ASCII de base)
FONT_5X7 = {
    ' ': [0x00, 0x00, 0x00, 0x00, 0x00],
    'A': [0x7E, 0x11, 0x11, 0x11, 0x7E], 'B': [0x7F, 0x49, 0x49, 0x49, 0x36],
    'C': [0x3E, 0x41, 0x41, 0x41, 0x22], 'D': [0x7F, 0x41, 0x41, 0x22, 0x1C],
    'E': [0x7F, 0x49, 0x49, 0x49, 0x41], 'F': [0x7F, 0x09, 0x09, 0x09, 0x01],
    'G': [0x3E, 0x41, 0x49, 0x49, 0x7A], 'H': [0x7F, 0x08, 0x08, 0x08, 0x7F],
    'I': [0x00, 0x41, 0x7F, 0x41, 0x00], 'J': [0x20, 0x40, 0x41, 0x3F, 0x01],
    'K': [0x7F, 0x08, 0x14, 0x22, 0x41], 'L': [0x7F, 0x40, 0x40, 0x40, 0x40],
    'M': [0x7F, 0x02, 0x0C, 0x02, 0x7F], 'N': [0x7F, 0x04, 0x08, 0x10, 0x7F],
    'O': [0x3E, 0x41, 0x41, 0x41, 0x3E], 'P': [0x7F, 0x09, 0x09, 0x09, 0x06],
    'Q': [0x3E, 0x41, 0x51, 0x21, 0x5E], 'R': [0x7F, 0x09, 0x19, 0x29, 0x46],
    'S': [0x46, 0x49, 0x49, 0x49, 0x31], 'T': [0x01, 0x01, 0x7F, 0x01, 0x01],
    'U': [0x3F, 0x40, 0x40, 0x40, 0x3F], 'V': [0x1F, 0x20, 0x40, 0x20, 0x1F],
    'W': [0x7F, 0x20, 0x18, 0x20, 0x7F], 'X': [0x63, 0x14, 0x08, 0x14, 0x63],
    'Y': [0x07, 0x08, 0x70, 0x08, 0x07], 'Z': [0x61, 0x51, 0x49, 0x45, 0x43],
    '0': [0x3E, 0x51, 0x49, 0x45, 0x3E], '1': [0x00, 0x42, 0x7F, 0x40, 0x00],
    '2': [0x42, 0x61, 0x51, 0x49, 0x46], '3': [0x21, 0x41, 0x45, 0x4B, 0x31],
    '4': [0x18, 0x14, 0x12, 0x7F, 0x10], '5': [0x27, 0x45, 0x45, 0x45, 0x39],
    '6': [0x3C, 0x4A, 0x49, 0x49, 0x30], '7': [0x01, 0x71, 0x09, 0x05, 0x03],
    '8': [0x36, 0x49, 0x49, 0x49, 0x36], '9': [0x06, 0x49, 0x49, 0x29, 0x1E],
    '_': [0x40, 0x40, 0x40, 0x40, 0x40], '-': [0x08, 0x08, 0x08, 0x08, 0x08],
    '.': [0x00, 0x60, 0x60, 0x00, 0x00], ':': [0x00, 0x36, 0x36, 0x00, 0x00],
    '(': [0x00, 0x3E, 0x41, 0x00, 0x00], ')': [0x00, 0x00, 0x41, 0x3E, 0x00],
    'X': [0x63, 0x14, 0x08, 0x14, 0x63]
}

def render_text_to_grid(grid, width, height, text, center_y, scale=4):
    text = text.upper()
    char_w = 6 * scale
    total_w = len(text) * char_w
    start_x = max(0, (width - total_w) // 2)
    start_y = max(0, center_y - (7 * scale) // 2)

    for i, char in enumerate(text):
        cols = FONT_5X7.get(char, FONT_5X7[' '])
        char_x = start_x + (i * char_w)
        for col_idx, col_bits in enumerate(cols):
            for row_idx in range(7):
                if (col_bits >> row_idx) & 1:
                    for sy in range(scale):
                        for sx in range(scale):
                            px = char_x + col_idx * scale + sx
                            py = start_y + row_idx * scale + sy
                            if 0 <= px < width and 0 <= py < height:
                                grid[py][px] = 1

def make_real_png_with_text(filepath, width, height, filename):
    def chunk(tag, data):
        return (
            struct.pack(">I", len(data))
            + tag
            + data
            + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
        )

    png_magic = b"\x89PNG\r\n\x1a\n"
    ihdr = chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0))

    text_grid = [bytearray(width) for _ in range(height)]
    scale = max(2, min(width, height) // 200)

    mid_y = height // 2
    render_text_to_grid(text_grid, width, height, "PLACEHOLDER", mid_y - (18 * scale), scale=scale + 1)
    render_text_to_grid(text_grid, width, height, filename, mid_y, scale=scale)
    render_text_to_grid(text_grid, width, height, f"{width}X{height}", mid_y + (18 * scale), scale=max(2, scale - 1))

    border_px = b"\xc8\xc8\xc8"
    bg_px = b"\x23\x25\x2e"
    text_px = b"\xff\xff\xff"
    border_thickness = 4

    raw_data = bytearray()
    for y in range(height):
        raw_data.append(0)
        is_border_y = (y < border_thickness) or (y >= height - border_thickness)
        row = text_grid[y]
        for x in range(width):
            if is_border_y or (x < border_thickness) or (x >= width - border_thickness):
                raw_data.extend(border_px)
            elif row[x]:
                raw_data.extend(text_px)
            else:
                raw_data.extend(bg_px)

    idat = chunk(b"IDAT", zlib.compress(bytes(raw_data), level=6))
    iend = chunk(b"IEND", b"")

    with open(filepath, "wb") as f:
        f.write(png_magic + ihdr + idat + iend)

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Erreur : '{INPUT_FILE}' introuvable.")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    created_files = []
    skipped_files = []

    for line in lines:
        filename = line.strip()
        if not filename or filename.startswith("#"):
            continue

        filepath = os.path.join(OUTPUT_DIR, filename)

        # Vérification d'existence avant toute création
        if os.path.exists(filepath):
            skipped_files.append(filename)
            continue

        ext = os.path.splitext(filename)[1].lower()

        if ext == ".png":
            make_real_png_with_text(filepath, DEFAULT_WIDTH, DEFAULT_HEIGHT, filename)
            print(f"[PNG] Généré : {filename}")
        else:
            with open(filepath, "w", encoding="utf-8") as dummy:
                dummy.write(f"# Placeholder pour {filename}\n")
            print(f"[TXT/AUTRE] Créé : {filename}")

        created_files.append(filename)

    # Récapitulatif console
    print("\n" + "=" * 40)
    print("BILAN D'EXÉCUTION")
    print("=" * 40)
    print(f"Nouveaux fichiers créés : {len(created_files)}")
    print(f"Fichiers ignorés (déjà existants) : {len(skipped_files)}")

    if skipped_files:
        print("\nFichiers non écrasés :")
        for name in skipped_files:
            print(f"  - {name}")
    print("=" * 40)

if __name__ == "__main__":
    main()